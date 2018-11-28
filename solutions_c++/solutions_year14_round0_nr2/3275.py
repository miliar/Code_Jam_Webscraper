#include "stdafx.h"

int _tmain(int argc, _TCHAR* argv[])
{
	double F, C, X;
	double time = 0.0;
	int T;
	int i, j, k;
	scanf("%d", &T);

	double totX = 0, totC= 0;
	double cps = 2.0;

	for (int tc = 0; tc < T; tc++)
	{
		scanf( "%lf %lf %lf", &C, &F, &X);

		while (totC <= totX)
		{
			totX = totC+ (double) X / cps;
			totC= totC+ (double) C / cps;
			cps += F;

			if (totX < totC+ X / cps)
				break;
		}
		printf("Case #%d: %.7lf\n", tc+1, totX);

		totC= 0.0f;
		totX = 0.0f;
		cps = 2.0f;
	}
	return 0;
}