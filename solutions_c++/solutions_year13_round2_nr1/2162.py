/*******************************************************************************
*	GCJ-round1B-problemA.cpp
*	Quantum Anemone
*******************************************************************************/

/*
*/

#include	<Windows.h>
#include	<stdio.h>
#include	<conio.h>
#include	<math.h>

FILE	*inputFile;
FILE	*outputFile;

int compar(const void *a, const void *b)
{
	return *((int *)a) - *((int *)b);
}

void solve(void)
{
	int	A, N, M[100];

	fscanf_s(inputFile, "%d", &A);
	fscanf_s(inputFile, "%d", &N);
	//printf("%d %d\n", A, N);
	for (int i=0; i<N; i++)
	{
		fscanf_s(inputFile, "%d", &M[i]);
	}
	// delete all?
	if (A == 1)
	{
		printf("%d\n", N);
		fprintf_s(outputFile, "%d\n", N);
		return;
	}
	// sort them!
	qsort(M, N, sizeof(*M), compar);

	int	nOps = 0;
	int	nextMote = 0;

	// absorb what we can
keepgoing:
	while ((nextMote < N) && (A > M[nextMote]))
	{
		A += M[nextMote++];
	}
	// are we finished?
	if (nextMote == N)
	{
done:
		printf("%d\n", nOps);
		fprintf_s(outputFile, "%d\n", nOps);
		return;
	}
	// how many inserts to get to the next number?
	int ni = 0;
	int tA = A;
	while (tA <= M[nextMote])
	{
		ni++;
		tA += (tA-1);
	}
	// just delete the rest?
	if ((N - nextMote) <= ni)
	{
		nOps += (N - nextMote);
		goto done;
	}
	printf("? ");
	nOps += ni;
	A = tA;
	goto keepgoing;
}

void main(int argc, char *argv[])
{
	unsigned __int64	frequency, t0, t1;

	QueryPerformanceCounter((LARGE_INTEGER *)&t0);

	printf_s("GCJ-round1B-problemA\n");
	printf_s("Quantum Anemone\n\n");

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
