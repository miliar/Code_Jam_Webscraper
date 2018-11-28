#include <iostream>
#include <fstream>
using namespace std;

const int N = 4;

int main()
{
	int attemps;
	cin >> attemps;

	for (int attemp = 1; attemp < attemps + 1; attemp++) {
		double C, F, X;
		cin >> C >> F >> X;

		int fermsTotal;
		int maxFerms = X / C + 1;
		double k = 2.0;
		double  bestTime = X / k;

		for (fermsTotal = 0; fermsTotal <= maxFerms; fermsTotal++) {
			double time = 0.0;
			double ti;
			k = 2.0;

			for (int i = 1; i <= fermsTotal; i++) {
				ti = C / k;
				time += ti;
				k += F;
			}
			time += X / k;
			if (time < bestTime)
				bestTime = time;
		}

		//printf("Case #%d: %.7lg\n", attemp, bestTime);
		cout.precision(7);
		cout << fixed;
		cout << "Case #" << attemp << ": " << bestTime << endl;
	}

}