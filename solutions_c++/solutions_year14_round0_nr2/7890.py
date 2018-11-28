#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		double C, F, X;
		cin >> C >> F >> X;
		double time = 0.0;
		double c = 0.0;
		int f = 0;
		while (c < X) {
			double r = X - C;
			if (r > 0) {
				if (X / (2 + f * F) > X / (2 + (f+1) * F) + C / (2 + f * F)) {
					time += C / (2 + f * F);
					f++;
				}
				else {
					time += X / (2 + f * F);
					break;
				}
			}
			else {
				time += X / 2;
				break;
			}
		}
		cout << fixed;
		cout.precision(7);
		cout << "Case #" << t << ": " << time << endl;
	}
	return 0;
}
