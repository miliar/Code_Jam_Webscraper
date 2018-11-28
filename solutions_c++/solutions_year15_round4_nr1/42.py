#include <iostream>
#include <cstring>
using namespace std;
const int MAX = 105;
int dir[MAX][MAX];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int n, m;
bool isav(int x, int y)
{
	return (0 <= x && x < n && 0 <= y && y < m);
}
int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int _ = 1; _ <= t; _++)
	{
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				char c;
				cin >> c;
				dir[i][j] = -1;
				if (c == '^')
					dir[i][j] = 0;
				else if (c == '>')
					dir[i][j] = 1;
				else if (c == 'v')
					dir[i][j] = 2;
				else if (c == '<')
					dir[i][j] = 3;
			}
		int ans = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (dir[i][j] != -1)
				{
					int x = i + dx[dir[i][j]], y = j + dy[dir[i][j]];
					while (isav(x, y) && dir[x][y] == -1)
					{
						x += dx[dir[i][j]];
						y += dy[dir[i][j]];
					}
					if (!isav(x, y))
					{
						ans++;
						int cnt = 0;
						for (int x = 0; x < n; x++)
							if (dir[x][j] != -1)
								cnt++;
						for (int y = 0; y < m; y++)
							if (dir[i][y] != -1)
								cnt++;
						if (cnt == 2)
							ans = -10000000;
					}
				}
		if (ans < 0)
			cout << "Case #" << _ << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << _ << ": " << ans << "\n";
	}
	return 0;
}
