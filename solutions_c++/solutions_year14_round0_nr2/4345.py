#include <cstdio>

int main()
{
	freopen("in2.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	
	int testCase;
	double C,F,X,prev = 0;
	double timeT(0.0),time1(0.0),time2(0.0),rate(2.0);
	
	scanf("%d",&testCase);
	
	for(int test = 1; test <= testCase; test++)
	{
		
		scanf("%lf%lf%lf",&C,&F,&X);
		
		while(true)
		{
			if(prev == 0)
			{
				timeT += C/rate;
				prev = C;
			}
			
			time1 = (X-prev)/rate;
			time2 = (X)/(rate+F);
			
			if(time1 < time2)
			{
				timeT += time1;
				break;
			}
			else
			{
				timeT += C/(rate+F);
				rate += F;
			}
		}
		printf("Case #%d: %.7lf\n",test,timeT);
		prev = 0;
		timeT = 0.0;
		rate = 2.0;
		
	}
}
