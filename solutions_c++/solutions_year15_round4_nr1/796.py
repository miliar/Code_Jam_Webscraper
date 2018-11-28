#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;
char board[100][100];
char done[100][100];
int R, C, y=0;

void check(int ir, int ic, int dr, int dc, int inc) {
	if (done[ir][ic]) return;
	int r = ir + dr;
	int c = ic + dc;
	while (r >= 0 && r < R && c >= 0 && c < C) {
		if (board[r][c] != '.') {
			done[ir][ic] = true;
			y += inc;
			return;
		}
		r += dr;
		c += dc;
	}
}

int main()
{
	int T;
	cin >> T;
	cout.precision(8);
	for (int casenum = 1; casenum <= T; ++casenum) {
		y = 0;
		cin >> R >> C;
		forn(r, R) {
			cin.ignore();
			forn(c, C) {
				cin >> board[r][c];
				done[r][c] = false;
			}
		}
		bool possible = true;
		forn(r, R) {
			forn(c, C) {
				switch (board[r][c]) {
					case '^':
						check(r, c, -1, 0, 0);
						check(r, c, 0, 1, 1);
						check(r, c, 1, 0, 1);
						check(r, c, 0, -1, 1);
						if (!done[r][c]) possible = false;
						break;
					case '>':
						check(r, c, 0, 1, 0);
						check(r, c, 1, 0, 1);
						check(r, c, 0, -1, 1);
						check(r, c, -1, 0, 1);
						if (!done[r][c]) possible = false;
						break;
					case 'v':
						check(r, c, 1, 0, 0);
						check(r, c, 0, -1, 1);
						check(r, c, -1, 0, 1);
						check(r, c, 0, 1, 1);
						if (!done[r][c]) possible = false;
						break;
					case '<':
						check(r, c, 0, -1, 0);
						check(r, c, -1, 0, 1);
						check(r, c, 0, 1, 1);
						check(r, c, 1, 0, 1);
						if (!done[r][c]) possible = false;
						break;
					default:
						break;
				}
			}
		}
		cout << "Case #" << casenum << ": ";
		if (!possible) {
			cout << "IMPOSSIBLE";
		} else {
			cout << y;
		}
		cout << endl;
	}
	return 0;
}

