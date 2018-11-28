// cookie.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int T = 0;
	double C = 0.0;
	double F = 0.0;
	double X = 0.0;
	double fSumC = 0.0;
	double fSumX = 0.0;
	double fCPS = 2.0;

	FILE* fpin = fopen("C:\\GCJ\\B-large.in", "r");
	FILE* fpout = fopen("C:\\GCJ\\B-large.out", "w");

	if(NULL == fpin || NULL == fpout )
		return 0;

	fscanf(fpin, "%d", &T);

	for (int tc = 0; tc<T; tc++)
	{
		fscanf(fpin, "%lf %lf %lf", &C, &F, &X);

		while (fSumC <= fSumX)
		{
			fSumX = fSumC + (double) X / fCPS;
			fSumC = fSumC + (double) C / fCPS;
			fCPS += F;

			if (fSumX < fSumC + X / fCPS)
				break;
		}
		fprintf(fpout, "Case #%d: %.7f\n", tc+1, fSumX);

		fSumC = 0.0f;
		fSumX = 0.0f;
		fCPS = 2.0f;
	}




	fclose(fpin);
	fclose(fpout);
	return 0;
}

