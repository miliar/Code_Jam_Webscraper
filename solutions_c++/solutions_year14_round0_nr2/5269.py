#include<stdio.h>

int main()
{

	int i,t;
	double c,f,x,y,sum,r,l,m;
	double a[100];
	scanf("%d",&t);
	for(i=0; i<t; i++)
	{       y=0.0000000,sum=0.0000000,r=2.00000;
		scanf("%lf%lf%lf",&c,&f,&x);
		while((c/r+(x/(r+f)))<(x/r))
		{
			sum=c/r;
			r+=f;
			y+=sum;
		};
		sum=x/r;
		y+=sum;
		a[i]=y;





	}
	for(i=0; i<t; i++)
	{
		printf("\nCase #%d: %.7lf",i+1,a[i]);
	}
	return 0;

}
