#include <stdio.h>
#include <stdlib.h>
#include <share.h>
#include <string>
#include <math.h>
#include <unordered_map>
using namespace std::tr1;

const unsigned int MAX_LINE = 1050000;

typedef unsigned __int64 bigint;

bigint GetDivisor(bigint number)
{
	bigint max = sqrt(long double(number));
	max += 5;

	for (bigint div = 2; div <= max; div++)
	{
		if ((number % div) == 0)
			return div;
	}
	return 0;
}

void main(int argc, char *argv[])
{
	char* fileName = "input\\C-small-attempt0.in";
	char* fileOutName = "output\\C-small-attempt0.out";
	//char* fileName = "input\\A-large.in";
	//char* fileOutName = "output\\A-large.out";
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

		fprintf(fileOutPtr, "Case #%d:\n", tt + 1);
		int numToGenerate = 3;
		int strLen = 6;
		sscanf(currStr,"%d %d", &strLen, &numToGenerate);
		unsigned int bits = (1 << (strLen - 1)) + 1; // 32769
		unsigned int bitsmax = (1 << strLen) - 1; // 65535
		for (int jj = 0; jj < numToGenerate; jj++)
		{
			bigint results[11] = {0};
			while (bits <= bitsmax) // 2 -> 16 - 1
			{
				bool failed = false;
				for (bigint n = 2; n <= 10; n++)
				{
					bigint currSum = 0;
					bigint baseMult = 1;
					for (int z = 0; z < strLen; z++)
					{
						if (bits & (1 << z))
						{
							currSum += baseMult;
						}
						baseMult = baseMult * n;
					}
					bigint divisor = GetDivisor(currSum);
					if (!divisor)
					{
						failed = true;
						break;
					}
					results[n] = divisor;
				}
				if (!failed)
				{
					for (int z = strLen - 1; z >= 0; z--)
					{
						if (bits & (1 << z))
							fprintf(fileOutPtr, "1");
						else
							fprintf(fileOutPtr, "0");
					}
					fprintf(fileOutPtr, " ");

					for (int z = 2; z <= 10; z++)
					{
						if (z < 10)
							fprintf(fileOutPtr, "%llu ", results[z]);
						else
							fprintf(fileOutPtr, "%llu\n", results[z]);
					}
					bits+=2;
					break;
				}
				bits+=2;
			}
		}
	}
	fflush(fileOutPtr);
	fclose(fileOutPtr);
	fclose(filePtr);
}