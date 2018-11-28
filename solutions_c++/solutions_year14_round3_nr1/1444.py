#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;
long long int g(long long int x,long long int y)//�����Լ��
{
	long long int r;
	while(y>0)
	{
		r=x%y;
		x=y;
		y=r;
	}
	return x;
}
long long int how(long long int q)//���Ƿ�Ϊ2����
{
	long long int i=0;
	while(q > 1)
	{
		long long int a = q%2;
		if (a!=0) return -1;
		else 
		{
			q = q/2;
			i++;
		}
	}
	return i;
}
int main()
{
	int T;
	long long int P,Q;
	FILE *inf = fopen("A-large.in","r");
	FILE *outf = fopen("testl.out","w");
	fscanf(inf,"%d",&T);
	for(int m=1; m<=T; m++)
	{
		fscanf(inf,"%lld/%lld\n",&P,&Q);
		long long int temp = g(P,Q);
		P = P/temp;
		Q = Q/temp;
		long long int ho = how(Q);
		if (ho == -1)
		{
			fprintf(outf,"Case #%d: impossible\n",m);
			continue;
		}
		bool flag = false;
		for (long long int i=ho;i>0;i--)
		{
			if(P >= pow((float)2,(int)i-1))
			{
				fprintf(outf,"Case #%d: %d\n",m,(ho -i+1));
				flag = true;
				break;
			}
		}
		if (flag == false)
		{
			fprintf(outf,"Case #%d: impossible\n",m);
		}
	
	}
	printf("OK!");
	getchar();
	fclose(inf);
	fclose(outf);

	return 0;
}
