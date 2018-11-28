#include <iostream>
#include <cstring>

using namespace std;

int main() {
	int ncase; cin >> ncase;
	for (int cs = 1; cs <= ncase; cs++) {
		int nr, nc; cin >> nr >> nc;
		string grid[nr];
		for (int r = 0; r < nr; r++) {
			cin >> grid[r];
		}

		int next[nr][nc][4];
		memset(next, -1, sizeof next);
		
		for (int r = 0; r < nr; r++) {
			int prev = -1;
			// right
			for (int c = nc-1; c >= 0; c--) {
				next[r][c][0] = prev;
				if (grid[r][c] != '.') prev = c;
			}
			// left
			prev = -1;
			for (int c = 0; c < nc; c++) {
				next[r][c][1] = prev;
				if (grid[r][c] != '.') prev = c;
			}
		}
		for (int c = 0; c < nc; c++) {
			int prev = -1;
			// down
			for (int r = nr-1; r >= 0; r--) {
				next[r][c][2] = prev;
				if (grid[r][c] != '.') prev = r;
			}
			// up
			prev = -1;
			for (int r = 0; r < nr; r++) {
				next[r][c][3] = prev;
				if (grid[r][c] != '.') prev = r;
			}
		}
		int ans = 0;
		bool possible = true;
		for (int r = 0; r < nr; r++) {
			for (int c = 0; c < nc; c++) {
				char cell = grid[r][c];
				bool currpossible = false;
				if (cell == '.') continue;
				for (int i = 0; i < 4; i++) {
					currpossible = currpossible || (next[r][c][i] > -1);
				}
				if (!currpossible) {
					possible = false;
					goto end;
				}
				if (cell == '<') {
					if (next[r][c][1] == -1) ans++;
				} else if (cell == '>') {
					if (next[r][c][0] == -1) ans++;
				} else if (cell == 'v') {
					if (next[r][c][2] == -1) ans++;
				} else if (cell == '^') {
					if (next[r][c][3] == -1) ans++;
				}
			}
		}

		end: if (possible) {
			cout << "Case #" << cs << ": " << ans << endl;
		} else {
			cout << "Case #" << cs << ": IMPOSSIBLE" << endl;
		}
	}
}
