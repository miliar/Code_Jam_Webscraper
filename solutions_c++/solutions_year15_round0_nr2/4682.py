#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
int a[105];
int main() {
	int t, cas = 0;
	int n, i, j, k;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d", &n);
		int ans = 1005;
		for (i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
		}

		for (i = 1; i < 10; ++i) {
			k = 0;
			for (j = 0; j < n; ++j) {
				k += (a[j] + i - 1) / i - 1;
			}
			ans = min(ans, i + k);
		}
		printf("Case #%d: %d\n", cas, ans);
	}
}
