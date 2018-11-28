#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <queue>
using namespace std;
long long  t, tt, B, M, mm[10][10];
int main() {
	freopen("B-small-attempt6.in", "r", stdin);
	freopen("Bsmall.out", "w", stdout);
	scanf("%lld", &t);
	for (tt = 1; tt <= t; tt++)
	{

		memset(mm, 0, sizeof(mm));
		printf("Case #%lld:", tt);
		scanf("%lld%lld", &B, &M);
		long long mx = 1 << (B - 2);
		if (M>mx)
		printf(" IMPOSSIBLE\n");
		else
		{
			for (int i = 0; i < B - 1; i++)
				for (int j = i + 1; j < B - 1; j++)
					mm[i][j] = 1;
			if (M == mx)for (int i = 0; i < B -1; i++) mm[i][B-1] = 1;
			else
			{
				for (int i = 1; i < B - 1; i++)
				{
					if (M%2) mm[i][B-1] = 1;
					M /= 2;
				}
			}
			printf(" POSSIBLE\n");
			for (int i = 0; i < B; i++)
			{
				for (int j = 0; j < B; j++)
					printf("%lld", mm[i][j]);
				printf("\n");
			}

		}
	}
	return 0;
}