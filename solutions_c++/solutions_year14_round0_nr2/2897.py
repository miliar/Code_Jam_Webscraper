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

		double curTime; // ���� ��ǥ���� �޼��ϴµ� �ɸ� �ð�
		double preFarmTime = 0.0; // ������ ������ �� ���µ� �ɸ� �ð�
		double minTime = targetAmount / 2.0; // ��ǥ���� �޼��ϴµ� �ɸ� �ּ� �ð�
		int targetFarm = 0; // ���� ������ ����
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