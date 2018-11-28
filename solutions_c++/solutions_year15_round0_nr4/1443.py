#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int T;
int X, R, C;

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		scanf("%d%d%d", &X, &R, &C);
		printf("Case #%d: ", test);

		if (X == 1) puts("GABRIEL");
		else if (X == 2) {
			if (R * C % 2 == 0) puts("GABRIEL");
			else puts("RICHARD");
		} else if (X == 3) {
			if (R * C % 3 == 0 && R >= 2 && C >= 2 && R * C >= 6) puts("GABRIEL");
			else puts("RICHARD");
		} else if (X == 4) {
			if (R * C % 4 == 0 && R * C >= 12 && R >= 3 && C >= 3) puts("GABRIEL");
			else puts("RICHARD");
		}

	}
	return 0;
}
