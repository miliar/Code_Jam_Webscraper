#include <stdio.h>
#include <stdlib.h>
#include <share.h>
#include <string>
#include <math.h>
#include <unordered_map>
using namespace std::tr1;

const unsigned int MAX_LINE = 1050000;

void main(int argc, char *argv[])
{
	//char* fileName = "input\\B-small-attempt0.in";
	//char* fileOutName = "output\\B-small-attempt0.out";
	char* fileName = "input\\B-large.in";
	char* fileOutName = "output\\B-large.out";
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

		int flipCount = 0;
		int strLen = strlen(currStr);
		for (int currIndex = strLen - 1; currIndex >= 0; currIndex--)
		{
			bool isUp = (currStr[currIndex] == '+');
			if (flipCount % 2)
				isUp = !isUp;
			if (!isUp)
				flipCount++;
		}
		fprintf(fileOutPtr, "Case #%d: %d\n", tt + 1, flipCount);
	}
	fflush(fileOutPtr);
	fclose(fileOutPtr);
	fclose(filePtr);
}