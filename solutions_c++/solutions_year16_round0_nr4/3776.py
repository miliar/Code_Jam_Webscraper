#pragma warning(disable:4996)
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>

using namespace std;

const char inFileName[] = "D-small.in";
const char outFileName[] = "D-small.out";

const int MAX_S = 110;

int T, k, c, s;
int pos[MAX_S];

int main() {

	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++)
	{
		fscanf(inFile, "%d%d%d", &k, &c, &s);

		fprintf(outFile, "Case #%d:", t + 1);
		for (int i = 1; i <= s; i++)
		{
			fprintf(outFile, " %d", i);
		}
		fprintf(outFile, "\n");
	}

	fclose(inFile);
	fclose(outFile);
	return 0;
}
