///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="A%d.in";
int FILE_FROM = 0;
int FILE_TO = 0;

#include <algorithm>
#include <limits>
#include <memory>

const bool OUT_FILE = true;
FILE *FILE_OUT;

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int i = 0; i < T; ++i)
	{
		unsigned int N, D = 0, C = 0, M;
		fscanf(fin, "%u", &N);
		if (N == 0)
		{
			fprintf(FILE_OUT, "Case #%d: INSOMNIA\n", i + 1);
			continue;
		}
		for (M = N;; M += N)
		{
			for (unsigned int K = M; K; K /= 10)
				D |= 1 << (K % 10);
			if (D == (1 << 10) - 1)
				break;
		}
		fprintf(FILE_OUT, "Case #%d: %u\n", i+1, M);
	}
}

///////////////////////////////////////////////////////////////////////////////

int main(int argc, char* argv[])
{
	char fileName[256];
	printf ("Which file: ");
	fgets ( fileName, 256, stdin );
	if (fileName[0]>13)
	{
		int i = atoi (fileName);
		FILE_FROM = FILE_TO = i;
	}
	for (int file_from=FILE_FROM; file_from<=FILE_TO; ++file_from)
	{
		sprintf(fileName, FILENAME, file_from);
		FILE *fin = fopen(fileName, "r");
		if (!fin)
		{
			printf("!!! CANNOT INF FILE %s", fileName);
			continue;
		} else {
			printf("Processing file: %s ...\n", fileName);
		}
		if (OUT_FILE)
		{
			char fileNameOut[256];
			sprintf(fileNameOut, "%s.out", fileName);
			FILE_OUT = fopen(fileNameOut, "w");
		} else
		{
			FILE_OUT = stdout;
		}
		ProcessFile(fin);
		fclose(fin);
		if (OUT_FILE)
			fclose(FILE_OUT);
	}
	printf("\nREADY!!!\n");
	getc(stdin);
	return 0;
}
