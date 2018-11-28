#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

bool isimp(vector<string> &mtr, int n, int m, int x, int y)
{
	for (int i=0; i<n; i++)
		if (i != x && mtr[i][y] != '.')
			return false;
	for (int i=0; i<m; i++)
		if (i != y && mtr[x][i] != '.')
			return false;
	return true;
}

bool safe(vector<string> &mtr, int n, int m, int x, int y)
{
	int dx = 0, dy = 0;
	switch(mtr[x][y])
	{
	case '^': dx = -1; break;
	case 'v': dx = 1; break;
	case '<': dy = -1; break;
	case '>': dy = 1; break;
	}

	x += dx;
	y += dy;
	while (x >= 0 && x < n && y >= 0 && y < m)
	{
		if (mtr[x][y] != '.')
			return true;
		x += dx;
		y += dy;
	}
	return false;
}

int main()
{
	int cn; cin >> cn;
	for (int cc=1; cc<=cn; cc++)
	{
		int n, m; cin >> n >> m;
		vector<string> mtr(n);
		for (int i=0; i<n; i++)
			cin >> mtr[i];

		int cnt = 0;
		bool imp = false;
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
				if (mtr[i][j] != '.')
				{
					if (safe(mtr, n, m, i, j))
						continue;
					if (isimp(mtr, n, m, i, j))
						imp = true;
					cnt++;
				}
		
		cout << "Case #" << cc << ": ";
		if (imp)
			cout << "IMPOSSIBLE";
		else
			cout << cnt;
		cout << endl;
	}
	return 0;
}
