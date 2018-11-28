#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int cases;
	scanf("%d", &cases);

	for (int z = 0; z < cases; z++) {
		double C, F, X;
		cin >> C >> F >> X;

		int farms = 0;
		double totalTime = 0;

		//              [winTime] = X / (F * farms + 2)
		//       [timeToNextFarm] = C / (F * farms + 2)
		// [winTimeWithExtraFarm] = X / (F * (farms+1) + 2)

		// while [winTime] is greater than [timeToNextFarm] + [winTimeWithExtraFarm]
		while ((X / (F * farms + 2)) > ((C / (F * farms + 2)) + (X / (F * (farms+1) + 2)))) {
			// totalTime += [timeToNextFarm], farms++
			totalTime += C / (F * farms + 2);
			farms++;
		}

		// totalTime += [winTime]
		totalTime += X / (F * farms + 2);

		cout << "Case #" << (z+1) << ": " << setprecision(10) << totalTime << endl;
		
	}

	return 0;
}