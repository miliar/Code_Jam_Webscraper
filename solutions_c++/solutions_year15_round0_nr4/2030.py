#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

void printResult(int i, int gabriel) {
	if (gabriel) {
		printf("Case #%d: GABRIEL\n", i);
	} else {
		printf("Case #%d: RICHARD\n", i);
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		int X, R, C;
		scanf("%d %d %d", &X, &R, &C);
		if (X == 1) {
			printResult(i, 1);
		} else if (X == 2) {
			printResult(i, (R * C) % 2 == 0);
		} else if (X == 3) {
			printResult(i, (R * C) % 3 == 0 && min(R, C) >= 2);
		} else if (X == 4) {
			printResult(i, min(R, C) >= 3 && max(R, C) == 4);
		} else if (X == 5) {

		} else if (X == 6) {

		} else if (X >= 7) {
			printResult(i, 0);
		}
	}
	return 0;
}