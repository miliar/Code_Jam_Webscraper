#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

typedef unsigned int uint128_t __attribute__((mode(TI)));

uint128_t gcd (uint128_t a, uint128_t b) {
	while (b) {
		a %= b;
		std::swap(a, b);
	}
	return a;
}

uint32_t bitcnt(uint128_t x) {
	uint32_t res = 0;
	while (x) {
		res += x & 1;
		x >>= 1;
	}
	return res;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int test = 0; test < T; ++test) {
		fprintf(stderr, "Case #%d:\n", test + 1);
		int N, X;
		scanf("%d%d", &N, &X);
		std::vector<int> v(N);
		std::vector<int> used(N, 0);
		for (int i = 0; i < N; ++i)
			scanf("%d", &v[i]);
		sort(v.rbegin(), v.rend());
		int ans = 0;
		for (int i = 0; i < N; ++i) {
			if (used[i])
				continue;
			for (int j = i + 1; j < N; ++j)
				if (!used[j] && (v[i] + v[j] <= X)) {
					used[j] = 1;
					break;
				}
			used[i] = 1;
			++ans;
		}

		printf("Case #%d: ", test + 1);
		printf("%d\n", ans);
	}

	return 0;
}