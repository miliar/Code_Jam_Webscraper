#include <stdio.h>

int numTestcases = 1, i = 0;
double cost = 1, farm = 1, target = 1, produce = 2;
double timeConsume = 0, nextTime = 0;

void handleTestCase() {
	timeConsume = 0, produce = 2;
	while (true) {
		nextTime = cost / produce;
		if ((nextTime + target / (produce + farm)) >= target / produce) {
			timeConsume += target / produce;
			// printf("%.7f %.7f\n", target / produce, timeConsume);
			break;
		}
		timeConsume += nextTime, produce += farm;
		// printf("%.7f ", nextTime);
	}
}

void printCaseResult() {

}

int main() {
	scanf("%d", &numTestcases);
	for (int i = 0; i < numTestcases; i++) {
		scanf("%lf %lf %lf", &cost, &farm, &target);
		// printf("debug %.7f %.7f %.7f\n", cost, farm, target);
		handleTestCase();
		printf("Case #%d: %.7f\n", i+1, timeConsume);
	}
	return 0;
}