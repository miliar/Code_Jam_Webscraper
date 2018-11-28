#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>
using namespace std;

int n[105], a[105][1005];
int ans[105];
int f[1005];
int tmp[1005];
set<int> num;

int main() {
	int T, cases = 0;
	scanf("%d", &T);	
	for (int i = 0; i < T; ++i) {
		int x;
		scanf("%d", &n[i]);
		ans[i] = 0;
		for (int j = 0; j < n[i]; ++j) {
			scanf("%d", &a[i][j]);
			ans[i] = max(ans[i], a[i][j]);
		}
	}
	for (int i = 1; i <= 1000; ++i) {
		for (int j = 0; j < T; ++j) {
			tmp[j] = 0;
			for (int k = 0; k < n[j]; ++k) {
				tmp[j] += (a[j][k] - 1) / i;
			}
			ans[j] = min(ans[j], tmp[j] + i);
		}
	}
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: %d\n", ++cases, ans[i]);
	}
	return 0;
}
