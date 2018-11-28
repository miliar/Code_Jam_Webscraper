#include <cstdio>
#include <vector>
#include <cmath>
#include <climits>
#include <ctime>
#include <cstring>
#include <cmath>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <iostream>
#include <set>
#include <map>
#include <utility>
#include <deque>
#include <complex>
#include <bitset>
#include <stack>
#include <functional>
#include <cassert>
#include <iomanip>
#include <numeric>

using namespace std;

#if defined(_MSC_VER) || __cplusplus > 199711L
#define typeof decltype
#endif
#ifndef DEBUG
#define dprintf(...)
#else
#define dprintf(...) fprintf(stderr, __VA_ARGS__)
#endif
#define rep(i, n) for(int i = 0, _##i = (n); i < _##i; ++i)
#define repe(i, n) for(int i = 0, _##i = (n); i <= _##i; ++i)
#define foru(i, a, b) for(int i = (a), _##i = (b); i <= _##i; ++i)
#define ford(i, a, b) for(int i = (a), _##i = (b); i >= _##i; --i)
#define forit(i, m) for(typeof((m).begin()) i = (m).begin(), _##i = (m).end(); i != _##i; ++i)

char board[5][5];

bool check_row(int r, char c)
{
	int cnt = 0;
	rep(i, 4) cnt += board[r][i] == c || board[r][i] == 'T';
	return cnt > 3;
}

bool check_col(int col, char c)
{
	int cnt = 0;
	rep(i, 4) cnt += board[i][col] == c || board[i][col] == 'T';
	return cnt > 3;
}

bool check_d1(char c)
{
	int cnt = 0;
	rep(i, 4) cnt += board[i][i] == c || board[i][i] == 'T';
	return cnt > 3;
}

bool check_d2(char c)
{
	int cnt = 0;
	rep(i, 4) cnt += board[i][3 - i] == c || board[i][3 - i] == 'T';
	return cnt > 3;
}

int main(int argc,char *argv[]) 
{
	// freopen("a.in", "r", stdin);
	// freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	rep(x, T)
	{
		goto sue_me;
		killme:
		x++;
		if (x >= T) break;
		sue_me:
		printf("Case #%d: ", x + 1);
		int cnt = 0;
		rep(i, 4)
		{
			scanf("%s", board[i]);
			rep(j, 4) cnt += board[i][j] != '.';
		}
		rep(i, 4)
		{
			if (check_row(i, 'X')) { puts("X won"); goto killme; }
			else if (check_row(i, 'O')) { puts("O won"); goto killme; }
		}
		rep(i, 4)
		{
			if (check_col(i, 'X')) { puts("X won"); goto killme; }
			else if (check_col(i, 'O')) { puts("O won"); goto killme; }
		}
		if (check_d1('X')) { puts("X won"); goto killme; }
		else if (check_d1('O')) { puts("O won"); goto killme; }
		if (check_d2('X')) { puts("X won"); goto killme; }
		else if (check_d2('O')) { puts("O won"); goto killme; }
		if (cnt == 16) puts("Draw");
		else puts("Game has not completed");
	}
	return 0;
}
