#include <stdio.h>
#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="A%d.in";
FILE *FILE_OUT;

///////////////////////////////////////////////////////////////////////////////

void ProcessFile(FILE* fin)
{
	int C;
	fscanf(fin, "%d", &C);
	for (int i=0; i<C; ++i)
	{
		char c;
		int Smax, Sum = 0, Friends = 0;
		fscanf(fin, "%d ", &Smax);
		for (int j=0; j<=Smax; ++j)
		{
			if (Sum<j)
			{
				Friends += j-Sum;
				Sum = j;
			}
			fscanf(fin, "%c", &c);
			Sum += c-'0';
		}
		fprintf(FILE_OUT, "Case #%d: %d\n", i+1, Friends);
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
