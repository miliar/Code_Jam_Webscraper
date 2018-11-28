#include <cstdio>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int n, m;
char bd[105][105];
bool v[105][105], sink[105][105];
int dx[4] = {0, -1, 0, 1}, dy[4] = {-1, 0, 1, 0};
int dir[300];

void dfs(int d, int y, int x, int ly, int lx){
	if (y < 0 || x < 0 || x >= m || y >= n){
		sink[ly][lx] = 1;
		return;
	}
	if (v[y][x] && bd[y][x] != '.') return;
	v[y][x] = 1;
	if (bd[y][x] == '.') dfs(d, y + dy[d], x + dx[d], ly, lx);
	else{
		int dd = dir[bd[y][x]];
		dfs(dd, y + dy[dd], x + dx[dd], y, x);
	}
}

void solve(){
	memset(v, 0, sizeof(v));
	memset(sink, 0, sizeof(sink));
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) scanf("%s", bd[i]);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (bd[i][j] != '.' && !v[i][j]) dfs(0, i, j, i, j);
	int ct = 0, imposs = 0;
	for (int i = 0; i < n; i++){
		
	}
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			if (sink[i][j]){
				ct++;
				bool good = 0;
				for (int k = 0; k < 4; k++){
					for (int l = 1;; l++){
						int nx = j + dx[k] * l, ny = i + dy[k] * l;
						if (nx < 0 || ny < 0 || nx >= m || ny >= n) break;
						if (bd[ny][nx] != '.') good = 1;
					}
				}
				if (!good) imposs = 1;
			}
		}
	}
	if (imposs) printf("IMPOSSIBLE\n");
	else printf("%d\n", ct);
}

int main(){
	dir['^'] = 0, dir['<'] = 1, dir['v'] = 2, dir['>'] = 3;
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}
