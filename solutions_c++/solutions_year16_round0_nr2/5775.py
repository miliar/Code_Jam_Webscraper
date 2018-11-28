#pragma warning(disable:4996)
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>

using namespace std;

const char inFileName[] = "B-large.in";
const char outFileName[] = "B-large.out";

const int MAX_N = 110;

int T, n;
char s[MAX_N];

int main() {

	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++)
	{
		fscanf(inFile, "%s", s);
		n = strlen(s);
		int sol = 1;
		for (int i = 1; i < n; i++)
		{
			if (s[i] != s[i - 1])
			{
				sol++;
			}
		}
		if (s[n - 1] == '+')
		{
			sol--;
		}


		fprintf(outFile, "Case #%d: %d\n", t + 1, sol);
	}

	fclose(inFile);
	fclose(outFile);
	return 0;
}
