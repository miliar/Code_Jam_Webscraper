#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <algorithm>

bool Func(int X, int R, int C)
{
	if (R < C) {
		std::swap(R, C);
	}
	if (X >= 7 || R*C%X != 0 || R < X || C < (X+1)/2){
		return false;
	}
	if (C > (X+1)/2) {
		return true;
	}
	if (X == 4) {
		if (C <= 2) {
			return false;
		}
	} else if (X == 5) {
		if (R <= 5 && C <= 3) {
			return false;
		}
	} else if (X == 6) {
		if (C <= 3) {
			return false;
		}
	}

	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int X, R, C;
		scanf("%d %d %d", &X, &R, &C);
		const char* res = "RICHARD";
		if (Func(X, R, C)) {
			res = "GABRIEL";
		}
		printf("Case #%d: %s\n", t, res);
	}
}
