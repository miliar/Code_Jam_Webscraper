#include <cstdio>

using namespace std;

int main()
{
	freopen("cookie.in", "r", stdin);
	freopen("cookie.out", "w", stdout);

	int casesCount;
	scanf("%d", &casesCount);

	for (int currentCase = 1; currentCase <= casesCount; currentCase++)
	{
		double cost, rateGain, goal;
		scanf("%lf%lf%lf", &cost, &rateGain, &goal);

		double currentRate = 2;
		double totalTime = 0;
		while(true)
		{
			double timeToGoal = goal / currentRate;
			double timeWithFarm = cost / currentRate + goal / (currentRate + rateGain);
			if (timeToGoal <= timeWithFarm)
			{
				totalTime += timeToGoal;
				break;
			}

			totalTime += cost / currentRate;
			currentRate += rateGain;
		}

		printf("Case #%d: %.7lf\n", currentCase, totalTime);
	}
	return 0;
}