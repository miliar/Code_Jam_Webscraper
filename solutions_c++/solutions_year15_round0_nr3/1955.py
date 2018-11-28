#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <map>

#define mp make_pair
#define ll long long

using namespace std;

const int maxN = 200000;

bool used[maxN];
bool g[maxN][2][4];

const pair <int, int> pr[4][4] = 
{
	{ mp(0, 0), mp(0, 1), mp(0, 2), mp(0, 3) },
	{ mp(0, 1), mp(1, 0), mp(0, 3), mp(1, 2)},
	{ mp(0, 2), mp(1, 3), mp(1, 0), mp(0, 1) },
	{ mp(0, 3), mp(0, 2), mp(1, 1), mp(1, 0) }
};

map <pair <pair <int, int>, pair <int, int> >, pair <int, int> > ms;

vector <pair <int, int> > v;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	ios_base::sync_with_stdio(0);
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 2; j++)
		{
			for (int ti = 0; ti < 4; ti++)
			{
				for (int tj = 0; tj < 2; tj++)
				{
					pair <int, int>  p1 = mp(j, i);
					pair <int, int>  p2 = mp(tj, ti);
					pair <int, int> ans = pr[i][ti];
					ans.first += j + tj;
					ans.first %= 2;
					ms[mp(p1, p2)] = ans;
				}
			}
		}
	}

	for (int i = 1; i <= t; i++)
	{
		int l, x;
		cin >> l >> x;
		string s;
		string cur;
		cin >> s;
		for (int j = 1; j <= x; j++)
		{
			cur += s;
		}
		v.clear();
		for (int j = 0; j < l * x; j++)
		{
			if (cur[j] == 'i')
			{
				v.push_back(mp(0, 1));
			}
			if (cur[j] == 'j')
			{
				v.push_back(mp(0, 2));
			}
			if (cur[j] == 'k')
			{
				v.push_back(mp(0, 3));
			}
		}
		for (int j = 0; j < 2; j++)
		{
			for (int tj = 0; tj < 4; tj++)
			{
				g[l * x][j][tj] = false;
			}
		}
		for (int pp = l * x - 1; pp >= 0; pp--)
		{
			for (int j = 0; j < 2; j++)
			{
				for (int tj = 0; tj < 4; tj++)
				{
					g[pp][j][tj] = false;
				}
			}
			for (int j = 0; j < 2; j++)
			{
				for (int tj = 0; tj < 4; tj++)
				{
					if (g[pp + 1][j][tj])
					{
						pair <int, int> tmp = ms[mp(v[pp], mp(j, tj))];
						g[pp][tmp.first][tmp.second] = true;
					}
				}
			}
			g[pp][v[pp].first][v[pp].second] = true;
		}

		pair <int, int> up = make_pair(0, 0);
		for (int j = 0; j < l * x; j++)
		{
			up = ms[mp(up, v[j])];
		}
		if (up != mp(1, 0))
		{
			cout << "Case #" << i << ": NO" << "\n";
			continue;
		}
		up = mp(0, 0);
		bool f = false;
		for (int j = 0; j <= l * x - 3; j++)
		{
			up = ms[mp(up, v[j])];
			if (up != mp(0, 1))
			{
				continue;
			}
			if (g[j + 1][0][2])
			{
				f = true;
				break;
			}
		}
		if (f)
		{
			cout << "Case #" << i << ": YES" << "\n";
		}
		else
		{
			cout << "Case #" << i << ": NO" << "\n";
		}
	}

	return 0;
}