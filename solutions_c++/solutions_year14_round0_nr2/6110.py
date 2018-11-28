#include <cfloat>
#include <iostream>
#include <cstdio>

int main(int argc, char** argv) {
	using namespace std;

	int numCases;
	cin >> numCases;

	for (int caseNum = 1; caseNum <= numCases; caseNum++) {
		double C,F,X;
		scanf("%lf %lf %lf", &C, &F, &X);

		cout << "Case #" << caseNum << ": ";

		double speed = 2.0;
		double sufferingTime = 0.0;
		double lowestTimeIfWait = DBL_MAX;
		while (1) {
			double timeIfWait = sufferingTime + X / speed;
			double timeToBuy = sufferingTime + C / speed;

			if (timeIfWait < lowestTimeIfWait) {
				lowestTimeIfWait = timeIfWait;
			}
			if (lowestTimeIfWait < sufferingTime) {
				sufferingTime = lowestTimeIfWait;
				break;
			} else {
				sufferingTime = timeToBuy;
				speed += F;
			}
		}

		printf("%.7f\n", sufferingTime);
	}

	return 0;
}
