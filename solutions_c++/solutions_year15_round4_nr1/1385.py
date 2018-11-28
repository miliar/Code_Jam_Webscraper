#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> ii;
int nTest;
int n, m;
int N;
char a[111][111];
int getnum(int x, int y){
	return (x - 1) * m + y;
}
int checkdir(int x, int y){
	int dx = 0;
	int dy = 0;
	if (a[x][y] == '^') dx = -1;
	if (a[x][y] == '>') dy = 1;
	if (a[x][y] == 'v') dx = 1;
	if (a[x][y] == '<') dy = -1;

	x += dx;
	y += dy;
	while (x >= 1 && x <= n && y >= 1 && y <= m){
		if (a[x][y] != '.') return 1;
		x += dx;
		y += dy;
	}

	return 0;

}
int checknode(int x, int y){
	//0 = ko can
	//1 = doi
	//2 = imp
	if (checkdir(x, y)) return 0;
	else {
		for (int i = 1; i <= 4; i++){
			if (i == 1) a[x][y] = '^';
			if (i == 2) a[x][y] = '<';
			if (i == 3) a[x][y] = '>';
			if (i == 4) a[x][y] = 'v';
			if (checkdir(x, y)) return 1;
		}
	}
	return 2;
}
int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &nTest);
	for (int test = 1; test <= nTest; test++){
		scanf("%d %d\n", &n, &m);
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= m; j++){
				scanf("%c", a[i] + j);
			}
			scanf("\n");
		}
		int ok = 1;
		int ans = 0;
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= m; j++) if (a[i][j] != '.') {
				int z = checknode(i, j);
				if (z > 0){
					if (z == 1) ans++;
					else {
						ok = 0;
						break;
					}
				}
			}
			if (ok == 0) break;
		}
		printf("Case #%d: ", test);
		if (ok) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
}