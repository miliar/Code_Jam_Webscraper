#include<stdio.h>
int main()
{
	int i,t,j,lim;
	double x,c,f,den,sum;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		den=2.0;
		sum=0.0;
		lim = (int)(x/c - 2/f);
		for(j=1;j<lim;j++)
		{
			sum +=c/den;
			den = den+f;
			printf("Case #%d: %lf\n",i,sum);
		}
		sum+=x/den;
		printf("Case #%d: %lf\n",i,sum);
	}
	return 0;
}
