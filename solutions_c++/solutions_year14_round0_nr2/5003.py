#include<stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
	int o=1;
	while(t--)
	{double c,f,x;
	scanf("%lf%lf%lf",&c,&f,&x);
	double d=2.0;
	
	double a;
	
	double sum=x/d;
	double ans=0.0;
	for(;;)
	{
	a=c/d;
	ans+=a;
	d+=f;
	double b=x/d;
	if(ans+b>=sum)
	break;
	else sum=ans+b;	
	
		}printf("Case #%d: %0.7lf\n",o,sum);
		o++;}
		return 0;
}
