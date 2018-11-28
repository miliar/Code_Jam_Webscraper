/*
 * c.cpp
 *
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <gmpxx.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {
}

typedef vector<vector<char> > t_board;


const char EMPTY = '.';
const char UP = '^';
const char RIGHT = '>';
const char LEFT = '<';
const char DOWN = 'v';

bool needChange(const t_board &g, int r, int c, int i, int j) {
	if (g[i][j] == EMPTY) {
		return false;
	}
	if (g[i][j] == UP) {
		for (int y = i-1; y >= 0; --y) {
			if (g[y][j] != EMPTY) {
				return false;
			}
		}
	}
	if (g[i][j] == DOWN) {
		for (int y = i+1; y < r; ++y) {
			if (g[y][j] != EMPTY) {
				return false;
			}
		}
	}
	if (g[i][j] == LEFT) {
		for (int x = j-1; x >= 0; --x) {
			if (g[i][x] != EMPTY) {
				return false;
			}
		}
	}
	if (g[i][j] == RIGHT) {
		for (int x = j+1; x < c; ++x) {
			if (g[i][x] != EMPTY) {
				return false;
			}
		}
	}
	return true;
}

bool noWay(const t_board &g, int r, int c, int i, int j) {
	if (g[i][j] != UP) {
		for (int y = i-1; y >= 0; --y) {
			if (g[y][j] != EMPTY) {
				return false;
			}
		}
	}
	if (g[i][j] != DOWN) {
		for (int y = i+1; y < r; ++y) {
			if (g[y][j] != EMPTY) {
				return false;
			}
		}
	}
	if (g[i][j] != LEFT) {
		for (int x = j-1; x >= 0; --x) {
			if (g[i][x] != EMPTY) {
				return false;
			}
		}
	}
	if (g[i][j] != RIGHT) {
		for (int x = j+1; x < c; ++x) {
			if (g[i][x] != EMPTY) {
				return false;
			}
		}
	}
	return true;
}

int solve(const t_board &grid, int r, int c) {
	int cnt = 0;
	forn (i, r) {
		forn (j, c) {
			if (needChange(grid, r, c, i ,j)) {
				++cnt;
				if (noWay(grid,  r, c, i, j)) {
					return -1;
				}
			}
		}
	}
	return cnt;
}

int main(void) {
	int t; cin >> t;
	forn(k, t) {
		int r, c;
		cin >> r >> c;
		t_board grid(r, vector<char>(c));
		forn (i, r) {
			forn (j, c) {
				cin >> grid[i][j];
			}
		}
		int ans = solve(grid, r, c);
		if (ans < 0) {
			cout << "Case #" << (k+1) << ": IMPOSSIBLE"<< endl;
		} else {
			cout << "Case #" << (k+1) << ": " << ans << endl;
		}
	}
	return 0;
}
