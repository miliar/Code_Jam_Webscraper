#include<stdio.h>
#include<stdlib.h>
int main()
{
	int t,n1,n2,i,j,temp,x;
	double F,C,X;
	scanf("%d",&t);
	for(x=1;x<=t;x++)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		double time=0.0,rate=2.0,chip=0.0;
		while(chip<X)
		{
			double t1=time+X/rate;
			double t2=time+C/rate+X/(F+rate);
			if(t1>t2)
			{
				time=time+C/rate;
				rate=rate+F;
				
			}
			else
			{
				time=time+X/rate;
				break;
			}
		}
		printf("Case #%d: %lf\n",x,time);
	}
	
}