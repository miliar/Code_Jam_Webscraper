#include<stdio.h>

int main()
{
	double time,cok,group,F,C,X,rate,current;	
	int T,test;
	scanf("%d",&T);
	for(test=1;test<=T;test++)
	{
		rate=2.0;
		cok=time=0.0;
		scanf("%lf%lf%lf",&C,&F,&X);
		while(cok<X)
		{
			if((cok+C)<X)
			{
				time=time+C/rate;
				cok=cok+C;
				if(((X-cok)/rate) > ((X-(cok-C))/(rate+F)))
				{
					rate=rate+F;
					cok=cok-C;
				}
				else
				{
					time=time+(X-cok)/rate;
					cok=X;
				}
			}
			else
			{
				time=time+(X-cok)/rate;
				cok=X;
			}
			
		}
		printf("Case #%d: %lf\n",test,time);
	}
	return 0 ;
}
	
		


















	
