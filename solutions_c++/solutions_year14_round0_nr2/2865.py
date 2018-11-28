#include <iostream>
#include <stdio.h>

using namespace std;

void HandleCases(int caseCount) {
	for (int i = 1; i <= caseCount; i++) {
		double cost = 0;
		double target = 0;
		double extraSpeed = 0;
		cin >> cost >> extraSpeed >> target;

		double speed = 2;
		double time_buy = 0;
		double time_not_buy = 0;
		double baseTime = 0;
		
		while (1){
			time_not_buy = target / speed;
			//cout << "time_not_buy is " << time_not_buy <<endl;
			time_buy = cost / speed + target / (speed + extraSpeed);
			//cout << "time_buy is " << time_buy <<endl;
			baseTime += (time_buy > time_not_buy ? 0 : cost / speed);
			//cout << "baseTime is " << baseTime <<endl;
			if (time_not_buy < time_buy) {
				baseTime += time_not_buy;
				break;
			}
			speed += extraSpeed;
		}
		printf("Case #%d: %.7lf\n", i, baseTime);
	}
}

int main() {
	int caseCount = 0;
	cin >> caseCount;

	HandleCases(caseCount);
}
