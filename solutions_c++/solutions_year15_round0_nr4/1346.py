#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

bool f(int X, int R, int C) {
	if (R > C) swap(R, C);
	if ((R*C) % X) return true;
	if (X > C) return true;
	if (X <= 2) return false;
	if (R == 1) return true;
	if (X <= 3) return false;
	if (R == 2) return true;
	return false;
}

int main() {
	int T, X, R, C;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d%d%d", &X, &R, &C);
		cout << "Case #" << tc << ": " << (f(X, R, C) ? "RICHARD" : "GABRIEL") << endl;
	}
	return 0;
}