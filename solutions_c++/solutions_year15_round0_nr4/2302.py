#include <iostream>

using namespace std;
char RES[][100] = { "RICHARD", "GABRIEL" };
int main() {
	int X, R, C;
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> X >> R >> C;
		int ans = 0;
		if (X >= 7)
			ans = 0;
		else if (X >= 4) {
			if ((R == 4 && C == 4) || (R == 4 && C == 3)
					|| (R == 3 && C == 4)) {
				ans = 1;
			} else
				ans = 0;
		} else if (X == 1) {
			ans = 1;
		} else if (X == 2) {
			if (R * C % 2 == 0) {
				ans = 1;
			} else {
				ans = 0;
			}
		} else {
			if (R * C % 3) {
				ans = 0;
			} else if (R == 1 || C == 1)
				ans = 0;
			else {
				ans = 1;
			}
		}

		cout << "Case #" << t << ": " << RES[ans] << endl;
	}

}
