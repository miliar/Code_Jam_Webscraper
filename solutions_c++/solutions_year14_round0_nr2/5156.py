#include<stdio.h>
int main()
{
	int i,j,k,l,t;
	double m,n,f,v,c,x,sum1,sum2,sum3;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		sum1=1.0;
		sum2=0.0;sum3=0.0;m=0.0;
		n=2.0;
		while(sum1>=sum2+sum3)
		{
		n=n+m;
		sum1=x/n;
		sum1+=sum2;
		sum2+=c/n;
		m=f;
		sum3=x/(n+m);	
		}
		printf("Case #%d: %.7lf\n",i+1,sum1);
	}
	return 0;
}
