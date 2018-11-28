#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <ctime>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;

int go[1000], T, n, m, tx[4] = {-1, 0, 0, 1}, ty[4] = {0, 1, -1, 0};
char a[110][110];

bool in(int x, int y) {
	return 1 <= x && x <= n && 1 <= y && y <= m;
}

int main() {
	scanf("%d", &T);
	go['^'] = 0;
	go['>'] = 1;
	go['<'] = 2;
	go['v'] = 3;
	for (int xx = 1; xx <= T; xx++) {
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++)
			scanf("%s", a[i] + 1);
		int ans = 0;
		bool ok = true;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				if (a[i][j] != '.') {
					int t = go[a[i][j]], x = i + tx[t], y = j + ty[t];
					while (in(x, y)) {
						if (a[x][y] != '.') break;
						x += tx[t];
						y += ty[t];
					}
					if (!in(x, y)) ans++;
					bool f = false;
					for (int p = 1; p <= m; p++)
						if (p != j && a[i][p] != '.') f = true;
					for (int p = 1; p <= n; p++)
						if (p != i && a[p][j] != '.') f = true;
					if (!f) ok = false;
				}
		if (!ok) printf("Case #%d: IMPOSSIBLE\n", xx);
		else printf("Case #%d: %d\n", xx, ans);
	}
}
