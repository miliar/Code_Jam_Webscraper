#include <cstdio>
#include <climits>
#include <iostream>
#define MAXN 1000
using namespace std;
int a[MAXN+5];
int main() {
	int T, n, maxmax, ans, tmpans;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &n);
		maxmax = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			maxmax = max(maxmax, a[i]);
		}
		ans = INT_MAX;
		for (int target = 1; target <= maxmax; target++) {
			tmpans = 0;
			for (int i = 0; i < n; i++) {
				if (a[i] <= target) {
					continue;
				}
				tmpans += a[i]/target+((a[i]%target == 0) ? 0 : 1)-1;
			}
			ans = min(tmpans+target, ans);
		}
		printf("Case #%d: %d\n", t, ans);
	}
}
