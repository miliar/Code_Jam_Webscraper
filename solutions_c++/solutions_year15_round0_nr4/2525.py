#include <bits/stdc++.h>

using namespace std;

char winner[2][20] = {"RICHARD", "GABRIEL"};

int main() {
	int T, tc=1, X, R, C, res;
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d %d", &X, &R, &C);
		if ((R*C) % X != 0) {
			res = 0;
		} else if (X <= 2) {
			res = 1;
		} else if (X >= 7 || R == 1 || C == 1 || (R < X && C < X)) {
			res = 0;
		} else if (X == 3) {
			res = 1;
		} else if (R <= 2 || C <= 2) {
			res = 0;
		} else if (X == 4) {
			res = 1;
		} else if (X == 5) {
			if ((R == 5 && C == 3) || (C == 5 && R == 3)) res = 0;
			else res = 1;
		} else if (X == 6) {
			if (R <= 4 || C <= 4) res = 0;
			else res = 1;
		}
		printf("Case #%d: %s\n", tc++, winner[res]);
	}
	return 0;
}