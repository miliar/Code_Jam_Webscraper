#define _SCL_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <conio.h>
#include <stdio.h>
#include <string.h>

//#define IN_FILE_NAME "B-small-attempt0.in"
//#define OUT_FILE_NAME "B-small-attempt0.out"

#define IN_FILE_NAME "B-large.in"
#define OUT_FILE_NAME "B-large.out"

static const int MAXS = 105;

int main()
{
	freopen(IN_FILE_NAME, "r", stdin);
	freopen(OUT_FILE_NAME, "w", stdout);

	int t, tests;
	scanf("%d", &tests);

	for (t = 0; t < tests; t++)
	{
		char line[MAXS];
		int total = 0;

		scanf("%s", line);
		int i = 0;
		if (line[0] == '-')
		{
			total = 1;
			while (line[i] != '\0' && line[i] == '-') i++;
		}

		while (line[i] != '\0')
		{
			if (line[i] == '-')
				total += 2;
			i++;
			while (line[i] == line[i - 1]) i++;
		}

		printf("Case #%d: %d\n", t + 1, total);
	}
}