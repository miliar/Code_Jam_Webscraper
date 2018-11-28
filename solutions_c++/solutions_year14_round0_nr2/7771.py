#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {

	int nTests;
	cin >> nTests;
	for (int i = 1; i <= nTests; i++) {
		double farmCost, farmProduce, finalGoal;
		cin >> farmCost >> farmProduce >> finalGoal;
	
		double time1 = finalGoal / 2.0;
		double time2 = farmCost / 2.0;
		if (time2 >= time1) {
			printf("Case #%d: %.7f\n", i, time1);
			continue;
		}

		double produceSpeed = 2.0;
		double timeCount = time2;
		double cookieCount = farmCost;
		while (cookieCount < finalGoal) {
			double needCookie = finalGoal - cookieCount;

			// time1: we wait until reach final goal
			double time1 = needCookie / produceSpeed;

			// time2: how long have we to wait to buy a farm
			double time2 = finalGoal / (produceSpeed + farmProduce);
			
			if (time2 >= time1) {
				timeCount += time1;
				break;
			} else {
				produceSpeed += farmProduce;
				timeCount += farmCost / produceSpeed;
				cookieCount = farmCost;
			}
		}
		printf("Case #%d: %.7f\n", i, timeCount);
	}

	return 0;
}
