#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <utility>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <math.h>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <list>
#include <sstream>
#include <time.h>
#include <stdlib.h>
#include <ctype.h>

#define print(Z,a,b) for (int __z = a; __z < b; __z ++) cout << Z[__z] << " ";
#define scan(Z,a,b) for (int __z = a; __z < b; __z ++) cin >> Z[__z];
#define bit(_z) (1ll << (_z))
#define rep(__z,__Z) for(int __z = 0; __z < __Z ; __z++ )
#define all(__z) __z.begin(),__z.end()

#define par pair<int, int>
#define p1 first
#define p2 second

#define eps = 1e-6

using namespace std;

int r, c;
char M[200][200];
int ans = 0;

int walk(int y, int x, int dy, int dx)
{
	bool first = true;
	while (first || (y < r and y >= 0 and x < c and x >= 0 and M[y][x] == '.'))
	{
		y += dy;
		x += dx;
		first = false;
	}
	if (y < r and y >= 0 and x < c and x >= 0)
		return 0;
	return 1;
}

int possible()
{
	for (int i = 0; i < r; i ++)
	{
		for (int j = 0; j < c; j ++)
		{
			int cnt = 0;
			for (int i2 = 0; i2 < r; i2 ++)
				if (M[i2][j] != '.')
					cnt ++;
			for (int j2 = 0; j2 < c; j2 ++)
				if (M[i][j2] != '.')
					cnt ++;
			if (cnt == 2 and M[i][j] != '.')
				return 0;
		}
	}
	return 1;
}

int main()
{
	int t;
	cin >> t;
	int caze = 0;
	while (t --)
	{
		ans = 0;
		caze ++;
		cin >> r >> c;
		for (int i = 0; i < r; i ++)
		{
			cin >> M[i];
		}

		for (int i = 0; i < r; i ++)
		{
			for (int j = 0; j < c; j ++)
			{
				if (M[i][j] == '^')
					ans += walk(i, j, -1, 0);
				if (M[i][j] == '>')
					ans += walk(i, j, 0, 1);
				if (M[i][j] == 'v')
					ans += walk(i, j, 1, 0);
				if (M[i][j] == '<')
					ans += walk(i, j, 0, -1);
			}
		}

		if (possible())
			cout << "Case #" << caze << ": " << ans << endl;
		else
			cout << "Case #" << caze << ": IMPOSSIBLE" << endl;
	}
		
	return 0;
}


