#include <bits/stdc++.h>
using namespace std;

const int N = int(1e3);

char Map[N][N];
bool Empty[N][N];
int n, m;

const int dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};

void fill (int x, int y)
{
	if (Empty[x][y]) return;
	Empty[x][y] = 1;
	for (int d = 0; d < 4; ++d)
	{
		int nx = x + dx[d], ny = y + dy[d];
		if (nx >= 0 && nx <= n + 1 && ny >= 0 && ny <= m + 1 && Map[nx][ny] == '.')
		{
			fill(nx, ny);
		}
	}
}

void solve ()
{
	cin >> n >> m;
	for (int i = 1; i <= n; ++i)
	{
		cin >> (Map[i] + 1);
	}
	memset(Empty, 0, sizeof Empty);
	for (int i = 0; i <= n + 1; ++i)
	{
		Map[i][0] = Map[i][m + 1] = '.';
	}
	for (int i = 0; i <= m + 1; ++i)
	{
		Map[0][i] = Map[n + 1][i] = '.';
	}
	fill(0, 0);
	int res = 0;
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
		{
			int prhb[4] = {0, 0, 0, 0}, pcnt = 0;
			for (int d = 0; d < 4; ++d)
			{
				int nx = i + dx[d], ny = j + dy[d];
				if (nx >= 0 && nx <= n + 1 && ny >= 0 && ny <= m + 1 && Empty[nx][ny])
				{
					prhb[d] = 1;
					pcnt ++;
				}
			}
			int dir;
			switch (Map[i][j])
			{
				case '>': dir = 2; break;
				case '<': dir = 3; break;
				case 'v': dir = 0; break;
				case '^': dir = 1; break;
				default: dir = -1; 
			}
			if (pcnt == 4 && dir != -1)
			{
				cout << "IMPOSSIBLE" << endl;
				return;
			}
			res += dir != -1 && prhb[dir];
		}
	cout << res << endl;
}

int main ()
{
	int tk;
	cin >> tk;
	for (int i = 1; i <= tk; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
}
