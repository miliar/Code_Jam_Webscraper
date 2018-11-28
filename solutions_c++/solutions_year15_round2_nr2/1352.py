#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAX 32
using namespace std;

int R, C, N;
int grid[MAX][MAX];

int cost() {
	int c = 0;
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			if(grid[i][j] != -1 && grid[i][j + 1] != -1) {
				c += 1;
			}
			if(i > 0) {
				if(grid[i][j] != -1 && grid[i - 1][j] != -1) {
					c += 1;
				}
			}
		}
	}
	return c;
}

int solve(int x, int y, int curr) {
	//printf("%d %d %d\n", x, y, curr);
	// column adjustment
	if(y == C) {
		y = 0;
		x += 1;
	}
	//final
	if(x == R) {
		return curr == N ? cost() : 1e9;
	}
 	if(curr == N) {
 		return cost();
 	}

	// place
	grid[x][y] = curr;
	int res1 = solve(x, y + 1, curr + 1);

	// skip
	grid[x][y] = -1;
	int res2 = solve(x, y + 1, curr);
	return min(res1, res2);
}

int main(int argc, char const *argv[]) {
	int cases;
	

	scanf("%d", &cases);

	for(int i = 1; i <= cases; i++) {
		scanf("%d %d %d", &R, &C, &N);
		memset(grid, -1, sizeof grid);
		printf("Case #%d: %d\n", i, solve(0, 0, 0));
	}

	return 0;
}