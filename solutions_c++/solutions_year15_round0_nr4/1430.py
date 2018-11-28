#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

#define FILE "D"

int main() {
	ios_base::sync_with_stdio(false);
	freopen(FILE ".in", "r", stdin);
	freopen(FILE ".out", "w", stdout);
	int T;
	cin >> T;
	for (int _ = 0; _ < T; ++_) {

		int X, R, C;
		cin >> X >> R >> C;

		bool f = true;
		if (X == 2) {
			if (R*C % 2 != 0) {
				f = false;
			}
		}
		if (X == 3) {
			if (R*C % 3 != 0) {
				f = false;
			}
			if (R <= 1 || C <= 1) {
				f = false;
			}
		}
		if (X == 4) {
			if (R*C % 4 != 0) {
				f = false;
			}
			if (R <= 2 || C <= 2) {
				f = false;
			}
		}
		/*
			Print answer
		 */
		cout << "Case #" << _+1 << ": ";
		if (f) {
			cout << "GABRIEL";
		} else {
			cout << "RICHARD";
		}
		cout << "\n";
	}
	return 0;
}