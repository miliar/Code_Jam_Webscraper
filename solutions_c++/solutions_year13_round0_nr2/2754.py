#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
#define mp make_pair
#define sqr(x) ((x)*(x))
const double PI = 3.1415926535;

int t, n, m;
int d[110][110], col[110], row[110];

int main()
{
#ifdef MYLOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	
	cin >> t;
	for (int cnt = 0; cnt < t; ++cnt)
	{
		cout << "Case #" << cnt+1 << ": ";
		cin >> n >> m;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				cin >> d[i][j];
		for (int i = 0; i < n; ++i)
		{
			row[i] = 0;
			for (int j = 0; j < m; ++j)
				row[i] = max(row[i], d[i][j]);
		}
		for (int j = 0; j < m; ++j)
		{
			col[j] = 0;
			for (int i = 0; i < n; ++i)
				col[j] = max(col[j], d[i][j]);
		}
		bool check = false;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (d[i][j] < row[i] && d[i][j] < col[j])
					check = true;
		cout << (check ? "NO\n" : "YES\n");
	}

	return 0;
}