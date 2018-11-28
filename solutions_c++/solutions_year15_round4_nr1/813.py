#include <cassert>
#include <iostream>
#include <vector>

#define FOR(it, seq) for(auto it : seq)
#define FORI(it, beg, end) for(auto it = beg; it != end; ++it)

#define DBG(x) cout << x
#define DBGV(v) {cout << "["; FOR(i_, v) {DBG(i_); cout << ", ";} cout << "]" << endl; }

using namespace std;

typedef long long lint;
typedef vector<int> VI;
typedef vector<lint> VL;
typedef vector<vector<char>> Grid;

int T, R, C;

char next(Grid &grid, int r, int c, char dir) {
	int dr, dc;
	switch(dir) {
		case '<': dr =  0; dc = -1; break;
		case '>': dr =  0; dc =  1; break;
		case 'v': dr =  1; dc =  0; break;
		case '^': dr = -1; dc =  0; break;
		default:
			  assert(false);
	}
	int i = 0;
	int nr, nc;
	do {
		++i;
		nr = r + i*dr;
		nc = c + i*dc;
		if (nr >= R || nr < 0 || nc >= C || nc < 0) {
			return '!';
		}
	} while (grid[nr][nc] == '.');

	return grid[nr][nc];
}

int solve() {
	char EOL;
	cin >> R >> C;
	//cin >> EOL;
	//DBG(EOL);
	

	vector<vector<char>> grid(R, vector<char>(C));
	FORI(r, 0, R) {
		FORI(c, 0, C) {
			cin >> grid[r][c];
		}
		//cin >> EOL;
	}
	//FORI(r, 0, R) DBGV(grid[r]);

	vector<vector<bool>> safe(R, vector<bool>(C));

	int result = 0;
	FORI(r, 0, R) FORI(c, 0, C) {
		if (grid[r][c] == '.') {
			safe[r][c] = true;
			continue;
		}

		if (next(grid, r, c, grid[r][c]) != '!') {
			safe[r][c] = true;
		} else {
			bool exists = false;
			for (char dir : {'>', '<', 'v', '^'}) {
				if (next(grid, r, c, dir) != '!') {
					exists = true;
					break;
				}
			}
			if (exists) {
				result += 1;
			}
			safe[r][c] = exists;
		}
	}

	FORI(r, 0, R) FORI(c, 0, C) {
		if (!safe[r][c]) {
			return -1;
		}
	}
	return result;
}

int main(int argc, char *argv[])
{
	cin >> T;

	FORI(t, 0, T) {
		cout << "Case #" << (t+1) << ": ";

		int r = solve();
		if (r < 0) {
			cout << "IMPOSSIBLE";
		} else {
			cout << r;
		}

		cout << endl;
	}


	return 0;
}
