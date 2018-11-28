#include <cstdio>

long gcd(long a, long  b) {
	while (b != 0) {
		long t = b;
		b = a % b;
		a = t;
	}
	return a;
}

int main() {
	int n;
	scanf("%d", &n);

	for (int t = 1; t <= n; t++) {
		long P, Q;
		scanf("%ld/%ld", &P, &Q);
		long d = gcd(Q, P);
		P = P/d;
		Q = Q/d;
		double c = Q;
		while (c > 1) {
			c /= 2;
		}
		if (c < 1) {
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
