#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

const int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};
const int N = 123;
string a[N];

#undef int
int main()
{
#define int long long
	int t; cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cerr << "Executing Case #" << tt << "\n";

		int n, m; cin >> n >> m;
		for (int i = 0; i < n; i++) cin >> a[i];

		int ret = 0;
		for (int i = 0; i < n and ret >= 0; i++)
			for (int j = 0; j < m; j++)
				if (a[i][j] != '.')
				{
					int cur = 0;
					for (int k = 0; k < 4; k++)
					{
						int x = i, y = j;
						bool seen = false;
						while (true)
						{
							x += dx[k];
							y += dy[k];
							if (x < 0 or x >= n or y < 0 or y >= m) break;
							if (a[x][y] != '.') seen = true;
						}
						if (!seen) cur++;
					}

					if (cur == 4)
					{
						ret = -1;
						break;
					}
					else if (cur != 0)
					{
						int cx, cy;
						if (a[i][j] == '^') cx = -1, cy = 0;
						if (a[i][j] == '>') cx = 0, cy = 1;
						if (a[i][j] == 'v') cx = 1, cy = 0;
						if (a[i][j] == '<') cx = 0, cy = -1;
						int x = i, y = j;
						bool seen = false;
						while (true)
						{
							x += cx;
							y += cy;
							if (x < 0 or x >= n or y < 0 or y >= m) break;
							if (a[x][y] != '.') seen = true;
						}
						if (!seen) ret++;
					}
				}

		cout << "Case #" << tt << ": ";
		if (ret < 0) cout << "IMPOSSIBLE\n";
		else cout << ret << "\n";
	}
	return 0;
}