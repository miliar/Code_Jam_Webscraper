#include <bits/stdc++.h>
using namespace std;
int F[105][1005][205], P, Q, N, H[105], G[105];
int f(int p, int moves, int h) {
	if (p == N) return 0;
	if (h <= 0) return f(p + 1, moves, H[p + 1]);
	int &ret = F[p][moves][h];
	if (ret != -1) return ret;
	ret = f(p, moves + 1, h - Q);
	if (moves) ret = max(ret, f(p, moves - 1, h - P) + (h - P <= 0 ? G[p] : 0));
	return ret;
}
int main() {
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn) {
		scanf("%d%d%d", &P, &Q, &N);
		for (int i = 0; i < N; ++i) scanf("%d%d", &H[i], &G[i]);
		memset(F, -1, sizeof(F));
		int ans = f(0, 1, H[0]);
		printf("Case #%d: %d\n", cn, ans);
	}
}

