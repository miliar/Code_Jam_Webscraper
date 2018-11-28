#include <stdio.h>
#include <stdlib.h>
#include <share.h>
#include <string>
#include <math.h>
#include <unordered_map>
using namespace std::tr1;

const unsigned int MAX_U16 = 65535;

__int64 lookupListA[10000001] = {0};

bool IsPalindromeA(__int64 num)
{
	if (!lookupListA[num])
	{
		char asString[1024];
		sprintf_s(asString, 1024, "%lld", num);
		
		int n = strlen(asString);
		for (int k = 0; k < n / 2; k++)
		{
			if (asString[k] != asString[n - 1 - k])
			{
				lookupListA[num] = 2;
				return false;
			}
		}
		lookupListA[num] = 1;
		return true;
	}
	return lookupListA[num] == 1;
}

unordered_map<__int64, bool> lookupList;

bool IsPalindromeB(__int64 num)
{
	unordered_map<__int64, bool>::const_iterator findResult = lookupList.find(num);
	if (findResult == lookupList.end())
	{
		char asString[1024];
		sprintf_s(asString, 1024, "%lld", num);
		
		int n = strlen(asString);
		for (int k = 0; k < n / 2; k++)
		{
			if (asString[k] != asString[n - 1 - k])
			{
				lookupList[num] = false;
				return false;
			}
		}
		lookupList[num] = true;
		return true;
	}
	return lookupList[num];
}

void main(int argc, char *argv[])
{
	char* fileName = "input\\A-large.in";
	char* fileOutName = "output\\A-large.out";
	FILE* filePtr = _fsopen(fileName, "r", _SH_DENYNO);
	FILE* fileOutPtr = _fsopen(fileOutName, "w", _SH_DENYNO);
	if (!filePtr || !fileOutPtr)
	{
		printf("File not found\n");
		return;
	}
	
	char currLine[MAX_U16];
	fgets(currLine, MAX_U16, filePtr);
	int numCases = atoi(currLine);
	for (int i = 0; i < numCases; i++)
	{
		fgets(currLine, MAX_U16, filePtr);
		char* parseContext;
		char* currSpot = strtok_s(currLine, " ", &parseContext);
		__int64 maxWait = _strtoui64(currSpot, NULL, 10);
		currSpot = strtok_s(NULL, " ", &parseContext);

		int numNeeded = 0;
		int totalSoFar = 0;
		for (int j = 0; j <= maxWait; j++)
		{
			int numThisTurn = currSpot[j] - '0';
			if (totalSoFar < j)
			{
				int missing = j - totalSoFar;
				numNeeded += missing;
				totalSoFar += missing;
			}
			totalSoFar += numThisTurn;
		}
		
		fprintf(fileOutPtr, "Case #%d: %lld\n", i + 1, numNeeded);
	}
	fflush(fileOutPtr);
	fclose(fileOutPtr);
	fclose(filePtr);
}