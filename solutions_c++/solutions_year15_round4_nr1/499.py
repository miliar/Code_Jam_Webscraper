#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;

char s[105][105];
int n, m;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%s", s[i]);

		int ans = 0;
		bool bad = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				if (s[i][j] != '.')
				{
					bool fo[4] = {0,0,0,0};
					for (int k = i + 1; k < n; k++)
					{
						if (s[k][j] != '.')
							fo[0] = 1;
					}
					for (int k = i - 1; k >= 0; k--)
					{
						if (s[k][j] != '.')
							fo[1] = 1;
					}
					for (int k = j + 1; k < m; k++)
					{
						if (s[i][k] != '.')
							fo[2] = 1;
					}
					for (int k = j - 1; k >= 0; k--)
					{
						if (s[i][k] != '.')
							fo[3] = 1;
					}
					int sum = 0;
					for (int i = 0; i < 4; i++)
						sum += fo[i];
					if (sum == 0)
						bad = 1;


					if (s[i][j] == '<' && fo[3])
						ans--;
					else if (s[i][j] == '>' && fo[2])
						ans--;
					else if (s[i][j] == '^' && fo[1])
						ans--;
					else if (s[i][j] == 'v' && fo[0])
						ans--;
					ans++;
				}
			}
		}
		printf("Case #%d: ", tt + 1);
		if (bad)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}


	return 0;
}