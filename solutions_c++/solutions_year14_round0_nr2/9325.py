#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int T, i, j, k;
	double C, F, X, cps, cookies, t;

	cin >> T;
	for (i = 0; i < T; i++) {
		t = cookies = 0;
		cps = 2;
		cin >> C >> F >> X;
		if (C > X || cps > X) {
			t = X/cps;
		} else {
			while (true) {
				if (X/cps < C/cps + X/(cps+F)) {
					t += X/cps;
					break; // done
				}
				
				t += C/cps;
				cps += F;
			}
		}
		cout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << t << "\n";
	}
	return 0;
}