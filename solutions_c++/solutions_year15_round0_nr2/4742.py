#include <cstdio>

int T, D, P[1234];

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &D);
		for (int i = 0; i < D; i++)
			scanf("%d", &P[i]);
		int res = 1000;
		// eat time
		for (int a = 1; a <= 1000; a++) {
			int b = 0; // special time
			for (int i = 0; i < D; i++)
				b += (P[i] - 1) / a;
			if (res > a+b) res = a+b;
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
