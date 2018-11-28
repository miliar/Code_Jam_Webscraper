#include <iostream>

using namespace std;

const int MAXN = 110;

char a[MAXN][MAXN];
bool marked[MAXN][MAXN];
int cnt[MAXN][MAXN];

int n, m;
typedef pair<int, int> pii;

pii getFirst(int nx, int ny, int dx, int dy)
{
	while (nx >= 0 && nx < n && ny >= 0 && ny < m && a[nx][ny] == '.')
		nx += dx, ny += dy;
	return pii(nx, ny);
}

int main()
{
	int tt;
	cin >> tt;
	for (int tc = 1; tc <= tt; tc++)
	{
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				cin >> a[i][j];
				marked[i][j] = false;
				cnt[i][j] = 0;
			}
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			int ny = getFirst(i, 0, 0, 1).second;
			if (ny != m)
			{
				cnt[i][ny]++;
				if (a[i][ny] == '<')
					ans++;
			}
			ny = getFirst(i, m - 1, 0, -1).second;
			if (ny != -1)
			{
				cnt[i][ny]++;
				if (a[i][ny] == '>')
					ans++;
			}
		}
		for (int i = 0; i < m; i++)
		{
			int nx = getFirst(0, i, 1, 0).first;
			if (nx != n)
			{
				cnt[nx][i]++;
				if (a[nx][i] == '^')
					ans++;
			}
			nx = getFirst(n - 1, i, -1, 0).first;
			if (nx != -1)
			{
				cnt[nx][i]++;
				if (a[nx][i] == 'v')
					ans++;
			}
		}
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (cnt[i][j] == 4)
					ans = -1;
		if (ans == -1)
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << tc << ": " << ans << endl;
	}
}
