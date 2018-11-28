
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

void solve() {
	static const int MAXN = 1033;
	static int D, A[MAXN];
	int ans = 1000;
	scanf("%d", &D);
	for (int i = 1; i <= D; ++i) scanf("%d", A + i);

	for (int h = 1; h <= 1000; ++h) {
		int res = h;
		for (int i = 1; i <= D; ++i)
			if (A[i] != 0)
				res += (A[i] + h - 1) / h - 1;
		ans = min(ans, res);
	}
	printf("%d\n", ans);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
