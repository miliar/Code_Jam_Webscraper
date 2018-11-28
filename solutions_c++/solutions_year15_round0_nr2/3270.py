#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <algorithm>
using namespace std;

int main(void)
{
	freopen("data.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int nT = 1; nT <= T; ++nT)
	{
		int D;
		int P;
		int ans[2000] = {0};
		scanf("%d", &D);
		for (int i = 0; i < D; ++i)
		{
			scanf("%d", &P);
			for (int j = 1; j <= P; ++j)
			{
				if (P % j == 0)
					ans[j] += P/j-1;
				else
					ans[j] += P/j;
			}
		}
		int ansans = 10000;
		for (int i = 1; i < 2000; ++i)
			if (i + ans[i] < ansans)
				ansans = i + ans[i];
		printf("Case #%d: %d\n", nT, ansans);
	}
}