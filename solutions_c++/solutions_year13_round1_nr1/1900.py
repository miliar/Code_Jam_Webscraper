/*******************************************************************************
*	GCJ-1A.cpp
*	Google Code Jam Round 1A
*	Christoper Mayer, aka Quantum Anemone
*******************************************************************************/

/*
*/

#include	<Windows.h>
#include	<stdio.h>
#include	<conio.h>
#include	<math.h>

FILE	*inputFile;
FILE	*outputFile;

void solve(void)
{
	unsigned __int64	r, p;

	unsigned __int64	x, black, vr;

	fscanf_s(inputFile, "%lld", &r);
	fscanf_s(inputFile, "%lld", &p);

	// pretend all is painted
	if ((r & 1) == 1)
	{	// r is odd
		vr = r/2;
		black = 2*vr*vr + vr;
	}
	else
	{	// r is even
		vr = r/2;
		black = 2*vr*vr - vr;
	}
	// add the virtual to our available paint
	p += black;
	// how many rings can we paint?
	if ((r&1) == 1)
	{
		// paint needed = 2x^2 + x
		if (p > 0x00ffffffffffffff)
			x = (-1 + sqrt(8.0)*sqrt((double)p)) / (4);	// close enough?
		else
			x = (-1 + sqrt(1.0 + 8.0*p)) / (4);
	}
	else
	{
		if (p > 0x00ffffffffffffff)
			x = (1 + sqrt(8.0)*sqrt((double)p)) / (4);
		else
			x = (1 + sqrt(1.0 + 8.0*p)) / (4);
	}
	x -= vr;

	printf("%lld\n", x);
	fprintf_s(outputFile, "%lld\n", x);
}

void main(int argc, char *argv[])
{
	unsigned __int64	frequency, t0, t1;

	QueryPerformanceCounter((LARGE_INTEGER *)&t0);

	printf_s("GCJ-1A\n");
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
