/*
 * b.cpp
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

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {}

bool isValid(const vector<vector<int> > &grid) {
	int n = grid.size();
	int m = grid[0].size();
	vector<int> row(n, 0);
	vector<int> col(m, 0);
	forn(i, n) forn(j, m) {
		row[i] = max(row[i], grid[i][j]);
		col[j] = max(col[j], grid[i][j]);
	}
	forn(i, n) forn(j, m)
		if (grid[i][j] < row[i] && grid[i][j] < col[j])
			return false;
	return true;
}

int main(void) {
	int t; cin >> t;
	forn(k, t) {
		int n, m; cin >> n >> m;
		vector<vector<int> > grid(n, vector<int> (m));
		forn(i, n) forn(j, m)
			cin >> grid[i][j];
		bool ans = isValid(grid);
		cout << "Case #" << (k+1) << ": " << (ans ? "YES" : "NO") << endl;
	}
	return 0;
}
