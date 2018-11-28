#include <iostream>
using namespace std;

const double INF_TIME = 1e5;

double solve(double farmCost, double additinalProfit, double targetCookies)
{
	double currentProfit = 2.0;
	double currentTime = 0.0;
	double currentCookies = 0.0;

	bool stop = false;
	while (targetCookies > currentCookies)
	{
		const double answer1 = currentTime + (targetCookies - currentCookies) / currentProfit;
		// Jeœli kupiê fabrykê.
		if (currentCookies >= farmCost)
		{
			const double numberOfFarms = (int)(currentCookies / farmCost);
			const double totalCost = numberOfFarms * farmCost;
			const double answer2 = currentTime + (targetCookies - currentCookies + totalCost) 
				/ (currentProfit + additinalProfit * numberOfFarms);

			if (answer2 < answer1)
			{
				currentProfit += additinalProfit * numberOfFarms;
				currentCookies -= totalCost;
				
				const double deltaTCookie = (farmCost - currentCookies) / currentProfit;
				currentTime += deltaTCookie;
				currentCookies += deltaTCookie * currentProfit;
			}
			else
				return answer1;
		}
		else
		{
			const double deltaTCookie = (farmCost - currentCookies) / currentProfit;
			const double deltaTTarget = (targetCookies - currentCookies) / currentProfit;
			double deltaT;
			if (deltaTCookie < deltaTTarget)
				deltaT = deltaTCookie;
			else
				deltaT = deltaTTarget;

			currentTime += deltaT;
			currentCookies += deltaT * currentProfit;
		}
	}

	return currentTime;
}
int main()
{
	int testCases;
	scanf("%d", &testCases);
	for (int testCase = 1; testCase <= testCases; ++testCase)
	{
		double farmCost, additionalProfit, targetCookies;
		scanf("%lf%lf%lf", &farmCost, &additionalProfit, &targetCookies);
		printf("Case #%d: %.7lf\n", testCase, solve(farmCost, additionalProfit, targetCookies));
	}

	return 0;
}