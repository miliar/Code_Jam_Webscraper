#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	int caMax;
	double c, f, x;

	FILE *fout = fopen("out.txt", "w");
	scanf("%d", &caMax);
	for (int ca = 1; ca <= caMax; ca++)
	{
		scanf("%lf", &c);
		scanf("%lf", &f);
		scanf("%lf", &x);
//		scanf("%lf %lf %lf", &c, &f &x);

		double minTime = -1.0f;
		double ft, mt, lt = 0.0f;
		double cc = 2.0f;

		while (1)
		{
			ft = x / cc + lt;
			if (minTime > ft ||  minTime < 0)
				minTime = ft;

			mt = c / cc;
			lt = lt + mt; 
			cc = cc + f;

			if (lt > minTime)
				break;
		}

		fprintf(fout, "Case #%d: %.7lf\n", ca, minTime);
	}
	fclose(fout);
	return 0;
}