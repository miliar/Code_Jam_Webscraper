#include <iostream>
#include <cfloat>
using namespace std;

int main()
{
	int tests;
	cin >> tests;
	for(int caseNum = 1; caseNum <= tests; caseNum++) {

		double farmCost;
		double farmOutput;
		double targetAmount;
		cin >> farmCost >> farmOutput >> targetAmount;

		double curTime; // 현재 목표량을 달성하는데 걸린 시간
		double preFarmTime = 0.0; // 이전에 농장을 다 짓는데 걸린 시간
		double minTime = targetAmount / 2.0; // 목표량을 달성하는데 걸린 최소 시간
		int targetFarm = 0; // 지을 농장의 개수
		while(true) {
			curTime = preFarmTime + farmCost/(2.0 + targetFarm*farmOutput) + targetAmount/(2.0 + ((targetFarm+1)*farmOutput));
			
			if(curTime >= minTime)
				break;
			
			preFarmTime += farmCost/(2.0 + targetFarm*farmOutput);
			minTime = curTime;
			targetFarm++;
		}

		cout.setf(ios::fixed);
		cout.precision(7);
		cout << "Case #" << caseNum << ": " << minTime << endl;
	}
	return 0;
}