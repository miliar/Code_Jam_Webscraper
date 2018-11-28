// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>

using namespace std;

bool uniform(int* map, int nX, int nY)
{
	int nValue = map[0];

	for (int y = 0; y < nY; y++)
		for (int x = 0; x < nX; x++)
		{
			if (map[y*nX + x] != nValue)
				return false;
		}

	return true;
}

int mapMin(int* map, int nX, int nY)
{
	int nMin = map[0];

	for (int y = 0; y < nY; y++)
		for (int x = 0; x < nX; x++)
		{
			if (map[y*nX + x] < nMin)
				nMin = map[y*nX + x];
		}

	return nMin;
}


int mapSecMin(int* map, int nX, int nY, int nMin)
{
	int nMin2 = 100;

	for (int y = 0; y < nY; y++)
		for (int x = 0; x < nX; x++)
		{
			if (map[y*nX + x] < nMin2 && map[y*nX + x] != nMin)
				nMin2 = map[y*nX + x];
		}

	return nMin2;
}

void solveMap(int* map, FILE* fout, int index, int nX, int nY)
{
	bool impossible = false;
	bool* isMinLine = (bool*)malloc(sizeof(bool)*nY);
	bool* isMinCol = (bool*)malloc(sizeof(bool)*nX);
	
	while (!impossible && !uniform(map, nX, nY))
	{
		int nValue = mapMin(map, nX, nY);
		int nMin2 = mapSecMin(map, nX, nY, nValue);

		// At least one Line or column must exist with only that minimum
		int nLines = 0;
		int nCols = 0;

		for (int y = 0; y < nY; y++)
		{
			isMinLine[y] = true;

			for (int x = 0; x < nX; x++)
				if (map[y*nX + x] != nValue)
					isMinLine[y] = false;

			if (!isMinLine[y])
				continue;

			nLines++;
		}

		for (int x = 0; x < nX; x++)
		{
			isMinCol[x] = true;

			for (int y = 0; y < nY; y++)
				if (map[y*nX + x] != nValue)
					isMinCol[x] = false;

			if (!isMinCol[x])
				continue;

			nCols++;
		}

		if (nLines == 0 && nCols == 0)
			impossible = true;
		else
		{
			for (int y = 0; y < nY; y++)
			{
				if (!isMinLine[y])
					continue;

				for (int x = 0; x < nX; x++)
					map[y*nX + x] = nMin2;
			}

			for (int x = 0; x < nX; x++)
			{
				if (!isMinCol[x])
					continue;

				for (int y = 0; y < nY; y++)
					map[y*nX + x] = nMin2;
			}
		}
	}

	if (impossible)
		fprintf(fout, "Case #%d: NO\n", index);
	else
		fprintf(fout, "Case #%d: YES\n", index);
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
		int n, m;
		
		fgets(buff, sizeof (buff), fp);
		sscanf(buff, "%d %d", &n, &m);

		int* map = (int*)malloc(4*n*m);

		for (int y = 0; y < n; y++)
		{
			fgets(buff, sizeof (buff), fp);
			char* currBuff = buff;

			for (int x = 0; x < m; x++)
			{
				map[x + y*m] = strtol(currBuff, &currBuff, 0);
			}
		}

		// We have the map, we solve it

		// If I have a line or a column where everything is equal
		// It must have been done last, thus be lower than the others
		solveMap(map, fout, index, m, n);
		printf("Solved test case %d\n", index);

		numberOfTestCases--;
		index++;
	}
}

