#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int s[105][105];
int h[105][2];//0-row, 1-col
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int t=1; t<=cas; t++)
	{
		memset(s, 0, sizeof(s));
		memset(h, 0, sizeof(h));
		int m, n;
		scanf("%d %d", &n, &m);
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<m; j++)
			{
				scanf("%d", &s[i][j]);
				h[i][0] = max(h[i][0], s[i][j]);
				h[j][1] = max(h[j][1], s[i][j]);
			}
		}
		bool flag = true;
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<m; j++)
			{
				if (s[i][j]!=h[i][0] && s[i][j]!=h[j][1])
				{
					flag = false;
					break;
				}
			}
		}
		printf("Case #%d: %s\n", t, flag?"YES":"NO");
	}
	return 0;
}