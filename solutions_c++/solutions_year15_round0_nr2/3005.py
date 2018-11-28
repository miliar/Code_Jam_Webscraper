#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;
int const N = 1e3 + 10;
int P[N];
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, d, p, ans, mx; 
	scanf("%d", &T);
	for (int _ = 1; _ <= T; _++) {
		scanf("%d", &d);
		ans = N;
		mx = 0;
		for (int i = 0; i < d; i++) {
			scanf("%d", P + i);
			mx = max(mx, P[i]);
		}
		for (int i = 1; i <= mx; i++) {
			int cnt = 0;
			for (int j = 0; j < d; j++)
				cnt += (P[j] - 1) / i;
			ans = min(ans, cnt + i);
		}
		printf("Case #%d: %d\n", _, ans);
	}
	return 0;
}