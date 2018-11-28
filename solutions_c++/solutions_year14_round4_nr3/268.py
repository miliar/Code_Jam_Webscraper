#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

const int MAX_N = 2020;
struct Node {
	int x0, y0, x1, y1;
} b[MAX_N];
int dp[MAX_N][MAX_N << 1];
int W, H, B;

int fx[4][2] = {
	{0, -1}, {-1, 0}, {0, 1}, {1, 0}
};

bool ok(int x, int y) {
	return x >= 0 && x < W && y >= 0 && y < H;
}

int gao(int x, int y, int now) {
	dp[x][y] = 1;
	if (y == H - 1) {
		return 1;
	}
	for (int i = 0; i < 4; i++) {
		int k = (i + now) % 4;
		int tx = x + fx[k][0];
		int ty = y + fx[k][1];
		if (ok(tx, ty) && dp[tx][ty] == 0) {
			if (gao(tx, ty, (k + 3) % 4)) {
				return 1;
			}
		}
	}
	return 0;
}

int main() {
	int __size__ = 256 << 20;
	char *__p__ = (char*)malloc(__size__) + __size__;
	__asm__("movl %0, %%esp\n" :: "r"(__p__));
	int n_case = 0;
	scanf("%d", &n_case);
	for (int ca = 1; ca <= n_case; ca++) {
		int ans = 0;
		scanf("%d%d%d", &W, &H, &B);
		fill(dp[0], dp[W + 5], 0);
		for (int i = 0; i < B; i++) {
			scanf("%d%d%d%d", &b[i].x0, &b[i].y0, &b[i].x1, &b[i].y1);
			for (int j = b[i].x0; j <= b[i].x1; j++) {
				for (int k = b[i].y0; k <= b[i].y1; k++) {
					dp[j][k] = 1;
				}
			}
		}
		for (int i = 0; i < W; i++) {
			if (dp[i][0] == 0) {
				ans += gao(i, 0, 0);
			}
		}
		printf("Case #%d: %d\n", ca, ans);
	//	fprintf(stderr, "Case #%d: %d\n", ca, ans);
	}
	return 0;
}
