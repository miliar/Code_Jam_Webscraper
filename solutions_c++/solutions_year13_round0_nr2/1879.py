#include <cstdio>
#include <algorithm>

using namespace std;


int t, n, m, a[101][101], m1[101], m2[101], boo;

int main()
{
	freopen("lawnmover.in", "r", stdin);
	freopen("lawnmover.out", "w", stdout);
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		boo = 0;
		printf("Case #%d: ", q + 1);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			m1[i] = 0;
		for (int i = 0; i < m; i++)
			m2[i] = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j<  m; j++)
			{
				scanf("%d", &a[i][j]);
				m1[i] = max(m1[i], a[i][j]);
				m2[j] = max(m2[j], a[i][j]);
			}
		for (int i = 0; i < n && !boo; i++)
			for (int j = 0; j < m; j++)
				if (m1[i] > a[i][j] && m2[j] > a[i][j])
				{
					//printf("%d %d\n", i + 1, j + 1);
					boo = 1;
					break;
				}
		if (boo)
			puts("NO");
		else
			puts("YES");
	}
}