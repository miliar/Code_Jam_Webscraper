#include <bits/stdc++.h>
using namespace std;
int T, R, C;
char g[150][150];
bool noLeft[150][150], noRight[150][150], noUp[150][150], noDown[150][150];
int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; ++i) scanf("%s", g[i]);
		memset(noLeft, 0, sizeof noLeft);
		memset(noRight, 0, sizeof noRight);
		memset(noUp, 0, sizeof noUp);
		memset(noDown, 0, sizeof noDown);
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				if (g[i][j] == '.') continue;
				noLeft[i][j] = 1;
				break;
			}
			for (int j = C-1; j >= 0; --j) {
				if (g[i][j] == '.') continue;
				noRight[i][j] = 1;
				break;
			}
		}
		for (int j = 0; j < C; ++j) {
			for (int i = 0; i < R; ++i) {
				if (g[i][j] == '.') continue;
				noUp[i][j] = 1;
				break;
			}
			for (int i = R-1; i >= 0; --i) {
				if (g[i][j] == '.') continue;
				noDown[i][j] = 1;
				break;
			}
		}
		bool imposs = 0; int ans = 0;
		for (int i = 0; i < R && !imposs; ++i) {
			for (int j = 0; j < C && !imposs; ++j) {
				if (g[i][j] == '.') continue;
				if (noUp[i][j] && noDown[i][j] && noLeft[i][j] && noRight[i][j]) imposs = 1;
				if (noUp[i][j] && g[i][j] == '^') ++ans;
				else if (noDown[i][j] && g[i][j] == 'v') ++ans;
				else if (noLeft[i][j] && g[i][j] == '<') ++ans;
				else if (noRight[i][j] && g[i][j] == '>') ++ans;
				else continue;
			}
		}
		printf("Case #%d: ", TC);
		if (imposs) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
}
