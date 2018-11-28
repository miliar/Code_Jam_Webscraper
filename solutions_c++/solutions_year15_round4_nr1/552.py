#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

int dir[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};

int check[102][102][4], grid[102][102];

int R, C;
/*
. period = no arrow
^ caret = up arrow
> greater than = right arrow
v lowercase v = down arrow
< les
*/
void input() {
	scanf("%d%d", &R, &C);
	char buf[128];
	for(int i = 0;i <= R+1;i ++) for(int j = 0;j <= C+1;j ++) grid[i][j] = 4;
	for(int i = 1;i <= R;i ++) {
		scanf("%s", &buf);
		for(int j = 0;j < C;j ++) {
			if(buf[j] == '.') grid[i][j+1] = 4;
			if(buf[j] == '^') grid[i][j+1] = 0;
			if(buf[j] == '>') grid[i][j+1] = 1;
			if(buf[j] == 'v') grid[i][j+1] = 2;
			if(buf[j] == '<') grid[i][j+1] = 3;
		}
	}
}

void solve() {
	memset(check, 0, sizeof(check));

	for(int i = 1;i <= R;i ++) for(int j = 1;j <= C;j ++) {
		if(check[i-1][j][0]||grid[i-1][j] != 4) check[i][j][0] = 1;
		if(check[i][j-1][3]||grid[i][j-1] != 4) check[i][j][3] = 1;
	}

	for(int i = R;i >= 1;i --) for(int j = C;j >= 1;j --) {
		if(check[i+1][j][2]||grid[i+1][j] != 4) check[i][j][2] = 1;
		if(check[i][j+1][1]||grid[i][j+1] != 4) check[i][j][1] = 1;
	}

	int res = 0;
	for(int i = 1;i <= R;i ++) for(int j = 1;j <= C;j ++) {
		if(grid[i][j] == 4) continue;
		if(check[i][j][grid[i][j]]) continue;

		if(!check[i][j][0]&&!check[i][j][1]&&!check[i][j][2]&&!check[i][j][3]) {
			printf("IMPOSSIBLE\n");
			return ;
		}
		++ res;
	}
	printf("%d\n", res);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Case;
	scanf("%d", &Case);
	for(int cas = 1;cas <= Case;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
}