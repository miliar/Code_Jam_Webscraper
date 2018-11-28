#include <stdio.h>
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		double C,F,X,rate=2.0,time=0.0;
		scanf("%lf %lf %lf",&C,&F,&X);
		while(1)
		{
			if(X<(X-C)/rate*(rate+F))
			{
				time+=C/rate;
				rate+=F;
			}
			else
			{
				time+=X/rate;
				break;
			}
		}
		printf("Case #%d: %.7lf\n",t,time);
	}
	return 0;
}
