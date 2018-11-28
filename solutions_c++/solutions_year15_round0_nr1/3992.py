// Standing_Ovation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *pFileRead, *pFileWrite;
	fopen_s(&pFileRead, "A-large.in", "r+");
	fopen_s(&pFileWrite, "A-large.out", "w+");

	int testCases;
	fscanf_s(pFileRead, "%d", &testCases);
	for (int i = 1; i <= testCases; ++i) 
	{
		unsigned int S_max;
		fscanf_s(pFileRead, "%u ", &S_max);

		char str[1002];
		fscanf_s(pFileRead, "%s", str, sizeof(str));

		unsigned int standing = 0;
		unsigned int needed = 0;

		for (unsigned int index = 0; index <= S_max; ++index) {
			 unsigned int current_number = str[index] - '0';
			 unsigned int current_needed = 0;

			if (index > standing && current_number > 0)
				current_needed = (index - standing);
			standing += (current_number + current_needed);
			needed += current_needed;
		}

		fprintf(pFileWrite, "Case #%d: %u \n", i, needed);

	}
	return 0;
}

