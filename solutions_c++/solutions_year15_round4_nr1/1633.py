#include <iomanip>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
using namespace std;

#define MAX 100

#define ok(r, c) ((r)>=0&&(c)>=0&&(r)<R&&(c)<C)

typedef pair<int, int> Pt;

#define mp make_pair

int dr[] = { -1, 0, 1, 0 };
int dc[] = { 0, 1, 0, -1 };
int inv[] = { 2, 3, 0, 1 };

#define kr (r + k * dr[d])
#define kc (c + k * dc[d])

#define PT(r, c) mp((r) + 1, (c) + 1)
#define row first - 1
#define col second - 1

int main() {
	int T;
	cin >> T;

	for (int t = 0; t++ < T;) {
		int R, C;
		int grid[MAX][MAX];
		cin >> R >> C;

		Pt interesting[MAX][MAX][4] = {};
		int cyc[MAX][MAX] = {};
		int ncyc = 0;

		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				char ch;
				cin >> ch;
				cerr << ch;
				switch (ch) {
					case '^': grid[r][c] = 0; break;
					case '>': grid[r][c] = 1; break;
					case 'v': grid[r][c] = 2; break;
					case '<': grid[r][c] = 3; break;
					default : grid[r][c] = -1;
				}
			}
			cerr << endl;
		}

		bool noInt = false, thing = false;
		for (int r = 0; !noInt && r < R; r++) {
			for (int c = 0; !noInt && c < C; c++) {
				if (grid[r][c] + 1) {
					thing = true;
					noInt = true;
					for (int d = 0; d < 4; d++) {
						for (int k = 1; ok(kr, kc); k++) {
							if (grid[kr][kc] + 1) {
								interesting[r][c][d] = PT(kr, kc);
								noInt = false;
								break;
							}
						}
					}
				}
			}
		}

		if (noInt) {
			cout << "Case #" << t << ": IMPOSSIBLE\n";
			cerr << "Case #" << t << ": IMPOSSIBLE\n";
			continue;
		} else if (!thing) {
			cout << "Case #" << t << ": 0\n";
			cerr << "Case #" << t << ": 0\n";
			continue;
		}

		int K = 0;
		bool v[MAX][MAX] = {};
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (grid[r][c] + 1 && !v[r][c]) {
					// follow path until we reach: (1) v, (2) fail
					int nr = r, nc = c;
					while (1) {
						if (!ok(nr, nc)) {
							K++;
							//cerr << " fix " << r << " " << c << endl;
							break;
						} else if (v[nr][nc]) {
							break;
						} else {
							v[nr][nc] = true;
							Pt x = interesting[nr][nc][grid[nr][nc]];
							nr = x.row;
							nc = x.col;
						}
					}
				}
			}
		}

		cout << "Case #" << t << ": " << K << endl;
		cerr << "Case #" << t << ": " << K << endl;
	}
	return 0;
}
