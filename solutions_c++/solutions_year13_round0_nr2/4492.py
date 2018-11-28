#include <stdio.h>
#include <algorithm>
int land[100][100], origin[100][100], n, m;
int main()
{
	int t;
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++)
	{
		scanf("%d %d", &n, &m);
		bool flag = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				scanf("%d", &land[i][j]);
				origin[i][j] = 100;
			}
		for (int i = 0; i < n; i++)
		{
			int _max = 0;
			for (int j = 0; j < m; j++)
				_max = std::max(_max, land[i][j]);
			for (int j = 0; j < m; j++)
				origin[i][j] = std::min(origin[i][j], _max);
		}
		for (int i = 0; i < m; i++)
		{
			int _max = 0;
			for (int j = 0; j < n; j++)
				_max = std::max(_max, land[j][i]);
			for (int j = 0; j < n; j++)
				origin[j][i] = std::min(origin[j][i], _max);
		}
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (land[i][j] != origin[i][j]) flag = false;
		printf("Case #%d: %s\n", cases, (flag) ? "YES" : "NO");
	}
}