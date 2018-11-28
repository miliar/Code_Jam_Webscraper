#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;

int n, m;
int fx[4][2];
map<char, int> mm;
char a[110][110];

void init() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) scanf("%s", a[i]);
}

bool cal(int x, int y, int z) {
	x += fx[z][0]; y += fx[z][1];
	while ((x >= 0) && (x < n) && (y >= 0) && (y < m)) {
		if (a[x][y] != '.') return true;
		x += fx[z][0]; y += fx[z][1];
	}
	return false;
}

void solve() {
	int k, ans = 0;
	bool p;
	for (int i = 0; i < n; i++) 
		for (int j = 0; j < m; j++) {
			if (a[i][j] == '.') continue;
			k = mm[a[i][j]];
			if (cal(i, j, k)) continue;
			p = false;
			for (int l = 0; l < 4; l++) {
				if (!cal(i, j, l)) continue;
				p = true;	
				break;
			}
			if (!p) {
				puts("IMPOSSIBLE");
				return;
			}
			++ans;
		}
	printf("%d\n", ans);
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	mm['^'] = 0; mm['>'] = 1; mm['v'] = 2; mm['<'] = 3;
	fx[0][0] = -1; fx[0][1] = 0;
	fx[1][0] = 0; fx[1][1] = 1;
	fx[2][0] = 1; fx[2][1] = 0;
	fx[3][0] = 0; fx[3][1] = -1;
	int cas; scanf("%d", &cas);
	for (int ca = 1; ca <= cas; ca++) {
		init();
		printf("Case #%d: ", ca);
		solve();
	}
}
