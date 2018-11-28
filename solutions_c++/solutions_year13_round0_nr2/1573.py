#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

int arr[100][100], rowMax[100], colMax[100];
int t, n, m, i, j, k;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    
    cin >> t;
    
    for (i = 1; i <= t; i++)
    {
		scanf("%d %d", &n, &m);

		for (int j = 0; j < 100; j++)
		{
			rowMax[j] = colMax[j] = 1;
		}

		for (j = 0; j < n; j++)
		{
			for (k = 0; k < m; k++)
			{
				scanf("%d", &arr[j][k]);
			}
		}

		for (j = 0; j < n; j++)
		{
			for (k = 0; k < m; k++)
			{
				rowMax[j] = max(rowMax[j], arr[j][k]);
				colMax[k] = max(colMax[k], arr[j][k]);
			}
		}

		bool ok = true;

		for (j = 0; j < n && ok; j++)
		{
			for (k = 0; k < m && ok; k++)
			{
				if (arr[j][k] >= rowMax[j] || arr[j][k] >= colMax[k]);
				else ok = false;
			}
		}

		if (ok)
		{
			printf("Case #%d: YES\n", i);
		}
		else
		{
			printf("Case #%d: NO\n", i);		
		}

	}  
	return 0;
}
