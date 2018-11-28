#include <cstdio>
#include <cassert>

int main ()
{
	int T;
	scanf("%d", &T);
	double C, F, X;
	double bestSecs;
	double secs;
	double rate;

	for (int tcase = 1; tcase <= T; tcase++)
	{
		scanf("%lf %lf %lf", &C, &F, &X);
		secs = 0;
		rate = 2;
		bestSecs = X/rate;

		while (true)
		{
			//What happens if we buy another farm?
			secs += C/rate;
			rate += F;
			if (secs+(X/rate) < bestSecs) bestSecs = secs+(X/rate);
			if (secs >= bestSecs) break;
		}

		printf("Case #%d: %lf\n", tcase, bestSecs);
	}
}