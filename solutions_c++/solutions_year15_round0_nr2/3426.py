#include <cstdio>
#include <algorithm>
using std::min;
using std::max;

int solve() {
	int n, p[1111] = {0}, max_v = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; ++ i) {
		int v;
		scanf("%d", &v);
		p[v]++;
		if (v > max_v) max_v = v;
	}
	int result = max_v;
	for (int i = 1; i < max_v && result == max_v; ++ i) {
		for (int k = 1; k <= i && result == max_v; ++ k) {
			int sum = k;
			for (int j = k + 1; j <= max_v; ++ j)
				sum += p[j] * ((j - 1) / k);
			if (sum <= i) result = i;
//			printf("%d %d %d\n", i, k, sum);
		}
	}
	return result;
}

int main(void) {
	int tests_count;
	scanf("%d", &tests_count);
	for (int test = 1; test <= tests_count; ++ test) {
		printf("Case #%d: %d\n", test, solve());
		fflush(stdout);
	}
	return 0;
}
