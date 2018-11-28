#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000 + 10;

int P[MAXN], N;

int main() {
	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; ++ cas) {
		int N; scanf("%d", &N);
		int m = 0;
		for (int i = 0; i < N; ++ i) {
			scanf("%d", P + i);
			m = max(m, P[i]);
		}
		int ret = m;
		for (int v = 1; v <= m; ++ v) {
			int r = 0;
			for (int i = 0; i < N; ++ i) if (P[i] > v) {
				r += P[i] / v + (P[i] % v != 0);
				-- r;
			}
			ret = min(ret, r + v);
		}
		printf("Case #%d: %d\n", cas, ret);
	}
	return 0;
}
