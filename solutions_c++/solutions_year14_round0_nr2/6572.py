#include<stdio.h>

#define InputFile "C:\\TempP\\CodeJam\\input\\cookieINP.txt"
#define OutputFile "C:\\TempP\\CodeJam\\input\\cookieOUT.txt"

void calcOutPutCookie(FILE* pFile, FILE* pOutFile, int num, double, double, double );
double clcSecondsCookie( double c, double f, double x);

int main()
{
	FILE* pFile = fopen(InputFile, "r");

	if (!pFile)
	{
		printf("Cannot open input.\n");
		return 0;
	}

	FILE* pOutFile  = fopen(OutputFile, "w");


	int nTestCases;
	//read test cases.
	fscanf(pFile,"%d\n", &nTestCases);

	for (int i=0; i < nTestCases; i++)
	{
		double C, F, X;
		fscanf(pFile, "%lf %lf %lf\n", &C, &F, &X);
		calcOutPutCookie(pFile, pOutFile, i+1, C, F, X);
	}

	if (pFile)
	{
		fclose(pFile);
	}

	if (pOutFile)
	{
		fclose(pOutFile);
	}

	return 0;
}

void calcOutPutCookie(FILE* pFile, FILE* pOutFile, int num, double c, double f, double x)
{
	fprintf(pOutFile, "Case #%d: %lf\n", num, clcSecondsCookie(c, f, x));
}

double clcSecondsCookie( double c, double f, double x)
{
	double rate = 2.0;
	double minTime = x / rate;
	double timepassed = 0.0;

	for (;;) 
	{
		double timeToNextfarm = timepassed + c / rate;
		double timetoWin = timeToNextfarm + ( x /(rate + f));

		if (timetoWin > minTime)
		{
			break;
		}

		rate = rate + f;
		timepassed = timeToNextfarm;
		minTime = timetoWin;
	}

	return minTime;
}
