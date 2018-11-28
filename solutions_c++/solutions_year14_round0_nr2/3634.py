#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	cout << fixed << setprecision(7);

	int T;
	cin >> T;
	for (int cn = 1; cn <= T; ++cn) {
		double cps = 2.0;
		double time = 0.0;

		double C, F, X;
		cin >> C >> F >> X;

		double timeToX = X / cps;
		double timeToC = C / cps;
		double timeToXafterC = timeToC + X / (cps + F);

		while (timeToX > timeToXafterC) {
			// cojo c
			cps += F;
			time += timeToC;
			timeToX = X / cps;
			timeToC = C / cps;
			timeToXafterC = timeToC + X / (cps + F);
		}

		cout << "Case #" << cn << ": " << time + timeToX << endl;
	}
}