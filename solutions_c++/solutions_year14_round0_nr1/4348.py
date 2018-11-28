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
	void *data = malloc(*size+2);
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
	int i = 0, j, k;
	int numCases = atoi(word[i++]);
	for (int test = 1; test <= numCases; test++)
	{
 		int a1 = atoi(word[i++]) - 1;
		int c1[16];
		for (j = 0; j < 16; j++)
			c1[j] = atoi(word[i++]);
		int a2 = atoi(word[i++]) - 1;
		int c2[16];
		for (j = 0; j < 16; j++)
			c2[j] = atoi(word[i++]);

		int p1[4];
		for (j = 0; j < 4; j++)
			p1[j] = c1[a1 * 4 + j];

		// each of p1 must be in different rows of c2, or else bad magician
		int newX[4], newY[4];
		// find each of our 4 cards
		for (j = 0; j < 4; j++)
		{
			for (k = 0; k < 16; k++)
			{
				if (p1[j] == c2[k])
				{
					newX[j] = k % 4;
					newY[j] = k / 4;
					break;
				}
			}
		}

		printf("%d\n", a1);
		for (j = 0; j < 4; j++)
		{
			for (k = 0; k < 4; k++)
				printf("%d ", c1[4 * j + k]);
			printf("\n");
		}
		printf("%d\n", a2);
		for (j = 0; j < 4; j++)
		{
			for (k = 0; k < 4; k++)
				printf("%d ", c2[4 * j + k]);
			printf("\n");
		}
		printf("p1[] = ");
		for (j = 0; j < 4; j++)
		{
			printf("%d ", p1[j]);
		}
		printf("\n");

		// good magician = unique newYs
		bool badMag = ((newY[0] == newY[1]) || (newY[0] == newY[2]) || (newY[0] == newY[3]) || (newY[1] == newY[2]) || (newY[1] == newY[3]) || (newY[2] == newY[3]));
		int card = -1;
		// which card?
		int nc = 0;
		for (j = 0; j < 4; j++)
		{
			for (k = 0; k < 4; k++)
			{
				if (p1[j] == c2[a2 * 4 + k])
				{
					card = c2[a2 * 4 + k];
					nc++;
					break;
				}
			}
		}
		printf("nc = %d, card = %d\n", nc, card);
		if (badMag && (nc == 0))
		{
			sprintf(buffer, "Case #%d: Volunteer cheated!\r\n", test);
			_write(fh, buffer, strlen(buffer));
			printf(buffer);
		}
		else
		{
			if (badMag && (nc > 1))
			{
				sprintf(buffer, "Case #%d: Bad magician!\r\n", test);
				_write(fh, buffer, strlen(buffer));
				printf(buffer);
			}
			else
			{
				sprintf(buffer, "Case #%d: %d\r\n", test, card);
				_write(fh, buffer, strlen(buffer));
				printf(buffer);
			}
		}
	}

	if (i != word.size())
		printf("ERROR!\n");

	_close(fh);

	_getch();
}
