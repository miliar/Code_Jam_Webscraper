#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int c[20], row1, row2, a, T, ans;

int main() {
#ifdef DEBUGj
	freopen("ex.in", "r", stdin);
	freopen("ex.out", "w", stdout);
#endif

	cin >> T;
	for (int iter = 0; iter < T; iter++) {
		ans = -1;
		cin >> row1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> a;
				if (row1 == i + 1) c[a] = iter + 1;
			}
		}

		cin >> row2;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> a;
				if ((row2 == i + 1) && (c[a] == iter + 1)) {
					if (ans == -1) ans = a;
					else ans = -2;
				}
			}
		}
		cout << "Case #" << iter + 1 << ": ";
		if (ans == -1) cout << "Volunteer cheated!" << endl;
		else if (ans == -2) cout << "Bad magician!" << endl;
		else cout << ans << endl;

	}
	return 0;
}