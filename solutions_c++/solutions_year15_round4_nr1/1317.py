#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <map>
using namespace std;
int TC, R, C, nothing[4][105][105], dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
char g[105][105];
map<char, int> mp;
bool ob(int x, int y){
	if(x == -1 || y == -1 || x == R || y == C) return true;
	else return false;
}
void fillup(int i, int j, int k){
	if(nothing[i][j][k] != -1) return;
	int nx = j + dir[i][0], ny = k + dir[i][1];
	if(ob(nx, ny)) nothing[i][j][k] = 1;
	else{
		fillup(i, nx, ny);
		if(g[nx][ny] == '.') nothing[i][j][k] = nothing[i][nx][ny];
		else nothing[i][j][k] = 0;
	}
}
int main(){
	mp['>'] = 0;
	mp['<'] = 2;
	mp['^'] = 3;
	mp['v'] = 1;
	scanf("%d", &TC);
	for(int tc = 1; tc <= TC; ++tc){
		memset(nothing, -1, sizeof(nothing));
		scanf("%d %d", &R, &C);
		for(int i = 0; i < R; ++i){
			scanf("%s", g[i]);
		}
		for(int i = 0; i < R; ++i){
			for(int j = 0; j < C; ++j){
				for(int k = 0; k < 4; ++k){
					fillup(k, i, j);
				}
			}
		}
		int ans = 0;
		for(int i = 0; i < R; ++i){
			for(int j = 0; j < C; ++j){
				if(g[i][j] != '.'){
					if(nothing[mp[g[i][j]]][i][j] == 1) ++ ans;
					if(nothing[0][i][j]+nothing[1][i][j]+nothing[2][i][j]+nothing[3][i][j] == 4) ans = -10000000;
				}
			}
		}
		if(ans < 0) printf("Case #%d: IMPOSSIBLE\n", tc);
		else printf("Case #%d: %d\n", tc, ans);
	}
}