// google jam.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <string.h>
#include <math.h>
#include <stdlib.h>



int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,t=0;  //���Դ���
	int r,t0;//��ʼ�뾶����ī
	int result;//���
	scanf("%d",&T);  //��ȡ���Դ���
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

