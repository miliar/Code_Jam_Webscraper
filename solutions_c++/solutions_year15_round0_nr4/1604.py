#include <bits/stdc++.h>
using namespace std;

int mat[20][20];
int X, R, C;

int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0 };

int valid(int x, int y) {
	return x >= 0 && y >= 0 && x < R && y < C;
}

int dfs(int mat[20][20], int i, int j) {
	if (mat[i][j] != 0) return 0;
	mat[i][j] = -1;
	
	int sum = 1;
	for (int k = 0; k < 4; k++)
		if (valid(i+dx[k], j+dy[k]))
			sum += dfs(mat, i+dx[k], j+dy[k]);
	return sum;
}

int check() {
	int cpy[20][20];
	memcpy(cpy, mat, sizeof(mat));
	
	int s = 0;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (cpy[i][j] == 0) 
				s = dfs(cpy, i, j);
			if (s % X != 0)
				return false;
		}
	}
	return true;
}

int bruteforce(int s) {
	if (s == X) return check();
	
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			// se è usato lo estendo
			if (mat[i][j] == 1) {
				// in ogni direzione
				for (int k = 0; k < 4; k++) {
					int x = i+dx[k];
					int y = j+dy[k];
					if (valid(x, y) && mat[x][y] == 0) {
						mat[x][y] = 1;
						if (bruteforce(s+1))
							return true;
						mat[x][y] = 0;
					}
				}
			}			
		}
	}
	return false;
	
}

int solve(int X, int R, int C) {
	
	int m = min(R, C);
	int M = max(R, C);
	
	// anello
	if (X >= 7) return 1;
	// i tonti non cornano
	if ((R*C)%X != 0) return 1;
	
	// linea dritta
	if (X > M) return 1;
	// caso base
	if (X == 1) return 0;
	// 2 sempre possibile se sono multiple
	if (X == 2) return 0;
	if (X == 3) {
		// solo L dà problemi
		if (m < 2) return 1;
		return 0;
	}
	if (X == 4) {
		// la Z rende dispari+dispari in file da 2
		if (m < 3) return 1;
		return 0;
	}
	if (X == 5) {
		// la croce limita il minimo
		if (m < 3) return 1;
		return 0;
	}
	if (X == 6) {
		// la croce 
		if (m == 4 && M >= 9) return 0;
		if (m < 5) return 1;
		return 0;
	}
	return 0;
}
// RICHARD = IMPOSSIBLE
// GABRIEL = POSSIBLE
int table[5][5][5];
int main() {
	/*for (X = 1; X <= 4; X++)
		for (R = 1; R <= 4; R++)
			for (C = 1; C <= 4; C++)		
				printf("(%d,%d,%d) = %s\n", X, R, C, solve(X, R, C) ? "Impossible" : "Always possible");
				//table[X][R][C] = solve(X, R, C);
	*/
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> X >> R >> C;
		if (solve(X, R, C) == 0)
			cout << "Case #" << t << ": GABRIEL" << endl;
		else
			cout << "Case #" << t << ": RICHARD" << endl;
	}
}
