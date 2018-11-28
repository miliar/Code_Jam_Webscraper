#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>

using namespace std;

const char inFileName[] = "B-large.in";
const char outFileName[] = "B-large.out";

const int MaxN = 200;

int T, n, m, sol;
int a[MaxN][MaxN];
int row[MaxN], col[MaxN];

int main() {
	
	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++) 
	{
		fscanf(inFile, "%d%d", &n, &m);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				fscanf(inFile, "%d", &a[i][j]);

		for (int i = 1; i <= n; i++)
		{
			row[i] = 0;
			for (int j = 1; j <= m; j++)
				row[i] = max(row[i], a[i][j]);
		}
		for (int j = 1; j <= m; j++)
		{
			col[j] = 0;
			for (int i = 1; i <= n; i++)
				col[j] = max(col[j], a[i][j]);
		}
		
		bool ok = true;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				ok = ok && (a[i][j] == min(row[i], col[j]));

		if (ok)
			fprintf(outFile, "Case #%d: YES\n", t + 1);
		else
			fprintf(outFile, "Case #%d: NO\n", t + 1);
	}	
	
	fclose(inFile);
	fclose(outFile);
	return 0;
}
