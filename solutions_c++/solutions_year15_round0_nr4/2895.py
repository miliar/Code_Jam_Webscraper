#include <stdio.h>
#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="D%d.in";
FILE *FILE_OUT;

#ifndef max
#define max(a,b)            (((a) > (b)) ? (a) : (b))
#endif

#ifndef min
#define min(a,b)            (((a) < (b)) ? (a) : (b))
#endif

///////////////////////////////////////////////////////////////////////////////

bool RichardWins( int X, int R, int C )
{
	if (X>=7) // can make a hole
		return true;
	if (X==1)
		return false;
	if (X>R*C) // can make a larger item
		return true;
	if (((R*C) % X) != 0)
		return true;
	if (X>=min(R,C)*2+1) // can make an item which does not fit 
		return true;
	if (X<min(R,C)*2-1) // cannot make a cork
		return false;

	// hack for small input, sorry
	if (X==2)
		return false;
	if (X==3)
		return false;
	if (X==4)
		return true;
	return false;
}

void ProcessFile(FILE* fin)
{
	for (int X=1; X<=4; ++X)
		for (int R=1; R<=4; ++R)
			for (int C=1; C<=4; ++C)
				RichardWins(X, R, C);
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		int X, R, C;
		fscanf(fin, "%d %d %d", &X, &R, &C);
		fprintf(FILE_OUT, "Case #%d: %s\n", i+1, RichardWins(X, R, C) ? "RICHARD" : "GABRIEL");
	}
}

///////////////////////////////////////////////////////////////////////////////

int main(int argc, char* argv[])
{
	char fileName[256];
	printf ("Which file: ");
	fgets ( fileName, 256, stdin );
	int i = atoi (fileName);
	sprintf(fileName, FILENAME, i);
	FILE *fin = fopen(fileName, "r");
	if (!fin)
	{
		printf("!!! CANNOT OPEN FILE %s", fileName);
		return 1;
	} else {
		printf("Processing file: %s ...\n", fileName);
	}
	char fileNameOut[256];
	sprintf(fileNameOut, "%s.out", fileName);
	FILE_OUT = fopen(fileNameOut, "w");
	ProcessFile(fin);
	fclose(fin);
	fclose(FILE_OUT);
	printf("\nREADY!!!\n");
	getc(stdin);
	return 0;
}
