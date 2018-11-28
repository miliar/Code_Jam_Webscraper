#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

#define DO for (int rr = r-1; rr <= r+1; rr++) for (int cc = c-1; cc <= c+1; cc++) if (cc != c || rr != r)

const int MAX = 50;
long board[MAX][MAX];
int R, C, M;
long id = 2;
int cr, cc;

bool empty(int r, int c)
{
	return r < 0 || c < 0 || r >= R || c >= C || board[r][c] != LONG_MAX;
}

bool zero(int r, int c)
{
	DO if (!empty(rr, cc)) return false;
	return true;
}

long flood(int r, int c)
{
	if (board[r][c] >= id || r < 0 || c < 0 || r >= R || c >= C) return 0;
	int ans = 1;
	board[r][c] = id;
	if (zero(r, c)) DO ans += flood(rr, cc);
	return ans;
}

bool run(int r, int c, int m, int sr, int sc)
{
	if (r*C + c + m > R*C) return false;
	if (r == R) {
		id++;
		bool success = flood(sr, sc) + M == R * C;
		if (success) {
			cr = sr;
			cc = sc;
		}
		return success;
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

void print()
{
	for (int r = 0; r < R; r++)
	{
		for (int c = 0; c < C; c++)
		{
			cout << (board[r][c] == LONG_MAX ? '*' : r == cr && c == cc ? 'c' : '.');
		}
		cout << "\n";
	}
}

int main()
{
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++)
	{
		cin >> R >> C >> M;
		cout << "Case #" << test + 1 << ":\n";
		if (run(0, 0, M, -1, -1)) {
			print();
		} else {
			cout << "Impossible\n";
		}
	}
}
