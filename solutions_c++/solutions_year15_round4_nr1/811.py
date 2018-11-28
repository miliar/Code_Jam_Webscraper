#include <bits/stdc++.h>
using namespace std;
const int maxn = 105;
string str[maxn];
int r, c, ans, fail;
bool vis[maxn][maxn];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
char u[4] = {'^', 'v', '<', '>'};
int dir(char x) {
	if(x == '^') return 0;
	if(x == 'v') return 1;
	if(x == '<') return 2;
	if(x == '>') return 3;
}
bool legal(int x, int y) {
	return x >= 0 && x < r && y >= 0 && y < c;
}
void Check(int x, int y) {
	int d = dir(str[x][y]);
	int p = x + dx[d], q = y + dy[d];
	while(legal(p, q) && str[p][q] == '.') {
		p = p + dx[d];
		q = q + dy[d];
	}
	if(legal(p, q)) return;
	ans++;
	for(int i = 0; i < 4; i++) {
		p = x + dx[i]; q = y + dy[i];
		while(legal(p, q) && str[p][q] == '.') {
			p = p + dx[i];
			q = q + dy[i];
		}
		if(legal(p, q)) {
			str[x][y] = u[i];	
			return;
		}
	}
	fail = 1;
}
int main() {
#ifdef youmu
	freopen("A-large.in", "r", stdin);
	freopen("A-large.ou", "w", stdout);
#endif
	int T, cases = 0;
	cin >> T;
	while(T--) {
		cin >> r >> c;
		for(int i = 0; i < r; i++) cin >> str[i];
		ans = 0;
		fail = 0;
		for(int i = 0; i < r && !fail; i++) {
			for(int j = 0; j < c && !fail; j++) {
				if(str[i][j] != '.') Check(i, j);
			}
		}
		printf("Case #%d: ", ++cases);
		if(fail) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ans);
		}
	}
	return 0;
}
