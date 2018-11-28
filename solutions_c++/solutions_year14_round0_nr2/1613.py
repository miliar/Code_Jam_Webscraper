#include <cstdio>
int main()
{
	int t;
	scanf("%d",&t);
	for(int z = 1; z <= t; z++) {
		double c,f,x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double min = x / 2;
		double startTime = 0;
		double newRate = 2;
		while(1)
		{
			startTime += (c / newRate);
			newRate += f;
			double newTime = startTime + x / newRate;
			if(newTime < min)
			{
				min = newTime;
			}
			else
			{
				break;
			}
		}
		printf("Case #%d: %.7lf\n",z, min);
	}
	return 0;
}