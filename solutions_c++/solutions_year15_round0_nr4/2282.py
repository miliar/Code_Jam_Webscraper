#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void init() {

}

unsigned X, R, C;

char* names[] = { "GABRIEL", "RICHARD" };

unsigned solve() {
	if (X == 1) {
		return 0;
	}

	if ((R * C) % X != 0) {
		return 1;
	}

	if (X == 2) {
		return 0;
	}

	if (X == 3) {
		return R == 1 || C == 1 ? 1 : 0;
	}
	
	return R + C >= 7 ? 0 : 1;
}

void solvecase() {
	cin >> X >> R >> C;
	unsigned result = solve();
	cout << names[result] << endl;
}

int N;
int main() {
	init();
	cin >> N;
	for (int t = 1; t <= N; ++t) {
		cout << "Case #" << t << ": ";
		solvecase();
	}

	return 0;
}