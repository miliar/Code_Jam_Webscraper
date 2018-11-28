#include <stdio.h>

#define FOR(a, b) for(a=1;a<=b;a++)

int main()
{
	freopen("B-large.in", "r", stdin);

	freopen("B-large.txt", "w", stdout);

	unsigned long long tc, i, j, k, n, p;

	unsigned long long a, b, m;

	scanf("%llu", &tc);

	FOR(i, tc) {

		scanf("%llu %llu %llu", &a, &b, &k);

		m = 0;

		for (j = k; j < b; j++) {

			for (p = k; p < a; p++) {
				if ((j & p) >= k)
					m++;
			}
		}

		printf("Case #%llu: %llu\n", i, (a*b) - m);
	}


	return 0;
}