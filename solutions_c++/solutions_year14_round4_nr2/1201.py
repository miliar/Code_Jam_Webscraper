#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
inline int abs(int x) {
	return x < 0 ? -x : x;
}
int a[1024], t[1024], tmp[1024], ind[1024];
int dp[1010][1010];
bool cmp(int i, int j) {
	return a[i] < a[j];
}
int inv(int n, int* a) {
	int left = n >> 1, r = n - left, i, j;
	int ret = (r > 1 ? (inv(left, a) + inv(r, a + left)) : 0);
	for (i = j = 0; i <= left; tmp[i + j] = a[i], i++) {
		for (ret += j; j < r && (i == left || !(a[i] < a[left + j])); tmp[i + j] = a[left + j], j++);
	}
	memcpy(a, tmp, sizeof(int) * n);
	return ret;
}
int main() {
	int testnum, n, mai, ans, tans, cnt, l, r, c;
	scanf("%d", &testnum);
	for (int test = 1; test <= testnum; test++) {
		scanf("%d", &n);
		mai = 0;
		for (int i = 0;i < n;i++) {
			scanf("%d", &a[i]);
			ind[i] = i;
			if (a[i] > a[mai])
				mai = i;
			for (int j = 0;j < n;j++)
				dp[i][j] = 1111111111;
		}
		sort(ind, ind + n, cmp);
		dp[0][0] = 0;
		ans = 1111111111;
		for (int i = 0;i <= n;i++) {
			for (int j = 0;i + j <= n;j++) {
				if (i + j == 0) continue;
				c = i + j - 1;
				l = r = 0;
				for (int k = ind[c];k >= 0;k--) l += a[k] > a[ind[c]];
				for (int k = ind[c];k < n;k++) r += a[k] > a[ind[c]];
				if (i) dp[i][j] = min(dp[i][j], dp[i - 1][j] + l);
				if (j) dp[i][j] = min(dp[i][j], dp[i][j - 1] + r);
				if (i + j == n && dp[i][j] < ans)
					ans = dp[i][j];
			}
		}
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}

