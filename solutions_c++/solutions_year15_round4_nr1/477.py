#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;
typedef long long ll;
const double eps = 1e-9;
const int mod = 1e9 + 7;


int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };


int main(){
	freopen("A-large (5).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{

		int n, m;
		cin >> n >> m;
		vector<string> v(n);
		getchar();
		for (int i = 0; i<n; ++i)
		{
			//cin >> v[i];
			getline(cin, v[i]);
		}

		set<pair<int, int> > in, leave;

		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				if (v[i][j] == '.')
					continue;
				int go = -1;
				if (v[i][j] == '>')
					go = 0;
				if (v[i][j] == '<')
					go = 1;
				if (v[i][j] == '^')
					go = 2;
				if (v[i][j] == 'v')
					go = 3;

				int x = i, y = j;
				while (1)
				{
					x += dx[go];
					y += dy[go];
					if (x < 0 || y < 0 || x >= n || y >= m)
					{
						leave.insert(make_pair(i, j));
						break;
					}
					if (v[x][y] != '.')
					{
						in.insert(make_pair(x, y));
						break;
					}
				}
			}
		}
		int ans = leave.size();
		bool wrong = false;
		for (auto it = leave.begin(); it != leave.end(); ++it)
		{
			bool good = false;
			int x = it->first, y = it->second;

			for (int i = 0; i < n; ++i)
			{
				if (i != x && v[i][y] != '.')
				{
					good = true;
					break;
				}
			}
			for (int j = 0; j < m; ++j)
			{
				if (j != y && v[x][j] != '.')
				{
					good = true;
					break;
				}
			}

			if (!good)
			{
				wrong = true;
				break;
			}
		}

		if (wrong)
		{
			cout << "Case #" << t << ": Impossible\n";
		}
		else
			cout << "Case #" << t << ": " << ans<<"\n";

	}


	return 0;
}
/*
4
2 2
^>
^>
2 2
>v
^<
3 3
...
.^.
...
1 1
.

*/