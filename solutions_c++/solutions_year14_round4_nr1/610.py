#include <cstdio>
#include <algorithm>
using std::sort;

const int N = 11111;
int n, x, s[N];

int solve() {
	bool used[N] = {0};
	int cnt = 0;
	sort(s + 1, s + 1 + n);
	for (int i = n; i > 0; -- i) {
		if (used[i]) continue;
		for (int j = 1; j < i; ++ j) {
			if (used[j]) continue;
			if (s[i] + s[j] <= x) {
				used[j] = true;
				break;
			}
		}
		used[i] = true;
		++ cnt;
	}
	return cnt;
}

int main(void) {
	int test_count;
	scanf("%d", &test_count);
	for (int test = 1; test <= test_count; ++ test) {
		scanf("%d%d", &n, &x);
		for (int i = 1; i <= n; ++ i) {
			scanf("%d", &s[i]);
		}
		printf("Case #%d: %d\n", test, solve());
	}
	return 0;
}
