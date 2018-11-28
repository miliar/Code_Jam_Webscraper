#include <cstdio>

int main(void)
{
	int cases;
	scanf("%i", &cases);
	for (int t = 0; t < cases; ++t)
	{
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double cookiesPerSecond = 2.0;
		double totTimeNow = 0;
		double bestTime = totTimeNow + x / cookiesPerSecond;
		while (totTimeNow < bestTime)
		{
			// Wait to buy a farm.
			double waitTime = c / cookiesPerSecond;
			totTimeNow += waitTime;
			cookiesPerSecond += f;
			double testTime = totTimeNow + x / cookiesPerSecond;
			if (testTime < bestTime)
				bestTime = testTime;
		}
		printf("Case #%i: %.7lf\n", t+1, bestTime);
	}
	return 0;
}