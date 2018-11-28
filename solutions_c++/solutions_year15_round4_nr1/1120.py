#include <iostream>
#include <vector>
#define forn(i, s, n) for (int i = (s); i < (n); i++)
#define sI(N) scanf("%d", &N)
using namespace std;

int R, C;

bool checkRight(vector<string> grid, int i, int j) {
	for (int k = j + 1; k < C; k++) {
		if (grid[i][k] != '.') {
			return true;
		}
	}
	return false;
}

bool checkLeft(vector<string> grid, int i, int j) {
	for (int k = j - 1; k >= 0; k--) {
		if (grid[i][k] != '.') {
			return true;
		}
	}
	return false;
}

bool checkTop(vector<string> grid, int i, int j) {
	for (int k = i - 1; k >= 0; k--) {
		if (grid[k][j] != '.') {
			return true;
		}
	}
	return false;
}

bool checkBottom(vector<string> grid, int i, int j) {
	for (int k = i + 1; k < R; k++) {
		if (grid[k][j] != '.') {
			return true;
		}
	}
	return false;
}

int main() {
	int T, t;
	sI(T);
	forn(t, 1, T + 1) {
		int N;
		sI(R);sI(C);
		vector<string> grid;
		string s;
		for (int i = 0; i < R; i++) {
			cin >> s;
			grid.push_back(s);
		}

		int ans = 0;
		bool impossible = false;
		for (int i = 0; i < R; i++) {
			//cout << grid[i] << endl;
			for (int j = 0; j < C; j++) {
				///printf("%d, %d, %c\n", i, j, grid[i][j]);
				if (grid[i][j] == '^') {
					if (!checkTop(grid, i, j)) {
						if (checkBottom(grid, i, j) || checkLeft(grid, i, j) || checkRight(grid, i, j)) {
							ans++;
						} else {
							impossible = true;
							break;
						}
					}
				} else if (grid[i][j] == 'v') {
					if (!checkBottom(grid, i, j)) {
						if (checkTop(grid, i, j) || checkLeft(grid, i, j) || checkRight(grid, i, j)) {
							ans++;
						} else {
							impossible = true;
							break;
						}
					}
				} else if (grid[i][j] == '>') {
					if (!checkRight(grid, i, j)) {
						if (checkBottom(grid, i, j) || checkLeft(grid, i, j) || checkTop(grid, i, j)) {
							ans++;
						} else {
							impossible = true;
							break;
						}
					}
				} else if (grid[i][j] == '<') {
					if (!checkLeft(grid, i, j)) {
						if (checkBottom(grid, i, j) || checkTop(grid, i, j) || checkRight(grid, i, j)) {
							ans++;
						} else {
							impossible = true;
							break;
						}
					}
				}
			}
			if (impossible) {
				break;
			}
		}

		if (impossible) {
			printf("Case #%d: IMPOSSIBLE\n", t);
		} else {
			printf("Case #%d: %d\n", t, ans);
		}
	}
	return 0;
}