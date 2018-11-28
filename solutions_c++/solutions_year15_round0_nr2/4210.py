#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
int test, n, a[1111];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &test);
	int ncase = 0;
	while (test --) {
		scanf("%d", &n);
		for (int i = 0; i < n; i ++) {
			scanf("%d", &a[i]);
		}
		int ans = 1000000000;
		for (int k = 1; k <= 1000; k ++) {
			int temp = k;
			for (int i = 0; i < n; i ++) {
				temp += (a[i] - 1) / k;
			}
			ans = min(ans, temp);
		}
		printf("Case #%d: %d\n", ++ ncase, ans);
	}
	return 0;
}

