/*******************************************************************************
*	GoogleCodeJamQualificationC
*	Christoper Mayer, aka Quantum Anemone
*******************************************************************************/

/*
Problem


*/

#include	<Windows.h>
#include	<stdio.h>
#include	<conio.h>
#include	<math.h>

FILE	*inputFile;
FILE	*outputFile;

bool palindrome(unsigned __int64 n)
{
	char	text[256], *p0, *p1;
	sprintf_s(text, "%lld", n);
	p0 = text;
	for (p1=text; *p1; p1++);	// find end
	p1--;						// point to last char
	while (p1 > p0)
	{
		if (*(p0++) != *(p1--))
			return false;
	}
	return true;
}

void solve(void)
{
	unsigned __int64	low, med1, med2, high, i, nFairAndSquare = 0;

	fscanf_s(inputFile, "%lld", &low);
	fscanf_s(inputFile, "%lld", &high);
	printf("%lld - %lld	", low, high);

	med1 = (unsigned __int64)sqrt((long double)low);
	med2 = (unsigned __int64)sqrt((long double)high);
	printf("(%lld-%lld) = ", med1, med2);

	for (i=med1; i<=med2; i++)
	{
		if (((i*i)>=low) && palindrome(i) && palindrome(i*i))
			nFairAndSquare++;
	}
	printf("%lld\n", nFairAndSquare);
	fprintf_s(outputFile, "%lld\n", nFairAndSquare);
}

void main(int argc, char *argv[])
{
	unsigned __int64	frequency, t0, t1;

	QueryPerformanceCounter((LARGE_INTEGER *)&t0);

	printf_s("GoogleCodeJamQualificationC\n");
	printf_s("Christoper Mayer, aka Quantum Anemone\n\n");

	// create output file
	char	outputFilename[256];
	sprintf_s(outputFilename, "%s.out", argv[1]);
	fopen_s(&outputFile, outputFilename, "w");
	printf_s("This program may output debug info to the console.\n");
	printf_s("The official output is written to the file %s.\n\n", outputFilename);

	// open input file
	fopen_s(&inputFile, argv[1], "r");

	// how many cases?
	int	nCases;
	fscanf_s(inputFile, "%d", &nCases);

	// solve them!
	for (int i=1; i<=nCases; i++)
	{
		printf_s("Case #%d: ", i);
		fprintf_s(outputFile, "Case #%d: ", i);
		solve();
	}

	// clean up
	fclose(inputFile);
	fclose(outputFile);

	QueryPerformanceCounter((LARGE_INTEGER *)&t1);
	QueryPerformanceFrequency((LARGE_INTEGER *)&frequency);
	printf_s("\nAll finished in %f seconds.\n", (t1-t0)/(float)frequency);
	_getch();
}
