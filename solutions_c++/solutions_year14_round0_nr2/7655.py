#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		double c, f, x;
		double timeSpent = 0;
		double cpr = 2;
		cin >> c >> f >> x;
		while (1) {
			if (x/cpr < c/cpr + x/(cpr + f)) {
				timeSpent += x/cpr;
				break;
			}
			else {
				timeSpent += c/cpr;
				cpr += f;
			}
		}
		cout << fixed << setprecision(7) << timeSpent << endl;
	}
	return 0;
}