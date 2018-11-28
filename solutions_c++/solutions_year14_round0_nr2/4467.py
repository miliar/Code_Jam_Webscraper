#include <stdio.h>

double howManySeconds(double fps, double target) {
	return target / fps;
}

int main() {
	int qtos;
	scanf("%d",&qtos);
	for (int x = 1; x <= qtos; x++) {
		double factoryCost, extraFps, currentFps,target;
		currentFps = 2.0;
		int finish = 0;
		double totalTimeSpent = 0;
		scanf("%lf %lf %lf",&factoryCost, &extraFps, &target);
		while (!finish) {
			double timeFlat = howManySeconds(currentFps,target);
			double timeToReachFactory = howManySeconds(currentFps,factoryCost);
			double newTimeFlat = howManySeconds(currentFps + extraFps,target);
			if (timeFlat > timeToReachFactory + newTimeFlat) {
				currentFps += extraFps;
				totalTimeSpent += timeToReachFactory;
			} else {
				finish = 1;
				totalTimeSpent += timeFlat;
				break;
			}
		}

		printf("Case #%d: %.7lf\n",x,totalTimeSpent);
	}


	return 0;
}