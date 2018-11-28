// CookieClicker.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>

int main(int argc, char* argv[])
{
	FILE *fp;
	double xSum=0.0, cSum=0.0, fRate=2.0, C, F, X;
	int  tcs=0;

	fp = fopen("c:\\small.in", "r");
	fscanf(fp, "%d", &tcs);

	for (int tc = 0; tc<tcs; tc++)
	{
		fscanf(fp, "%lf %lf %lf", &C, &F, &X);

		while (cSum <= xSum)
		{
			xSum = cSum + (double) X / fRate;
			cSum = cSum + (double) C / fRate;
			fRate += F;

			if (xSum < cSum + X / fRate)
				break;
		}

		printf("Case #%d: %.7f\n", tc+1, xSum);

		cSum = 0.0f;
		xSum = 0.0f;
		fRate = 2.0f;
	}
	fclose (fp);
	return 0;
}
