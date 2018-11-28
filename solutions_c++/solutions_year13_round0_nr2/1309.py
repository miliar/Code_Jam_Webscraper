#include<iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int g[105][105], mark[105][105];
int mk = 1, n, m;
bool vis[105 * 105];
bool isin(int x, int y);
int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
void dfs(int x, int y){
	mark[x][y] = mk;
	for(int i = 0; i < 4; i++){
		int tx = x + dir[i][0], ty = y + dir[i][1];
		if(g[tx][ty] == g[x][y] && mark[tx][ty] == 0){
			dfs(tx, ty);
		}
	}
}
int col[105], row[105];
int main() {
	freopen("B-large.in", "r", stdin);
	int cas, c = 1;
	scanf("%d", &cas);
	while(cas--){
		scanf("%d%d", &n, &m);
		printf("Case #%d: ", c++);
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= m; j++){
				scanf("%d", &g[i][j]);
			}
		}
		for(int i = 1; i <= n; i++){
			row[i] = 0;
			for(int j = 1; j <= m; j++){
				row[i] = max(row[i], g[i][j]);
			}
		}
		for(int i = 1; i <= m; i++){
			col[i] = 0;
			for(int j = 1; j <= n; j++){
				col[i] = max(col[i], g[j][i]);
			}
		}
		bool flag = true;
		for(int i = 1; i <= n && flag; i++){
			for(int j = 1; j <= m && flag; j++){
				if(g[i][j] != row[i] && g[i][j] != col[j])
					flag = false;
			}
		}
		if(flag){
			puts("YES");
		}
		else{
			puts("NO");
		}
	}
}
 				    
