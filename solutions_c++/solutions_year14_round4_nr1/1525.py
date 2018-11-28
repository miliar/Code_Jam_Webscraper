#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>

using namespace std;

const char inFileName[] = "A-large.in";
const char outFileName[] = "A-large.out";

const int MaxN = 10100;

int T, n, x;
int a[MaxN];

int main() {
	
	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++) 
	{
		fscanf(inFile, "%d%d", &n, &x);
		for (int i = 0; i < n; i++)
			fscanf(inFile, "%d", &a[i]);

		int sol = 0;
		sort(a, a + n);
		int i = n - 1, j = 0;
		while (j <= i)
		{
			if (a[i] + a[j] <= x) j++;
			i--;
			sol++;
		}

		fprintf(outFile, "Case #%d: %d\n", t + 1, sol);
	}	
	
	fclose(inFile);
	fclose(outFile);
	return 0;
}
