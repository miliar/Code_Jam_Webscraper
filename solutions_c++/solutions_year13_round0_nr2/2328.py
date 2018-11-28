/*******************************************************************************
*	GoogleCodeJamQualificationB
*	Christoper Mayer, aka Quantum Anemone
*******************************************************************************/

/*
Problem


*/

#include	<Windows.h>
#include	<stdio.h>
#include	<conio.h>

FILE	*inputFile;
FILE	*outputFile;

void solve(void)
{
	// read in the data
	int	x, y, lawnX, lawnY;
	fscanf_s(inputFile, "%d", &lawnY);
	fscanf_s(inputFile, "%d", &lawnX);
	printf("%d x %d	", lawnX, lawnY);
	int *lawnH = new int[lawnX*lawnY];
	for (y=0; y<lawnY; y++)
	for (x=0; x<lawnX; x++)
			fscanf_s(inputFile, "%d", &lawnH[y*lawnX + x]);

	// solve
		// find max values for each column and row
	int *lawnXmax = new int[lawnX];
	//printf("xmax: ");
	for (x=0; x<lawnX; x++)
	{
		y = 0;
		lawnXmax[x] = lawnH[y*lawnX + x];
		for (y=1; y<lawnY; y++)
			if (lawnXmax[x] < lawnH[y*lawnX + x])
				lawnXmax[x] = lawnH[y*lawnX + x];
		//printf("%d ", lawnXmax[x]);
	}
	int *lawnYmax = new int[lawnY];
	//printf("ymax: ");
	for (y=0; y<lawnY; y++)
	{
		x = 0;
		lawnYmax[y] = lawnH[y*lawnX + x];
		for (x=1; x<lawnX; x++)
			if (lawnYmax[y] < lawnH[y*lawnX + x])
				lawnYmax[y] = lawnH[y*lawnX + x];
		//printf("%d ", lawnYmax[y]);
	}

	// check each square
	for (y=0; y<lawnY; y++)
	for (x=0; x<lawnX; x++)
	{
		if ((lawnH[y*lawnX + x] != lawnYmax[y]) && (lawnH[y*lawnX + x] != lawnXmax[x]))
		{
			printf("NO\n");
			fprintf_s(outputFile, "NO\n");
			goto cleanup;
		}
	}
	printf("YES\n");
	fprintf_s(outputFile, "YES\n");

cleanup:
	// clean up
	delete []lawnYmax;
	delete []lawnXmax;
	delete []lawnH;
}

void main(int argc, char *argv[])
{
	unsigned __int64	frequency, t0, t1;

	QueryPerformanceCounter((LARGE_INTEGER *)&t0);

	printf_s("GoogleCodeJamQualificationB\n");
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
