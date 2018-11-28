// lotery_small.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	FILE * pFile;
	pFile = fopen("input.in", "r");
	FILE * oFile;
	oFile = fopen("output.txt", "w+");
	int t;
	fscanf(pFile, "%d", &t);
	int a, b, k;
	int rslt;
	long long int pocet;
	for (int n = 1; n <= t; n++){
		fscanf(pFile, "%d %d %d", &a, &b, &k);
		pocet = 0;
		for (int i = 0; i < a; i++){
			for (int j = 0; j < b; j++){
				//printf("%d %d %d %d\n", i, j, i&j, k);
				rslt = i&j;
				if (rslt < k){ pocet++; }
			}
		}
		fprintf(oFile, "Case #%d: %d\n", n, pocet);
	}
	fclose(pFile);
	fclose(oFile);
	return 0;
}

