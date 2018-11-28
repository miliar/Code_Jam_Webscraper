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
	int r,t0;//初始半径，油墨
	int result;//结果
	scanf("%d",&T);  //获取测试次数
	while(t++<T)
	{
		scanf("%d",&r);
		scanf("%d",&t0);

		result = 0;

		for(int tmp=0;tmp<=t0;++result)
		{
			tmp += 2*r + 1;
			r +=2;
		}

		printf("Case #%d: %d\n",t,result-1);
	}
	return 0;
}

