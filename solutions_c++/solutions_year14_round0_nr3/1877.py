# include <cstdio>
# include <cstring>

int R, C, M;
int tot;
int c[7][7];

// special : M+1==R*C
bool vis[7][7];
const int d[][2] = {
	{-1,-1}, {-1,0}, {-1,1},
	{0, -1},         {0,1},
	{1,-1,}, {1, 0}, {1,1}
};
bool ok(int x, int y)
{
    if (1<=x&&x<=R && 1<=y&&y<=C) return true;
    return false;
}
void dfs(int x, int y)
{
	++tot;
	vis[x][y] = true;
	if (c[x][y]!=0) return ;
	for (int i = 0; i < 8; ++i) {
		int nx = x + d[i][0];
		int ny = y + d[i][1];
		if ( ok(nx,ny) && !vis[nx][ny] ) {
			if (c[nx][ny] == -1) printf("--------------------------err! %d %d %d\n", R, C, M);
			dfs(nx, ny);
		}
	}
}
bool check(int S)
{
	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) {
			if ( (S>>(i*C+j)) & 0x1 ) {
				c[i+1][j+1] = -1;
			} else {
				c[i+1][j+1] = 0;
			}
		}
	}
	for (int i = 1; i <= R; ++i) {
		for (int j = 1; j <= C; ++j) {
			if (c[i][j] == -1) {
				for (int k = 0; k < 8; ++k) {
					int ni = i + d[k][0];
					int nj = j + d[k][1];
					if ( ok(ni, nj) && c[ni][nj]!=-1 ) {
						++c[ni][nj];
					}
				}
			}
		}
	}
	int x = 0, y = 0;
	for (int i = 1; i <= R; ++i) {
		for (int j = 1; j <= C; ++j) {
			if (c[i][j] == 0) {
				x = i, y = j;
			}
		}
	}
	if (!x && !y) {
		return false;
	}
	for (int i = 1; i <= R; ++i) {
		for (int j = 1; j <= C; ++j) {
			vis[i][j] = false;
		}
	}
	tot = 0;
	dfs(x, y);
	if (tot+M==R*C) {
    //    printf(" yes\n");  // debug
		for (int i = 1; i <= R; ++i) {
			for (int j = 1; j <= C; ++j) {
				if (c[i][j]==-1) printf("*");
				else if (i==x&&j==y) printf("c");
				else printf(".");
			}
			printf("\n");
		}
		return true;
	}
	return false;
}
inline int cnt(int& S)
{
    int ret = 0;
    for (int i = R*C-1; i >= 0; --i) {
        if ((S>>i) & 0x1) ++ret;
    }
    return ret;
}
void solve(void)
{
	if (M==0) {
      //  printf(" yes\n");  // debug
		for (int i = 1; i <= R; ++i) {
			for (int j = 1; j <= C; ++j) {
				if (i==1 && j==1) printf("c");
				else printf(".");
			}
			printf("\n");
		}
		return ;
	}
	if (M+1==R*C) {
	  //  printf(" yes\n");  // debug
		printf("c");
		for (int i = 2; i <= C; ++i) printf("*"); printf("\n");
		for (int i = 2; i <= R; ++i) {
			for (int j = 1; j <= C; ++j) {
				printf("*");
			}
			printf("\n");
		}
		return ;
	}
	int t = 0x1 << (R*C);
	for (int i = 0; i < t; ++i) {
		if (cnt(i) == M) {
			if (check(i)) {
				return ;
			}
		}
	}
	//printf(" no\n");  // debug
	printf("Impossible\n");
}

int main()
{
	int T;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("outb.txt", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		scanf("%d%d%d",&R, &C, &M);
	//	printf("%d %d %d ", R, C, M); // debug
		printf("Case #%d:\n", i);
		solve();
	}
	return 0;
}
