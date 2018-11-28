#include <iostream>
#include <cstdio>

const int MAXN = 1010;
char s[MAXN];

void solve() {
	int n;
	scanf("%d", &n);
	scanf("%s", s);
	int ans = 0;
	int cur = 0;
	for (int i = 0; i <= n; ++i) {
		if (cur < i) {
			int d = i - cur;
			cur += d;
			ans += d;
		}
		cur += s[i] - '0';
	}
	printf("%d\n", ans);
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int t = 1; t <= tt; ++t) {
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}