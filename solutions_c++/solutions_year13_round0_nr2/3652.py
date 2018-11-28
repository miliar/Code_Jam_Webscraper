#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;


	int t, n, m, i;

	int a[100][100];

	int r[100], c[100];

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);

	cin >> t;

	for	( i = 0; i < t; i++ )
	{
		scanf("%d %d", &n, &m );
		for (int j = 0; j < 100; j++) r[j] = c[j] = 0; 
		for ( int j = 0; j < n; j++ )
		{
			for ( int k = 0; k < m; k++ )
			{
				scanf("%d", &a[j][k]);
				r[j] = max(a[j][k], r[j]);
				c[k] = max(a[j][k], c[k]);
			}
		}
		bool ok = true;
		for (int j = 0; j < n && ok; j++)
		{
			for (int k = 0; k < m && ok; k++)
				ok = !(a[j][k] < r[j] && a[j][k] < c[k]);
		}
		printf("Case #%d: ", i + 1);
		if (!ok)
			printf("NO\n");
		else
			printf("YES\n");
	}

	return 0;
}