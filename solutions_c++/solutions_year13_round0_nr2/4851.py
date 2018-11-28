#include <iostream>
#include <cstdio>
#include <memory.h>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	int t = 0;
	while (t < T)
	{
		t++;
		int n, m;
		scanf("%d%d", &n, &m);
		int map[200][200];
		memset(map, 0, sizeof(map));
		for (int i = 0; i < n; i ++)
		for (int j = 0; j < m; j ++)
		{
			scanf("%d", &map[i][j]);
		}
		int row[200];
		int col[200];
		memset(row, 0 ,sizeof(row));
		memset(col, 0, sizeof(col));

		int flag = 0;
		while (1)
		{
			int max = -1;
			for (int i = 0; i < n; i ++)
			for (int j = 0; j < m; j ++)
			{
				if (map[i][j] > 0 && map[i][j] > max)
				{
					max = map[i][j];
				}
			}

			if (max == -1)
			{
				break;
			}
			// cout << "max: "	 << max << endl;
			// make not movable

			for (int i = 0; i < n && !flag; i ++)
			for (int j = 0; j < m && !flag; j ++)
			{
				if (map[i][j] == max)
				{
					if (row[i] && col[j])
					{
						flag = 1;
					}
				}
			}
			if (flag)
			{
				break;
			}

			for (int i = 0; i < n; i ++)
			for (int j = 0; j < m; j ++)
			{
				if (map[i][j] == max)
				{
					map[i][j] = -1;
					row[i] = 1;
					col[j] = 1;
				}
			}

		}
		if (flag)
		{
			printf("Case #%d: NO\n", t);
		}
		else
		{
			printf("Case #%d: YES\n", t);
		}

	}
}
