// google jam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string.h>
#include <math.h>
#include <stdlib.h>

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,t=0;  //测试次数
	int A,B;
	int result; //结果
	int fs[5] = {1,4,9,121,484};//存储数据
	scanf("%d",&T);  //获取测试次数
	while(t++<T)
	{
		result = 0;

		scanf("%d",&A);
		scanf("%d",&B);

		for(int i=0;i<5;++i)
		{
			if(fs[i]>=A && fs[i]<=B)
				result ++;
		}

		printf("Case #%d: %d\n",t,result);
	}
	return 0;
}

