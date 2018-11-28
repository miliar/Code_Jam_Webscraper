#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B1.out", "w", stdout);
	int n, x, d, cas = 1;
	scanf("%d", &n);
	for (int i = 0; i < n; i ++ ) {
		scanf("%d", &d);
		std::vector<int> q;
		for (int j = 0; j < d; j ++ ) {
			scanf("%d", &x);
			q.push_back(x);
		}
		int ans = 1000;
		for (int p = 1; p < 1000; p ++ ) {
			int c = p;
			for (int j = 0; j < q.size(); j ++ )
				c = c + (q[j] - 1) / p;
			ans = std::min(ans, c);
		}
		printf("Case #%d: %d\n", cas ++ , ans);
	}
	return 0;
}