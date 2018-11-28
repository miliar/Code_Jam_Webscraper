#include <cstdio>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int n;
int a[1005];

void solve(){
	scanf("%d", &n);
	int ans = 0, ans2 = 0, maxV = -1;
	for (int i = 0; i < n; i++) scanf("%d", &a[i]);
	for (int i = 0; i < n - 1; i++)
		if (a[i] > a[i + 1]) ans += a[i] - a[i + 1];
	for (int i = 0; i < n - 1; i++) maxV = max(maxV, a[i] - a[i + 1]);
	for (int i = 0; i < n - 1; i++) ans2 += min(maxV, a[i]);
	printf("%d %d\n", ans, ans2);
}

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}
