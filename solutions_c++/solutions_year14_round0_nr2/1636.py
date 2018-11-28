#include <stdio.h>
#define f(i,n) for(int i=0; i <n;i++)
int main()
{
	int t;
	scanf("%d",&t);
	f(i,t)
	{
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		double min =0, max = x/2+1;
		bool success = false;
		double best = -1;
		while(max-min>1e-7)
		{
			double mid = (max+min)/2;
			double time = mid;
			double rate = 2;
			
			while((time*rate)>=c && time*rate<x)
			{
				time-=c/rate;
				rate+=f;
			}

			if(time*rate>=x)
			{
				success = true;
				best = mid;
				max = mid;
			}
			else
			{
				min = mid;
			}
		}

		printf("Case #%d: %.7lf\n", i+1, best);
	}

	return 0;
}
