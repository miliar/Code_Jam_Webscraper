// ConsoleApplication3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <iostream>
#include <string>
#include <cassert>
#include <sstream>

using namespace std;

int dx[] = { -1, 1, 0, 0 }, dy[] = { 0, 0, -1, 1 };

void solve()
{
	int r, c, n; cin >> r >> c >> n;
	int best = 99999999;
	for (int m = 0; m < (1 << (r * c)); ++m) {
		int msk = m;
		int cnt = 0;
		int cand = 0;
		int t[18][18];
		for (int i = 0; i <= r + 1; ++i) for (int j = 0; j <= c + 1; ++j) t[i][j] = 0;
		for (int a = 1; a <= r; ++a)
			for (int b = 1; b <= c; ++b) {
				t[a][b] = msk & 1;
				cnt += t[a][b];
				msk >>= 1;
				if (t[a][b]) for (int i = 0; i < 4; ++i) {
					int x = a + dx[i], y = b + dy[i];
					if (t[x][y])
					++cand;
				}
			}
		if (cnt == n)
			best = min(best, cand);
	}
	cout << best;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t; cin >> t;
	for (auto q = 1; q <= t; ++q) {
		cout << "Case #" << q << ": ";
		solve();
		cout << endl;
	}
	return 0;
}

