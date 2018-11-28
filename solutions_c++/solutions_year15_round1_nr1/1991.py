#include <bits/stdc++.h>

using namespace std;

const int MOD = 100007;

int a[1010];

int main()
{
	int T, n;
	cin >> T;
	for (int cas = 1; cas <= T; cas++) {
		cin >> n;
		for (int i = 0; i < n; i++) cin >> a[i];
		int c0 = 0, c1 = 0, delta = 0;
		for (int i = 1; i < n; i++) {
			if (a[i - 1] > a[i]) {
				c0 += a[i - 1] - a[i];
				delta = max(delta, a[i - 1] - a[i]);
			}
		}
		for (int i = 0; i < n - 1; i++) {
			c1 += min(a[i], delta);
		}
		printf("Case #%d: %d %d\n", cas, c0, c1);
	}
	return 0;
}
