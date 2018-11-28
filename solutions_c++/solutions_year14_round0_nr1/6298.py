#include <iostream>
#include <cstdio>
#include <algorithm>


using namespace std;

int t, n, x, y, i, j, exists, q, tt;
int a[10][10], b[10][10];

int main()
{


	cin >> t;

	n = 4;

	for (tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d", &x);
		for (i = 1; i <= n; i++)
			for (j = 1; j <= n; j++)
				scanf("%d", &a[i][j]);
		
		scanf("%d", &y);
		for (i = 1; i <= n; i++)
			for (j = 1; j <= n; j++)
				scanf("%d", &b[i][j]);
		
		exists = 0;
		for (i = 1; i <= n; i++)
			for (j = 1; j <= n; j++)
				if (a[x][i] == b[y][j])
					exists++, q = a[x][i];
		
		if (exists == 1)
			printf("%d\n", q);
		else
		if (exists >= 2)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}
	return 0;			                         
}
