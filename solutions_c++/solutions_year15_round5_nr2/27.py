#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

const int INF = 1000000000;

typedef long long s64;

const int MaxN = 1000000;

int n, nk;
int a[MaxN], s[MaxN], ds[MaxN];

int main()
{
	int nT;
	cin >> nT;

	for (int nt = 1; nt <= nT; nt++)
	{
		scanf("%d %d", &n, &nk);
		for (int i = 0; i <= n - nk; i++)
			scanf("%d", &s[i]);
		for (int i = 0; i + 1 <= n - nk; i++)
			ds[i] = s[i + 1] - s[i];

		static int smin[MaxN];
		static int smax[MaxN];
		for (int i = 0; i < nk; i++)
		{
			int scur = 0;
			smin[i] = smax[i] = 0;
			for (int k = i; k < n - nk; k += nk)
			{
				scur += ds[k];
				smin[i] = min(smin[i], scur);
				smax[i] = max(smax[i], scur);
			}
		}
		int resL = s[0];
		for (int i = 0; i < nk; i++)
			resL += smin[i];
		resL = (int)floor((long double)resL / nk);

		int resR = s[0];
		for (int i = 0; i < nk; i++)
			resR += smax[i];
		resR = (int)ceil((long double)resR / nk);

		int res = resR - resL;
		for (int i = 0; i < nk; i++)
		{
			int d = smax[i] - smin[i];
			if (d > res)
				res = d;
		}

		printf("Case #%d: %d\n", nt, res);
	}

	return 0;
}
