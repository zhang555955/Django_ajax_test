from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def getPage(request):
    '''
    返回页面
    '''
    return render(request,'Django_Ajax_Project.html')


def sendData(request):
    '''
    响应ajax请示
    内容是json对象
    '''
    return JsonResponse({'data': 'hello world'})