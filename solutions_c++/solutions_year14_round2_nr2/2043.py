#include <cstdio>

#define FOR(x, b, e) for (int x = b; x <= (e); ++x)

int main() {
	int a, b, k, t, res;

	scanf("%d", &t);
	FOR(q, 1, t) {
		res = 0;

		scanf("%d %d %d", &a, &b, &k);
		FOR(i, 0, a-1) FOR(j, 0, b-1) {
			if ((i & j) < k) res++;
		}

		printf("Case #%d: %d\n", q, res);
	}

	return 0;
}
