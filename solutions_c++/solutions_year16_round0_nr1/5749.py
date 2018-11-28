#include <stdio.h>
#include <stdlib.h>
#include <share.h>
#include <string>
#include <math.h>
#include <unordered_map>
using namespace std::tr1;

const unsigned int MAX_LINE = 1050000;

typedef unsigned __int64 bigint;

void main(int argc, char *argv[])
{
	//char* fileName = "input\\A-small-attempt0.in";
	//char* fileOutName = "output\\A-small-attempt0.out";
	char* fileName = "input\\A-large.in";
	char* fileOutName = "output\\A-large.out";
	FILE* filePtr = _fsopen(fileName, "r", _SH_DENYNO);
	FILE* fileOutPtr = _fsopen(fileOutName, "w", _SH_DENYNO);
	if (!filePtr || !fileOutPtr)
	{
		printf("File not found\n");
		return;
	}

	char* currStr = (char*)malloc(MAX_LINE);
	fgets(currStr, MAX_LINE, filePtr);
	int numCases = atoi(currStr);
	for (int tt = 0; tt < numCases; tt++)
	{
		fgets(currStr, MAX_LINE, filePtr);
		currStr[strcspn(currStr, "\r\n")] = 0;

		int seenCount = 0;
		int seen[10] = {0};
		bigint myN = _strtoui64(currStr, NULL, 10);
		bigint currNum = 0;
		for (int j = 0; j < 10000; j++)
		{
			currNum += myN;

			bigint temp = currNum;
			while (temp)
			{
				bigint curr = temp % 10;
				if (!seen[curr])
				{
					seen[curr] = 1;
					seenCount++;
				}
				temp = temp / 10;
			}

			if (seenCount == 10)
				break;
		}
		if (seenCount == 10)
			fprintf(fileOutPtr, "Case #%d: %llu\n", tt + 1, currNum);
		else
			fprintf(fileOutPtr, "Case #%d: INSOMNIA\n", tt + 1);
	}
	fflush(fileOutPtr);
	fclose(fileOutPtr);
	fclose(filePtr);
}