#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <queue>
#include <algorithm>
using namespace std;

int t, n;
double a[1005], b[1005];

int main() {
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	scanf("%d", &t);
	int cases = 0;
	while(t--) {
		scanf("%d", &n);
		for(int i = 1; i <= n; i++) {
			scanf("%lf", a+i);
		}
		for(int i = 1; i <= n; i++) {
			scanf("%lf", b+i);
		}
		sort(a + 1, a + 1 + n, greater<double>());
		sort(b + 1, b + 1 + n, greater<double>());
		int i = 1, j = 1;
		int ans1 = 0, ans2 = 0;
		while(i <= n && j <= n) {
			if(a[i] >= b[j]) {
				i ++;
				ans1 ++;
			} else {
				i ++;
				j ++;
			}
		}
		i = 1, j = 1;
		sort(a + 1, a + 1 + n);
		sort(b + 1, b + 1 + n);
		while(i <= n && j <= n) {
			if(a[i] <= b[j]) {
				i++;
			} else {
				i ++;
				j ++;
				ans2 ++;
			}
		}
		printf("Case #%d: %d %d\n", ++cases, ans2, ans1);
	}
	return 0;
}

