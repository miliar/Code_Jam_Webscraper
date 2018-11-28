#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
const int N = 10;
bool a[N][N];
int p[N][N];
int r, c, m;
// -1 = *, -2 = c
bool check() {
	int cnt = 0, ex, ey;
	memset(p, 0, sizeof(p));
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++) {
			if (a[i][j]) {
				p[i][j] = -1;
				continue;
			}
			for (int x = i - 1; x <= i + 1; x++)
				for (int y = j - 1; y <= j + 1; y++) {
					if (x == i && y == j)
						continue;
					if (x < 0 || x >= r || y < 0 || y >= c)
						continue;
					if (a[x][y])
						p[i][j]++;
				}
			if(p[i][j] == 0){
				cnt++;
				ex = i;
				ey = j;
			}
		}
	if(m == r * c - 1){
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				if(p[i][j] != -1){
					p[i][j] = -2;
					return true;
				}
	}
//	if(cnt == 0) return false;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++) {
			if (a[i][j])
				continue;
			bool flag = false;
			for (int x = i - 1; x <= i + 1; x++)
				for (int y = j - 1; y <= j + 1; y++) {
					if (x == i && y == j)
						continue;
					if (x < 0 || x >= r || y < 0 || y >= c)
						continue;
					if (p[x][y] == 0){
						flag = true;
						break;
					}
				}
			if(!flag){
				if(p[i][j] == 0 && cnt == 1) continue;
				return false;
			}
		}
	p[ex][ey] = -2;
	return true;
}
bool dfs(int x, int y, int m) {
//	printf("x=%d y=%d m=%d\n", x, y, m);

	if (m == 0)
		return check();
	if(m < 0)
		return false;
	if(x >= r || y >= c)
		return false;

	if (r * c < x * c + y + m)
		return false;

	for (int i = x; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (i == x && j < y)
				continue;
			a[i][j] = true;

			if(j == c - 1){
				if(dfs(i + 1, 0, m - 1)) return true;
			} else {
				if(dfs(i, j + 1, m - 1)) return true;
			}

			a[i][j] = false;
		}
	}
	return false;
}
int main() {
	int t;
	freopen("C-small-attempt3.in", "r", stdin);
	freopen("C-small-attempt3.out", "w", stdout);
	scanf("%d", &t);
//	printf("%d\n", t);
	for (int cas = 1; cas <= t; cas++) {
		scanf("%d%d%d", &r, &c, &m);
//		printf("%d %d %d\n", r, c, m);
		memset(a, false, sizeof(a));
		bool ans = dfs(0, 0, m);
		printf("Case #%d: \n", cas);
		if(ans){
			for(int i = 0; i < r; i++){
				for(int j = 0; j < c; j++){
					if(p[i][j] == -1)
						printf("*");
					else if(p[i][j] == -2)
						printf("c");
					else
						printf(".");
				}
				puts("");
			}
		} else {
			puts("Impossible");
		}
	}
	return 0;
}
