#include <bits/stdc++.h>

using namespace std;

#define MAXN 110
int r, c;
char grid[MAXN][MAXN];

bool has(int sx, int sy, int x, int y, int a, int b) {
	if(x < 0 || y < 0 || x >= r || y >= c) return false;
	if(grid[x][y] != '.' && (x!=sx || y!=sy)) return true;
	return has(sx, sy, x+a, y+b, a, b);
}
bool hasUp(int x, int y) {
	return has(x, y, x, y, -1, 0);
}
bool hasDown(int x, int y) {
	return has(x, y, x, y, 1, 0);
}
bool hasLeft(int x, int y) {
	return has(x, y, x, y, 0, -1);
}
bool hasRight(int x, int y) {
	return has(x, y, x, y, 0, 1);
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int test = 1; test<=t; test++) {
		printf("Case #%d: ", test);
		scanf("%d %d", &r, &c);
		for(int i = 0; i<r; i++) {
			for(int j = 0; j<c; j++) {
				scanf(" %c", &grid[i][j]);
			}
		}
		int ret = 0;
		bool cant = false;
		for(int i = 0; i<r; i++) {
			for(int j = 0; j<c; j++) {
				if(grid[i][j] != '.') {
					if(grid[i][j] == '^') {
						if(!hasUp(i, j)) {
							if(hasLeft(i, j) || hasRight(i, j) || hasDown(i, j)) ret++;
							else  {
					
								cant = true;
							}
						}
					}
					if(grid[i][j] == '>') {
						if(!hasRight(i, j)) {
							if(hasLeft(i, j) || hasUp(i, j) || hasDown(i, j)) ret++;
							else cant = true;
						}
					}
					if(grid[i][j] == '<') {
						if(!hasLeft(i, j)) {
							if(hasUp(i, j) || hasRight(i, j) || hasDown(i, j)) ret++;
							else cant = true;
						}
					}
					if(grid[i][j] == 'v') {
						if(!hasDown(i, j)) {
							if(hasLeft(i, j) || hasRight(i, j) || hasUp(i, j)) ret++;
							else cant = true;
						}
					}
				}
			}
		}
		if(cant) {
			printf("IMPOSSIBLE\n");
		}
		else {
			printf("%d\n", ret);
		}
	}
	return 0;
}