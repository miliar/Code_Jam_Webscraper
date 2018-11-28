// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include "stdint.h"

using namespace std;

bool isPalindrome(int64_t x)
{
	int nLength = 0;
	int64_t t = x;

	while (t > 0)
	{
		nLength++;
		t /= 10;
	}

	// nLength = number of decimals in x
	t = x;

	for (int i = 0; i < nLength / 2; i++)
	{
		int nDecimalSmall = x;
		for (int j = 0; j < i; j++)
			nDecimalSmall /= 10;

		nDecimalSmall = nDecimalSmall % 10;

		int nDecimalBig = x;
		for (int j = 0; j < nLength - i - 1; j++)
			nDecimalBig /= 10;

		nDecimalBig = nDecimalBig % 10;

		if (nDecimalBig != nDecimalSmall)
			return false;
	}

	return true;
}

void solve(FILE* fout, int index, int64_t start, int64_t end)
{
	int nNumFS = 0;

	long double squareStart = start;
	long double squareEnd = end;

	squareStart = sqrt(squareStart);
	squareEnd = sqrt(squareEnd);

	int64_t sqStart = (int64_t)squareStart - 1;
	int64_t sqEnd = (int64_t)squareEnd + 1;

	for (int64_t x = sqStart; x <= sqEnd; x++)
	{
		int nSquare = x * x;

		if (nSquare < start || nSquare > end)
			continue;

		if (!isPalindrome(nSquare))
			continue;

		if (!isPalindrome(x))
			continue;

		nNumFS++;
	}

	fprintf(fout, "Case #%d: %d\n", index, nNumFS);
}


int _tmain(int argc, _TCHAR* argv[])
{
	char buff[1024];
	string fileToOpen = "input.txt";
	string fileToWrite = "output.txt";

	FILE* fp = fopen (fileToOpen.c_str(), "rb");
	if (!fp)
    {
		printf("Error: could not open file '%s'!\n", fileToOpen.c_str());
		return 0;
    }
	FILE* fout = fopen (fileToWrite.c_str(), "w");

	int numberOfTestCases;

	fgets(buff, sizeof (buff), fp);
	sscanf(buff, "%d", &numberOfTestCases);

	int index = 1;

	while (numberOfTestCases > 0)
	{
		int64_t start, end;
		//char start[1024];
		//char end[1024];
		
		fgets(buff, sizeof (buff), fp);
		sscanf(buff, "%lld %lld", &start, &end);

		//int i = 0;
		//while (buff[i] != ' ')
		//{
		//	start[i] = buff[i];
		//	i++;
		//}


		solve(fout, index, start, end);
		printf("Solved test case %d\n", index);

		numberOfTestCases--;
		index++;
	}
}

