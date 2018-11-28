#include <bits/stdc++.h>

using namespace std;
const int N = 1005;
int t, n;
char s[N];
int main() {
	scanf("%d", &t);
	for(int test = 1; test <= t; test++) {
		printf("Case #%d: ", test);
		scanf("%d %s", &n, &s[0]);
		int ans = 0;
		int cnt = 0;
		for(int i = 0; i <= n; i++) {
			ans = max(ans, i - cnt);
			cnt += s[i] - 48;
		}
		printf("%d\n", ans);
	}
	return 0;
}