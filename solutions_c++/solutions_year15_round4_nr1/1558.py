#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char graph[105][105];
int main()
{
	int ncase;

	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	cin >> ncase;

	for(int icase = 1;icase <= ncase;icase++)
	{
		int r, c;
		cin >> r >> c;
		for(int i = 0;i < r;i++)
			cin >> graph[i];
		
		int res = 0;
		int rowOne[105], colOne[105];
		memset(rowOne, 0, sizeof(rowOne));
		memset(colOne, 0, sizeof(colOne));
		for(int i = 0;i < r;i++)
		{
			int sum = 0;
			for(int j = 0;j < c;j++)
				sum += graph[i][j] != '.';
			rowOne[i] = (sum == 1);
		}

		for(int i = 0;i < c;i++)
		{
			int sum = 0;
			for(int j = 0;j < r;j++)
				sum += graph[j][i] != '.';
			colOne[i] = (sum == 1);
		}

		for(int i = 0;i < r;i++)
			for(int j = 0;j < c;j++)
			{
				if (rowOne[i] && colOne[j] && graph[i][j] != '.')
					res = -1;
			}

		if (res == -1)
		{
			cout << "Case #" << icase << ": IMPOSSIBLE" << endl;
			continue;
		}
		
		for(int i = 0;i < r;i++)
		{
			for(int j = 0;j < c;j++)
				if (graph[i][j] != '.')
				{
					res += graph[i][j] == '<';
					break;
				}

			for(int j = c - 1;j >= 0;j--)
				if (graph[i][j] != '.')
				{
					res += graph[i][j] == '>';
					break;
				}
		}

		for(int i = 0;i < c;i++)
		{
			for(int j = 0;j < r;j++)
				if (graph[j][i] != '.')
				{
					res += graph[j][i] == '^';
					break;
				}

			for(int j = r - 1;j >= 0;j--)
				if (graph[j][i] != '.')
				{
					res += graph[j][i] == 'v';
					break;
				}
		}
		cout << "Case #" << icase << ": " << res << endl;
	}

	return 0;
}
