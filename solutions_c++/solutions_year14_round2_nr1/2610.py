#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <math.h>

#define ATTRIBUTE_NORETURN __attribute__((noreturn))

void error(const char* fmt, ...) __attribute__((format(printf, 1, 2), noreturn));

void error(const char* fmt, ...)
{
	va_list args;
	va_start(args, fmt);

	vfprintf(stderr, fmt, args);

	va_end(args);

	exit(-1);
}

void nfscanf(int argCount, FILE* f, const char* fmt, ...)
{
	va_list args;
	va_start(args, fmt);

	if (vfscanf(f, fmt, args) != argCount)
		error("File format error");

	va_end(args);
}

void doTestCase(FILE* f, int caseNo)
{
	int i, n;
	char** strings;
	char** stringsOrig;

	int* repCount, totalRepCount, targetRepCount;
	int opCount = 0;
	int totalOps = 0;

	nfscanf(1, f, "%d\n", &n);

	strings = (char**) malloc(sizeof(char*) * n);
	stringsOrig = (char**) malloc(sizeof(char*) * n);
	repCount = (int*) malloc(sizeof(int) * n);

	for (i = 0;i < n;++i)
	{
		stringsOrig[i] = strings[i] = (char*) malloc(sizeof(char) * 128);
		nfscanf(1, f, "%s\n", strings[i]);
		fprintf(stderr, "String %d: %s\n", i, strings[i]);
		repCount[i] = 0;
	}
	fflush(stderr);

	char currentChar = strings[0][0];
	while (currentChar != '\0')
	{
		totalRepCount = 0;
		for (i = 0;i < n;++i)
		{
			repCount[i] = 0;

			if (*strings[i] == '\0')
			{
				totalOps = -1;
				break;
			}

			while (*(strings[i]) == currentChar)
			{
				++repCount[i];
				++strings[i];
			}

			if (repCount[i] == 0)
				totalOps = -1;

			totalRepCount += repCount[i];
		}

		if (totalOps == -1)
			break;

		// We want each string to have totalRepCount/n repetitions of this letter in it.
		targetRepCount = (int) round((float)totalRepCount/(float)n);
		for (i = 0;i < n;++i)
		{
			opCount = abs(repCount[i] - targetRepCount);
			totalOps += opCount;
		}

		currentChar = strings[0][0];
	}

	for (i = 0;i < n;++i)
	{
		if (*strings[i] != '\0')
		{
			totalOps = -1;
			break;
		}
	}

	if (totalOps == -1)
		printf("Case #%d: %s\n", caseNo+1, "Fegla Won");
	else
		printf("Case #%d: %d\n", caseNo+1, totalOps);

	for (i = 0;i < n;++i)
		free(stringsOrig[i]);

	free(strings); free(stringsOrig);
	free(repCount);
}

int main(int argc, char* argv[])
{
	FILE* f;

	if (argc < 2) error("USAGE: %s <filename>\n", argv[0]);

	f = fopen(argv[1], "r");
	if (!f) error("Unable to open file\n");

	int i, t;
	if (fscanf(f, "%d\n", &t) != 1) error("File format error\n");

	for (i = 0;i < t;++i)
		doTestCase(f, i);

	fclose(f);
	return 0;
}

