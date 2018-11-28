#include <cstdio>
#include <utility>

using namespace std;

const int MAXN = 100 + 5;
const char dir[] = {'^', '>', 'v', '<'};

int n, m;
bool vis[MAXN][MAXN];
char cell[MAXN][MAXN];

pair<int, int> check(int x, int y, char dir) {
	switch (dir) {
		case '^':
			x--;
			break;
		case '>':
			y++;
			break;
		case 'v':
			x++;
			break;
		case '<':
			y--;
			break;
	}
	if (x < 1 || x > n || y < 1 || y > m)
		return make_pair(-1, -1);
	if (cell[x][y] != '.')
		return make_pair(x, y);
	return check(x, y, dir);
}

void go(int x, int y, int &ans) {
       vis[x][y] = true;
       pair<int, int> t = check(x, y, cell[x][y]);
       if (t.first > -1 && t.second > -1) {
	       if (!vis[t.first][t.second])
		       go(t.first, t.second, ans);
	       return;
       }
       for (int i = 0; i < 4; i++) {
	       pair<int, int> t = check(x, y, dir[i]);
	       if (t.first > -1 && t.second > -1) {
		       cell[x][y] = dir[i];
		       ans++;
		       go(t.first, t.second, ans);
		       return;
	       }
       }
       ans = -1;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T, kase = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++) {
				char &ch = cell[i][j];;
				for (ch = getchar(); ch != '.' && ch != '^' && ch != '>' && ch != 'v' && ch != '<'; ch = getchar());
				vis[i][j] = false;
			}
		int ans = 0;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				if (cell[i][j] != '.' && !vis[i][j])
					go(i, j, ans);
		if (ans > -1)
			printf("Case #%d: %d\n", ++kase, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", ++kase);
	}
	return 0;
}
