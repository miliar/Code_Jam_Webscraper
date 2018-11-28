#include <bits/stdc++.h>
using namespace std;

/*
*/

long long ind(int k, int c, int x, int y)
{
	long long r = x;
	for (int i = 1; i < c; i++)
		r *= k;
	r += y;
	return r;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; z++)
	{
		int n, k, s;
		scanf("%d %d %d", &n, &k, &s);
		if (k == 1)
		{
			if (s < n)
			{
				printf("Case #%d: IMPOSSIBLE\n", z);
			}
			else
			{
				printf("Case #%d:", z);
				for (int i = 0; i < n; i++)
					printf(" %d", i+1);
				printf("\n");
			}
		}
		else
		{
			int should = (n+1) / 2;
			if (should <= s)
			{
				printf("Case #%d:", z);
				for (int i = 0; i < (n+1)/2; i++)
					printf(" %lld", ind(n, k, i, n-i));
				printf("\n");
			}
			else
			{
				printf("Case #%d: IMPOSSIBLE\n", z);
			}
		}
	}
}