// A2015.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdio.h>
#include <vector>

#define FILE_INPUT	"in3.txt"
#define FILE_OUTPUT "out.txt"
int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fpIn = fopen(FILE_INPUT, "rt");
	if (fpIn == NULL)
		return -1;

	FILE* fpOut = fopen(FILE_OUTPUT, "wt");
	if (fpOut == NULL)
		return -2;

	char buf[1024] = {0};
	fscanf(fpIn, "%s\n", buf);
	int all = atoi(buf);
	for (int i = 0; i < all; ++i)
	{
		char sMax[8] = {0};
		char sValue[1024] = {0};
		fscanf(fpIn, "%s %s\n", sMax, sValue);

		int s = atoi(sMax);
		int need = 0;
		int now = 0;
		for (int j = 0; j <= s; ++j)
		{
			char ch[2];
			ch[0] = sValue[j];
			ch[1] = 0;

			if (j > now)
			{
				need += 1;
				now += 1;
			}

			int digit = atoi(ch);
			now += digit;
		}

		fprintf(fpOut, "Case #%d: %d\n", i + 1, need);
	}

	fclose(fpIn);
	fclose(fpOut);




	return 0;
}

