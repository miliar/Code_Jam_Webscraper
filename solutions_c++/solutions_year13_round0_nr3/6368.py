// fns.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"
#include "string.h"


int _tmain(int argc, _TCHAR* argv[])
{
	
	FILE *fpin, *fpout;
	char buff[100], num[100], rev[100], num2[100], rev2[100];
	int no_tests, err, found, len;
	unsigned long long lower, upper, val;
	long double lsqrt, usqrt;

	/* open output file */
	err = fopen_s(&fpout, "test.out", "w");
	if (err != 0)
	{
		printf("Unable to open output file\n");
		return(-1);
	}

	/* open input file */
	err = fopen_s(&fpin, "test.in", "r");
	if (err != 0)
	{
		printf("Unable to open input file\n");
		return(-2);
	}
	/* read in input file */
	fgets( buff, 99, fpin );
	sscanf_s(buff, "%d", &no_tests);
	printf("Number of tests: %d\n", no_tests);

	for (int i=0; i<no_tests; i++)
	{

		fgets( buff, 99, fpin );
		sscanf_s(buff, "%llu %llu", &lower, &upper);
		printf ("lower bound: %llu, Upper Bound: %llu\n", lower, upper);

		fprintf(fpout, "Case #%d: ", i+1);

		/* find the square roots of the lower and upper bounds */
		lsqrt = ceil(sqrt((long double)lower));
		usqrt = floor(sqrt((long double)upper));
		printf("Square roots: %f, %f\n", lsqrt, usqrt);

		/* start looking for palindrones */
		found = 0;

		for (long double a=lsqrt; a<=usqrt; a++)
		{
			val = (unsigned long long)a;
			sprintf_s(num, "%llu", val);
			len = strlen(num);
			for (int j=0; j<len; j++)
				rev[len-j-1]=num[j];
			rev[len]='\0';
			val = (unsigned long long)a*a;
			sprintf_s(num2, "%llu", val);
			len = strlen(num2);
			for (int j=0; j<len; j++)
				rev2[len-j-1]=num2[j];
			rev2[len]='\0';
			if (!strcmp(num, rev) && !strcmp(num2, rev2))
			{
				printf("%s, %s\n", num, num2);
				found++;
			}
		}


		fprintf(fpout, "%d\n", found);
	}
	return 0;
}

