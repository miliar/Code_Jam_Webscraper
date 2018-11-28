#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
char s[N];
int main() {
	int n, T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		printf("Case #%d: ", tt);
		scanf("%d", &n);
		scanf("%s", s);
		int ans = 0, now = 0;
		for (int i = 0; i <= n; ++i) {
			int t = s[i] - '0';
			if (now < i)	ans += i - now;
			now = t + max(now, i);
		}
		printf("%d\n", ans);
	}
	return 0;
}
