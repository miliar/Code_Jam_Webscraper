#include <algorithm>
#include <climits>
#include <iostream>
using namespace std;

long board[50][50];
int R, C, M;
long id = 2;
int cr, cc;

char letter(int r, int c)
{
	if (board[r][c] == LONG_MAX) return '*';
	else if (r == cr && c == cc) return 'c';
	else return '.';
}

void print()
{
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++)
			cout << letter(r, c);
		cout << "\n";
	}
}

int valid(int r, int c)
{
	return r >= 0 && r < R && c >= 0 && c < C;
}

bool zero(int r, int c)
{
	for (int rr = r-1; rr <= r+1; rr++)
		for (int cc = c-1; cc <= c+1; cc++)
			if (cc != c || rr != r)
				if (valid(rr, cc) && board[rr][cc] == LONG_MAX)
					return false;
	return true;
}

long flood(int r, int c)
{
	if (!valid(r, c) || board[r][c] >= id) return 0;
	int ans = 1;
	board[r][c] = id;
	if (zero(r, c))
		for (int rr = r-1; rr <= r+1; rr++)
			for (int cc = c-1; cc <= c+1; cc++)
				if (cc != c || rr != r)
					ans += flood(rr, cc);
	return ans;
}

bool run(int r, int c, int m, int sr, int sc)
{
	if (r*C + c + m > R*C) return false;
	if (r == R) {
		id++;
		if (flood(sr, sc) + M == R * C) {
			cr = sr;
			cc = sc;
			return true;
		}
		return false;
	}
	int nr = r, nc = c + 1;
	if (nc == C) nc = 0, nr++;
	board[r][c] = 0;
	if (run(nr, nc, m, r, c)) return true;
	if (m > 0) {
		board[r][c] = LONG_MAX;
		if (run(nr, nc, m - 1, sr, sc)) return true;
	}
	return false;
}

int main()
{
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		cin >> R >> C >> M;
		cout << "Case #" << test << ":\n";
		if (run(0, 0, M, -1, -1)) {
			print();
		} else {
			cout << "Impossible\n";
		}
	}
}
