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
		double p = 0.0f;
		double c = atof(word[i++]);
		double a = 2.0f;
		double f = atof(word[i++]);
		double x = atof(word[i++]);
		double t1, t2;
		t1 = x / a;
next:
		t2 = p + (c / a) + (x / (a + f));
		if (t2 < t1)
		{
			p += c / a;
			a += f;
			t1 = t2;
			goto next;
		}
		sprintf(buffer, "Case #%d: %f\r\n", test, t1);
		_write(fh, buffer, strlen(buffer));
		printf(buffer);
	}

	_close(fh);

	_getch();
}
