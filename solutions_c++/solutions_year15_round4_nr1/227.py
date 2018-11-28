#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <utility>
#include <iostream>
#include <cmath>
#include <ctime>
#include <iomanip>
#include <set>
#include <vector>
#include <queue>
#include <map>
using namespace std;

const int xx[4] = {-1, 0, 1, 0};
const int yy[4] = {0, 1, 0, -1};
int tst, n, m;
char mp[200][200];
bool in(int x, int y) { return x>=1&&x<=n&&y>=1&&y<=m;}
int main()  {
	scanf("%d", &tst);
	for (int t = 1; t <= tst; t ++)  {
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i ++)  
			for (int j = 1; j <= m; j ++)  {
				char c = getchar();
				while (c != '^' && c != '.' && c != '>' && c != '<' && c != 'v')  c = getchar();
				mp[i][j] = c;
			}
		int ans = 0;
		bool no = false;
		for (int i = 1; i <= n; i ++)
			for (int j = 1; j <= m; j ++)  {
				bool bad = false;
				int ok = 0;
				if (mp[i][j] == '.') continue;
				for (int d = 0; d < 4; d ++)  {
					int x = i, y = j;
					x += xx[d], y += yy[d];
					while (in(x, y) && mp[x][y] == '.') {
						x += xx[d], y += yy[d];
					}
					if (!in(x, y))  { //bad
						if (d == 0 && mp[i][j] == '^') bad = true;
						if (d == 1 && mp[i][j] == '>') bad = true;
						if (d == 2 && mp[i][j] == 'v')  bad = true;
						if (d == 3 && mp[i][j] == '<')  bad = true;
					}else { //find arrow
						ok ++;
					}
				}
				if (!bad) continue;
				if (ok == 0)  no = true;
				ans ++;
			}
			if (no) printf("Case #%d: IMPOSSIBLE\n", t);
			else printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}