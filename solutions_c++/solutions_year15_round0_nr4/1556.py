#include <stdio.h>
#include <string.h>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <map>
#include <bitset>

#define REP(a, b) for (int a = 0; a < b; ++a)
#define FORU(a, b, c) for (int a = b; a <= c; ++a)
#define FORD(a, b, c) for (int a = b; a >= c --a)
#define pb push_back
#define mp make_pair
using namespace std;

int main() {
	int T, X, R, C;

	scanf("%d", &T);

	FORU(tc, 1, T) {
		scanf("%d %d %d", &X, &R, &C);

		if (X == 1) {
			printf("Case #%d: GABRIEL\n", tc);
			continue;
		}

		int mini = min(R, C), maks = max(R, C);

		printf("Case #%d: ", tc);

		if (mini >= (X - 1) && maks >= X && ((R * C) % X == 0)) {
			puts("GABRIEL");
		}
		else {
			puts("RICHARD");
		}
	}

	return 0;
}
