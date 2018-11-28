
#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

void solve() {
	static char s[1033];
	int x;
	scanf("%d", &x);
	scanf("%s", s);

	int ans = 0, presum = s[0] - '0';
	for (int i = 1; i <= x; ++i) {
		int y = s[i] - '0';
		if (y != 0 && presum < i) {
			ans += i - presum;
			presum += i - presum + y;
		}
		else presum += y;
	}
	printf("%d\n", ans);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++ Case) {
		printf("Case #%d: ", Case);
		solve();
	}
	return 0;
}
