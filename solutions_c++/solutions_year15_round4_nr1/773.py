#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int r, c, ans;
char b[105][105];
char d[] = "^v<>";
bool check(int i, int j) {
	bool flag[4];
	memset(flag, false, sizeof flag);
	for (int k = 0; k < i; ++k)
		if (b[k][j] != '.') flag[0] = true;
	for (int k = i + 1; k < r; ++k)
		if (b[k][j] != '.') flag[1] = true;
	for (int k = 0; k < j; ++k)
		if (b[i][k] != '.') flag[2] = true;
	for (int k = j + 1; k < c; ++k)
		if (b[i][k] != '.') flag[3] = true;
	int cnt = 0;
	for (int k = 0; k < 4; ++k) {
		if (d[k] == b[i][j] && flag[k])
			return true;
		if (flag[k]) cnt++;
	}
	if (cnt) ans++;
	return cnt > 0;
}
void solve() {
	ans = 0;
	scanf("%d%d", &r, &c);
	for (int i = 0; i < r; ++i) scanf("%s", b[i]);
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			if (b[i][j] != '.') {
				if (!check(i, j)) {
					printf("IMPOSSIBLE\n");
					return;
				}
			}
		}
	}
	printf("%d\n", ans);
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; ++_) {
		printf("Case #%d: ", _);
		solve();
	}
	return 0;
}
