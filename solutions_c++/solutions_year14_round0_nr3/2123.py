#include <cstdio>
#include <iostream>
using namespace std;

int n, m, clear;
bool flag = false;
int a[13];
bool used[13][13];
int count;
int matrix[13][13];
char ans[13][13];
int answerA[13];

void click(int x, int y)
{
	if (x < 0 || x == n || y < 0 || y == m || used[x][y])
		return;
	used[x][y] = true;
	++count;
	if (matrix[x][y] == 0)
	{
		for (int dx = -1; dx < 2; dx++)
			for (int dy = -1; dy < 2; dy++)
				click(x + dx, y + dy);
	}
}

bool check()
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			matrix[i][j] = -1;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < a[i]; j++)
			matrix[i][j] = 0;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (matrix[i][j] == 0)
			{
				for (int dx = -1; dx < 2; dx++)
					for (int dy = -1; dy < 2; dy++)
					{
						int x = i + dx;
						int y = j + dy;
						if (x < 0 || x == n || y < 0 || y == m)
							continue;

						if (matrix[x][y] == -1)
							++matrix[i][j];
					}
			}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			used[i][j] = false;

	count = 0;
	click(0, 0);
	return count == clear;
}

void rec(int clear, int row)
{
	if (clear == 0 && check())
	{
		flag = true;
		for (int i = 0; i < 13; i++)
			answerA[i] = a[i];
	}

	if (row == n || flag)
		return;

	for (int i = 1; i <= clear; i++)
	{
		a[row] = i;
		rec(clear - i, row + 1);
		a[row] = 0;
	}
}

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++)
	{
		int b;
		cin >> n >> m >> b;
		clear = n * m - b;
		flag = false;
		for (int i = 0; i < 13; i++)
			answerA[i] = 0;

		rec(clear, 0);
		cout << "Case #" << test << ":\n";
		if (!flag)
		{
			cout << "Impossible\n";
			continue;
		}
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				ans[i][j] = '*';

		for (int i = 0; i < n; i++)
			for (int j = 0; j < answerA[i]; j++)
				ans[i][j] = '.';

		ans[0][0] = 'c';
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
				cout << ans[i][j];
			cout << endl;
		}

	}
	return 0;
}
