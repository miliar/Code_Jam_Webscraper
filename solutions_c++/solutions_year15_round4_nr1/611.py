#include <cstdio>
#include <cstring>

const int d[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
const int MAXN = 100 + 10;

int n, m;
char map[MAXN][MAXN];
bool a[MAXN][MAXN][5];

inline bool inRange(int x, int y){
	return 0 <= x && x < n && 0 <= y && y < m;
}

void check(int x, int y, int i){
	if (map[x][y] != 4)
		return;

	while (inRange(x += d[i][0], y += d[i][1]) && map[x][y] == 4);
	if (inRange(x, y))
		a[x][y][(i + 2) % 4] = true;
}

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		scanf("%d%d", &n, &m);
		for (int i=0;i<n;++i)
			scanf("%s", map[i]);

		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
				if (map[i][j] == '^')
					map[i][j] = 0;
				else if (map[i][j] == '>')
					map[i][j] = 1;
				else if (map[i][j] == 'v')
					map[i][j] = 2;
				else if (map[i][j] == '<')
					map[i][j] = 3;
				else
					map[i][j] = 4;

		memset(a, 0, sizeof(a));
		for (int i=0;i<n;++i){
			a[i][0][3] = a[i][m - 1][1] = true;
			check(i, 0, 1);
			check(i, m - 1, 3);
		}
		for (int j=0;j<m;++j){
			a[0][j][0] = a[n - 1][j][2] = true;
			check(0, j, 2);
			check(n - 1, j, 0);
		}

		bool imp = false;
		int ans = 0;
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
				if (map[i][j] < 4){
					if (a[i][j][0] && a[i][j][1] && a[i][j][2] && a[i][j][3])
						imp = true;
					ans += a[i][j][map[i][j]];
				}

		if (imp)
			printf("Case #%d: IMPOSSIBLE\n" ,casi);
		else
			printf("Case #%d: %d\n", casi, ans);
	}
	return 0;
}
