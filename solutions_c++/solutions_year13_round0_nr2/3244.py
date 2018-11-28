#include <stdio.h>
#include <string.h>

bool judge(const int a[100][100], int n, int m)
{
	static int rmax[100];
	static int cmax[100];
	int i, j;

	for (i = 0; i < n; ++i)
		{
		rmax[i] = -1;
		for (j = 0; j < m; ++j)
			{
			if (rmax[i] < a[i][j])
				{
				rmax[i] = a[i][j];
				}//end if
			}//end for
		}//end for

	for (j = 0; j < m; ++j)
		{
		cmax[j] = -1;
		for (i = 0; i < n; ++i)
			{
			if (cmax[j] < a[i][j])
				{
				cmax[j] = a[i][j];
				}//end if
			}//end for
		}//end for

	for (i = 0; i < n; ++i)
		{
		for (j = 0; j < m; ++j)
			{
			if (a[i][j] < rmax[i] && a[i][j] < cmax[j])
				{
				return false;
				}//end if
			}//end for
		}//end for

	return true;
}//end judge

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int a[100][100];
	int t;
	int c, n, m;
	int i, j;

	scanf("%d", &t);
	for (c = 1; c <= t; ++c)
		{
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; ++i)
			{
			for (j = 0; j < m; ++j)
				{
				scanf("%d", &a[i][j]);
				}//end for
			}//end for
		printf("Case #%d: %s\n", c, judge(a, n, m) ? "YES" : "NO");
		}//end for
	
	return 0;
}//end main
