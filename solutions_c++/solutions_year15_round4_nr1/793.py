#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <iostream>
#include <algorithm>
#include <deque>
#include <stack>
#include <fstream>
#include <string>
#include <cmath>
#include <climits>
#include <queue>
#include <ctime>
#include <functional>
#include <cstring>
#include <map>
#include <cctype>
#include <unordered_map>

using namespace std;
using pr = pair<int, int>;

pr direct(char ch)
{
	if (ch == '.')
		return { 0, 0 };

	if (ch == '>')
		return { 0, 1 };

	if (ch == '<')
		return { 0, -1 };

	if (ch == '^')
		return { -1, 0 };

	if (ch == 'v')
		return { 1, 0 };
}

int solve(vector<string> a)
{
	auto check = [&a](int i, int j) -> bool
	{
		return 0 <= i && i < a.size() && 0 <= j && j < a[0].size();
	};
	
	int res = 0;
	for (int u = 0; u < a.size(); u++)
	{
		for (int v = 0; v < a[0].size(); v++)
		{
			pr d = direct(a[u][v]);
			if (d != pr{0, 0})
			{
				pr cur = { u + d.first, v + d.second };
				bool ok = false;
				while (check(cur.first, cur.second))
				{
					if (a[cur.first][cur.second] != '.')
					{
						ok = true;
					}
					cur.first += d.first;
					cur.second += d.second;
				}

				if (!ok)
				{
					for (int i = 0; i < a.size(); i++)
					{
						if (a[i][v] != '.' && i != u)
							ok = true;
					}
					for (int i = 0; i < a[0].size(); i++)
					{
						if (a[u][i] != '.' && i != v)
							ok = true;
					}

					if (ok)
						res++;
					else
						return -1;
				}
			}
		}
	}
	return res;
}

int main()
{
	freopen("INPUT.TXT", "r", stdin); freopen("OUTPUT.TXT", "w", stdout);
	int t, r, c;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> r >> c;
		vector<string> a(r);
		for (int u = 0; u < r; u++)
		{
			cin >> a[u];
		}
		
		cout << "Case #" << i + 1 << ": ";
		int res = solve(a);
		if (res == -1)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << res << endl;
		}
	}
}