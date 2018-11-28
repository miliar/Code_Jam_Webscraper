#include <cstdio>
#include <iostream>
using namespace std;

int main(void) {
	int t, testCases;
	double farmCost, farmRate, cookiesToWin, totalTime;
	double rate, timeNoFarm, timeToFarm, timeUseFarm;
	cin >> testCases;
	for (t=1; t<=testCases; t++) {
		cin >> farmCost >> farmRate >> cookiesToWin;
		rate = 2.0;
		totalTime = 0.0;
		while (1) {
			//either buy farm as soon as possible or don't buy at all
			timeNoFarm = cookiesToWin / rate;
			timeToFarm = farmCost / rate;
			timeUseFarm = timeToFarm + (cookiesToWin / (rate+farmRate));
			if (timeNoFarm < timeUseFarm) {
				totalTime += timeNoFarm;
				break;
			}
			else {
				totalTime += timeToFarm;
				rate += farmRate;
			}
		}
		
		printf("Case #%d: %.7lf\n", t, totalTime);
	}
	
	
	return 0;
}