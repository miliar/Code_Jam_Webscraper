#include<cstdio>
#include<cstdlib>
#include<cmath>
int T, i;
double C, F, X, time, totaltime, rate;

int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
	{
		scanf("%lf %lf %lf", &C, &F, &X);
		time = 0;
		rate = 2.0;
		totaltime = X/2.0;
		double Cbyrate = C/rate;
		double Xbyrate = X/rate;
		totaltime=Xbyrate;	
		while(1)
		{
			rate += F;
			time += Cbyrate;
			Cbyrate = C/rate;
			Xbyrate = X/rate;
			if (time + Xbyrate>= totaltime)
				break;
			totaltime = time + Xbyrate;
		}
		printf("Case #%d: %0.7lf\n", t, totaltime);
	}
}