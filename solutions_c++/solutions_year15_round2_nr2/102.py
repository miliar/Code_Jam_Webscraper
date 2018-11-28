#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

long R, C, N;
int board[10000][10000];

void remove(int i, int j)
{
	int x = board[i][j];
	board[i][j] = 9;
	//cout << "R: " << i << ',' << j << ' ' << x << endl;
	if (i > 0 && board[i-1][j] != 9) {
		--board[i-1][j];
		--x;
	} 
	if (i < R-1 && board[i+1][j] != 9) {
		--board[i+1][j];
		--x;
	}
	if (j > 0 && board[i][j-1] != 9) {
		--board[i][j-1];
		--x;
	} 
	if (j < C-1 && board[i][j+1] != 9) {
		--board[i][j+1];
		--x;
	}
	assert(x == 0);
}

long minimize(long n)
{
	long x = 0;
	long cap = 3;
	while (n < R*C) {
		for (int i = 0; i < R && n < R*C; ++i) {
			for (int j = 0; j < C && n < R*C; ++j) {
				if (board[i][j] == cap) {
					remove(i, j);
					x += cap;
					++n;
				}
			}
		}
		--cap;
	}
	return x;
}
void set_board()
{
	forn(i, R) {
		forn(j, C) {
			board[i][j] = 4;
			if (j == 0) --board[i][j];
			if (j == C - 1) --board[i][j];
			if (i == 0) --board[i][j];
			if (i == R - 1) --board[i][j];
		}
	}
}
void p(long u)
{
	cout << endl << "Board: " << u << endl;
	forn(i, R) {
		forn(j, C) {
			cout << board[i][j];
		}
		cout << endl;
	}
}
int main()
{
	int T;
	cin >> T;
	cout.precision(8);
	for (int casenum = 1; casenum <= T; ++casenum) {
		cin >> R >> C >> N;
		cout << "Case #" << casenum << ": ";
		//cout << R << 'x' << C << "-> " << N << endl;
		if (N <= (R*C+1)/2) {
			cout << 0;
		} else {
			//p();
			long u = 2*R*C - R - C;
			long v = u;
			long n = N;
			set_board();
			for (int i = 1; n < R*C && i < R-1; ++i) {
				for (int j = 1+i%2; n < R*C && j < C-1; j += 2) {
					++n;
					remove(i, j);
					u -= 4;
				}
			}
			u -= minimize(n);
			//p(u);
			n = N;
			set_board();
			for (int i = 1; n < R*C && i < R-1; ++i) {
				for (int j = 2-i%2; n < R*C && j < C-1; j += 2) {
					++n;
					remove(i, j);
					v -= 4;
				}
			}
			v -= minimize(n);
			//p(v);
			cout << min(u, v);
		}
		cout << endl;

	}
	return 0;
}

