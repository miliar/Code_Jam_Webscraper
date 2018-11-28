#include <bits/stdc++.h>

using namespace std;
const int N = 1005;
int t, n;
int P[N];
int main() {
	scanf("%d", &t);
	for(int test = 1; test <= t; test++) {
		printf("Case #%d: ", test);
		scanf("%d", &n);
		int mx = 0;
		for(int i = 1; i <= n; i++) {
			scanf("%d", &P[i]);
			mx = max(mx, P[i]);
		}
		int ans = mx;
		for(int i = 1; i <= mx; i++) {
			int steps = 0;
			for(int j = 1; j <= n; j++) {
				steps += (P[j] + i - 1) / i - 1;
			}
			ans = min(ans, steps + i);
		}
		printf("%d\n", ans);
	}
	return 0;
}