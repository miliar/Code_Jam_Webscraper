#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int n, m, a[105][105];

bool ok(int x, int y)
{
	int i;
	for (i = 0; i < m; i ++)
		if (a[x][i] > a[x][y])
			break;
	if (i >= m)
		return 1;
	for (i = 0; i < n; i ++)
		if (a[i][y] > a[x][y])
			return 0;
	return 1;
}

int main()
{
	int t, cas = 1;
	int i, j, k;
	scanf("%d", &t);
	while (t --)
	{
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; i ++)
			for (j = 0; j < m; j ++)
				scanf("%d", &a[i][j]);
		for (i = 0; i < n; i ++)
		{
			for (j = 0; j < m; j ++)
			{
				if (!ok(i, j))
					break;
			}
			if (j < m)
				break;
		}
		printf("Case #%d: ", cas++);
		if (i < n)
			puts("NO");
		else
			puts("YES");
	}
	return 0;
}
