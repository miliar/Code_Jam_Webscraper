#include <cstdio>

using namespace std;

int main() {

	int testcases;
	scanf("%d", &testcases);

	for (int tc=1; tc<testcases+1; tc++) {
		printf("Case #%d: ", tc);

		double farmCost, farmRate, winThreshold;
		scanf("%lf %lf %lf", &farmCost, &farmRate, &winThreshold);

		// double currentMoney = 0;
		double currentRate = 2.0;

		// can either wait for farmCost to buy a farm, or wait to cross the threshold

		double timeTaken = 0.0;

		// printf("%lf %lf %lf\n", farmCost, farmRate, winThreshold);

// int i=0;
		while (true) {
			// i++;
			// if (i > 20) {
			// 	printf("dead\n");
			// 	break;
			// }
			double timeForNextFarm = farmCost / currentRate;
			double timeForNextFarmThenWin = farmCost / currentRate + winThreshold / (currentRate + farmRate);
			double timeToWin = winThreshold / currentRate;
			// printf("next farm %lf\n", timeForNextFarm);
			// printf("next farm then win %lf\n", timeForNextFarmThenWin);
			// printf("win %lf\n", timeToWin);

			if (timeToWin < timeForNextFarmThenWin) {
				// win
				timeTaken += timeToWin;
				break;
			}
			else {
				// buy a farm
				currentRate += farmRate;
				timeTaken += timeForNextFarm;
			}
		}

		printf("%.7lf\n", timeTaken);
		
	}

	return 0;
}