#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int T, n, x, s[10005], ans;

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d%d", &n, &x);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &s[i]);
		}
		sort(s, s+n);
		ans = 0;
		for (int i = 0, j = n - 1; i <= j; ) {
			if (i == j) {
				ans++;
				break;
			}
			else if (s[i] + s[j] <= x) {
				ans++;
				++i;
				--j;
			}
			else {
				ans++;
				--j;
			}
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}