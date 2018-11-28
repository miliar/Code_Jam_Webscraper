#include<cstdio>

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		double T=0,A=1e100;
		for(int i=0;;i++)
		{
			const double a=T+X/(2+i*F);
			if(a>=A)break;
			A=a;
			T+=C/(2+i*F);
		}
		printf("Case #%d: %.7f\n",t,A);
	}
	return 0;
}
