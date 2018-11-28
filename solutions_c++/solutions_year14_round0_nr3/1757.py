#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

inline int Abs(int x)
{
	return x < 0 ? -x : x;
}

void solve(int r, int c, int m)
{
	if (m == r * c - 1)
	{
		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				if (i == 0 && j == 0)
					cout << "c";
				else
					cout << "*";
			}
			cout << endl;
		}
		return;
	}

	vector <pair <int, int>> t;
	for (int mask = 0; mask < (1 << (r * c - 1)); mask++)
	{
		int bits = 0;
		for (int i = 0; i < r * c; i++)
			if ((1 << i) & mask)
				bits++;
		if (bits != m)
			continue;
		int nmask = mask;
		int ar, ac;
		t.clear();
		for (int i = 0; i < r * c; i++)
		{
			if ((1 << i) & mask)
				continue;
			int rc = i / c;
			int cc = i % c;
			int cur_mask = nmask;
			bool ok = true;
			for (int dr = -1; dr <= 1 && ok; dr++)
			{
				if (rc + dr < 0 || rc + dr >= r)
					continue;
				for (int dc = -1; dc <= 1 && ok; dc++)
				{
					int nr = rc + dr;
					int nc = cc + dc;
					if (nc < 0 || nc >= c)
						continue;
					int bit = nr * c + nc;
					if ((1 << bit) & mask)
					{
						ok = false;
						break;
					}
					cur_mask |= (1 << bit);
				}
			}
			if (ok)
			{
				ok = false;
				if (t.empty())
					ok = true;
				for (int i = 0; i < t.size() && !ok; i++)
					if (Abs(rc - t[i].first) <= 1 && Abs(cc - t[i].second) <= 1)
					{
						ok = true;
						break;
					}
				if (ok)
				{
					nmask = cur_mask;
					ar = rc;
					ac = cc;
					t.push_back(make_pair(rc, cc));
				}
			}
		}
		if (nmask == (1 << (r * c)) - 1)
		{
			vector <vector <char>> ans(r, vector <char>(c));
			for (int i = 0; i < r * c; i++)
			{
				int rc = i / c;
				int cc = i % c;
				if (mask & (1 << i))
					ans[rc][cc] = '*';
				else if (rc == ar && cc == ac)
					ans[rc][cc] = 'c';
				else
					ans[rc][cc] = '.';
			}
			for (int i = 0; i < r; i++)
			{
				for (int j = 0; j < c; j++)
					cout << ans[i][j];
				cout << endl;
			}

			return;
		}
	}

	cout << "Impossible" << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 0; t < tc; t++)
	{
		int r, c, m;
		cin >> r >> c >> m;
		printf("Case #%d:\n", t + 1);
		solve(r, c, m);
	}
}