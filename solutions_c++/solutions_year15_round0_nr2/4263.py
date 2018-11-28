#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
int a[N];
int main() {
	int n, T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		printf("Case #%d: ", tt);
		scanf("%d", &n);
		int mx = 0;
		for (int i = 1; i <= n; ++i)	scanf("%d", &a[i]), mx = max(mx, a[i]);
		int ans = N;
		for (int i = 1; i <= mx; ++i) {
			int t = 0;
			for (int j = 1; j <= n; ++j) {
				t += a[j] / i;
				if (a[j] % i == 0)	--t;
			}
			ans = min(ans, t + i);
		}
		printf("%d\n", ans);
	}
	return 0;
}
