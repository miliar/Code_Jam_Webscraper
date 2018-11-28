#include <cstdio>
using namespace std;

int main()
{
	freopen ("2014qualsB.in", "r", stdin);
	freopen ("2014qualsB.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);

		double rate = 2, total = 0;
		while (true)
		{
			if (C/rate + X/(rate+F) < X/rate)
			{
				total += C/rate;
				rate += F;
			}
			else
			{
				total += X/rate;
				break;
			}
		}

		printf("Case #%d: %.7f\n", t, total);
	}

	return 0;
}