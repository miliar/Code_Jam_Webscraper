#include <cstdio>
#include <algorithm>

using std::min;

const int N = 1111;
int n, v[N];

int solve() {
	int ret = 0;
	for (int i = 0; i < n; ++ i) {
		int p = 0, q = 0;
		for (int j = 0; j <= i; ++ j) {
			if (v[i] < v[j]) ++ p;
		}
		for (int j = i; j < n; ++ j) {
			if (v[i] < v[j]) ++ q;
		}
		ret += min(p, q);
	}

	return ret;
}

int main(void) {
	int test_count;
	scanf("%d", &test_count);
	for (int test = 1; test <= test_count; ++ test) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++ i) {
			scanf("%d", &v[i]);
		}
		printf("Case #%d: %d\n", test, solve());
	}
	return 0;
}
