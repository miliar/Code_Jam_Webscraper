#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <math.h>
#include <memory.h>



int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		long long N, P;
		scanf("%lld%lld", &N, &P);
		long long have, may;
		long long NN = 1LL << N;
		if (P == NN)
		{
			may = P - 1;
			have = P - 1;
		}
		else
		{
			have = 2;
			long long pp = P;
			while (P * 2 > NN)
			{
				have *= 2;
				NN /= 2;
				P -= NN;
			}
			have -= 2;
			NN = 1LL << N;
			
			P = pp;
			may = 2;
			while (P * 2 < NN)
			{
				NN /= 2;
				may *= 2;
			}
			NN = 1LL << N;
			may = NN - may;

		}
		printf("Case #%d: %lld %lld\n", t+1, have, may);
	}

	return 0;
}