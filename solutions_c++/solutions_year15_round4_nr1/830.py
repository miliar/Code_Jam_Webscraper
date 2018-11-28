#include <bits/stdc++.h>

using namespace std;

int T;
int h, w;
char grid[120][120];

int main()
{
	cin >> T;
	for (int C = 1; C <= T; C++)
	{
		cin >> h >> w;
		vector<int> row[120], col[120];
		for (int r = 0; r < h; r++)
		for (int c = 0; c < w; c++)
		{
			char cur;
			cin >> cur;
			grid[r][c] = cur;
			if (cur != '.')
			{
				row[r].push_back(c);
				col[c].push_back(r);
			}
		}
		int ans = 0;
		for (int r = 0; r < h && ans != -1; r++)
		for (int c = 0; c < w && ans != -1; c++)
		{
			if (grid[r][c] == '<')
			{
				if (row[r].size() == 1 && col[c].size() == 1) ans = -1;
				else if (row[r][0] == c) ans++;
			}
			if (grid[r][c] == '>')
			{
				if (row[r].size() == 1 && col[c].size() == 1) ans = -1;
				else if (*row[r].rbegin() == c) ans++;
			}
			if (grid[r][c] == '^')
			{
				if (col[c].size() == 1 && row[r].size() == 1) ans = -1;
				else if (col[c][0] == r) ans++;
			}
			if (grid[r][c] == 'v')
			{
				if (col[c].size() == 1 && row[r].size() == 1) ans = -1;
				else if (*col[c].rbegin() == r) ans++;
			}
		}
		cout << "Case #" << C << ": ";
		if (ans == -1)
			cout << "IMPOSSIBLE\n";
		else cout << ans << '\n';
	}
	return 0;
}

