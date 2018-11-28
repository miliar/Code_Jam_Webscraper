#include <iostream>
#include <cstring>

using namespace std;

int a, b, c;
char g[100][100];
int vis[100][100];

int dir[8][2] = { { -1, 0 }, { 1, 0 }, { 0, 1 }, { 0, -1 }, { -1, -1 }, { -1, 1 }, { 1, 1 }, { 1, -1 } };

bool expand(int remain, int x, int y)
{
	if (remain == 0)
		return true;
	if (x < 0 || x > a || y < 1 || y > b)
		return false;
	if (g[x][y] == '*')
		return false;
	char h[100][100];
	memcpy(h, g, sizeof g);
	vis[x][y] = 1;
	int cnt = 0;
	for (int i = 0; i < 8; i++)
	{
		int newx = x + dir[i][0];
		int newy = y + dir[i][1];
		if (newx > 0 && newx <= a && newy > 0 && newy <= b)
		{
			if (g[newx][newy] == '*')
			{
				g[newx][newy] = '.';
				cnt++;
			}
		}
	}
	if (cnt == 0)
	{
		vis[x][y] = 0;
		memcpy(g, h, sizeof g);
		return false;
	}
	if (remain >= cnt)
	{
		int newr = remain - cnt;
		for (int i = 1; i <= a; i++)
		{
			for (int j = 0; j <= b; j++)
			{
				if (!vis[i][j] && g[i][j] == '.')
				{
					if (expand(newr, i, j))
						return true;
				}
			}
		}
	}
	vis[x][y] = 0;
	memcpy(g, h, sizeof g);
	return false;
}

int main()
{
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++)
	{
		memset(g, '*', sizeof g);
		memset(vis, 0, sizeof vis);
		cin >> a >> b >> c;
		cout << "Case #" << tt << ":" << endl;
		/*
		if (a == 1)
		{
			cout << 'c';
			for (int i = 0; i < b - c - 1; i++)
				cout << '.';
			for (int i = 0; i < c; i++)
				cout << '*';
			cout << endl;
			continue;
		}
		if (b == 1)
		{
			cout << 'c' << endl;
			for (int i = 0; i < a - c - 1; i++)
				cout << '.' << endl;
			for (int i = 0; i < c; i++)
				cout << '*' << endl;
			continue;
		}
		*/
		int remain = a * b - c - 1;
		int can = false;
		for (int i = 1; i <= a && !can; i++)
		{
			for (int j = 1; j <= b && !can; j++)
			{
				g[i][j] = 'c';
				if (expand(remain, i, j))
				{
					for (int k = 1; k <= a; k++)
					{
						for (int l = 1; l <= b; l++)
						{
							cout << g[k][l];
						}
						cout << endl;
					}
					can = true;
					continue;
				}
				g[i][j] = '*';
			}
		}
		if (!can)
			cout << "Impossible" << endl;
	}
}