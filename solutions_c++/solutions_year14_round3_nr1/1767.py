#include <cstdio>

int main() {
	int n;
	scanf("%d", &n);

	for (int t = 1; t <= n; t++) {
		int P, Q;
		scanf("%d/%d", &P, &Q);

		double check2 = Q;
		while (check2 > 1) {
			check2 /= 2;
		}

		if (check2 < 1) {
			printf("Case #%d: impossible\n", t);
		} else {
			int i;
			for (i = 0; ; i++) {
				if (Q <= P) break;
				Q /= 2;
			}

			printf("Case #%d: %d\n", t, i);
		}

	}

	return 0;
}