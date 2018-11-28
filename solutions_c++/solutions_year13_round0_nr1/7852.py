#include <cstdio>

#define FOR(i,a,b) for (int i=(a); i<(b); i++)
#define MAX 10

using namespace std;

int t, x, y;
char grid[MAX][MAX], W;

void find(char c) {
	FOR(i,0,4) FOR(j,0,4)
		if (grid[i][j] == c) {
			x = j, y = i;
			return;
		}
	x = -1, y = -1;
}

char solve() {
	FOR(i,0,4) {
		if (grid[i][0] == grid[i][1] &&
			grid[i][1] == grid[i][2] &&
			grid[i][2] == grid[i][3] &&
			grid[i][3] != '.')
			return grid[i][0];
		else if (grid[0][i] == grid[1][i] &&
			grid[1][i] == grid[2][i] &&
			grid[2][i] == grid[3][i] &&
			grid[3][i] != '.')
			return grid[0][i];
	}
	if (grid[0][0] == grid[1][1] &&
		grid[1][1] == grid[2][2] &&
		grid[2][2] == grid[3][3] &&
		grid[3][3] != '.')
		return grid[0][0];
	else if (grid[0][3] == grid[1][2] &&
		grid[1][2] == grid[2][1] &&
		grid[2][1] == grid[3][0] &&
		grid[3][0] != '.')
		return grid[0][3];
	return 0;
}

int main() {
	scanf("%d\n", &t);
	FOR(i,0,t) {
		FOR(j,0,4) fgets(grid[j], MAX, stdin);
		getchar();
		
		find('T');
		if (x != -1 && y != -1) {
			grid[y][x] = 'X';
			W = solve();
			if (!W) {
				grid[y][x] = 'O';
				W = solve();	
			}
		}
		else W = solve();
		
		printf("Case #%d: ", i+1);
		
		if (!W) {
			find('.');
			if (x == -1 && y == -1)
				printf("Draw\n");
			else
				printf("Game has not completed\n");
		}
		else printf("%c won\n", W);
	}

	return 0;
}