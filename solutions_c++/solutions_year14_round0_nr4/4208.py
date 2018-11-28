#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <io.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <vector>

using namespace std;

void* loadfile(char *filename, int *size)
{
	int fh = _open(filename, O_BINARY);
	*size = _filelength(fh);
	void *data = malloc(*size + 2);
	_read(fh, data, *size);
	((char *)data)[*size] = ((char *)data)[*size + 1] = 0;
	_close(fh);
	return data;
}

bool whitespace(char c)
{
	return ((c == '\n') || (c == '\r') || (c == '\t') || (c == 0) || (c == ' '));
}

void tokenize(char *data, int size, vector<char *> *word)
{
	char *p = data;
	while (*data)
	{
		for (p = data; !whitespace(*p); p++);
		*p = 0;
		if (p != data)
			word->push_back(data);
		data = p + 1;
	}
}

int fcomp(const void * a, const void * b)
{
	if (*((float*)a) < *((float*)b))
		return -1;
	if (*((float*)a) > *((float*)b))
		return 1;
	return 0;
}

void main(int argc, char *argv[])
{
	printf("Google Code Jam 1\n\n");

	printf("Reading %s... ", argv[1]);
	int size;
	char *data = (char *)loadfile(argv[1], &size);
	printf("(%d)\n", size);

	vector<char *> word;
	tokenize(data, size, &word);
	for (auto w : word)
		printf("%s ", w);
	printf("\n\n");

	int fh = _open(argv[2], O_BINARY | O_RDWR | O_CREAT | O_TRUNC, S_IREAD | S_IWRITE);

	char buffer[256];
	int i = 0, j, k, war = 0, dwar = 0;
	int numCases = atoi(word[i++]);
	for (int test = 1; test <= numCases; test++)
	{
		int nBlocks = atoi(word[i++]);
		printf("%d blocks\n", nBlocks);
		float naomi[1000], ken[1000];
		for (j = 0; j < nBlocks; j++)
			naomi[j] = atof(word[i++]);
		for (j = 0; j < nBlocks; j++)
			ken[j] = atof(word[i++]);
		// smallest first
		qsort(naomi, nBlocks, sizeof(float), fcomp);
		qsort(ken, nBlocks, sizeof(float), fcomp);

		dwar = 0;
		int ni[1000], ki[1000];
		for (j = 0; j < nBlocks; j++)
		{
			ni[j] = ki[j] = j;
		}
		for (j = 0; j < nBlocks; j++)
		{
			if (naomi[ni[0]] < ken[ki[0]])
			{  // we lose 1
				// kill naomi's bottom
				for (k = 0; k < nBlocks - j-1; k++)
					ni[k] = ni[k + 1];
				// kill ken's top (no-op)
			}
			else
			{
				// naomi's bottom take's kens bottom
				dwar++;
				// kill naomi's bottom
				for (k = 0; k < nBlocks - j-1; k++)
					ni[k] = ni[k + 1];
				// kill ken's bottom
				for (k = 0; k < nBlocks - j-1; k++)
					ki[k] = ki[k + 1];
			}
		}

		war = 0;
		for (j = 0; j < nBlocks; j++)
		{
			ni[j] = ki[j] = j;
		}
		for (j = 0; j < nBlocks; j++)
		{
			// naomi plays highest
			// ken plays to just beat
			for (k = 0; k < nBlocks - j; k++)
			{
				if (ken[k] > naomi[nBlocks-j-1])
					break;
			}
			if (k == nBlocks - j)
			{ // naomi wins
				war++;
				// ken plays lowest
				for (k = 0; k < nBlocks - j - 1; k++)
					ken[k] = ken[k + 1];
			}
			else
			{ // ken wins, plays k
				for (; k < nBlocks - j - 1; k++)
					ken[k] = ken[k + 1];
			}
		}

		sprintf(buffer, "Case #%d: %d %d\r\n", test, dwar, war);
		_write(fh, buffer, strlen(buffer));
		printf(buffer);
	}

	if (i != word.size())
		printf("ERROR!\n");

	_close(fh);

	_getch();
}
