#include <cstdio>

using namespace std;

int main()
{
	char inFile[30], outFile[30];
	FILE *fin, *fout;
	int testNum, n , m, lawn[100][100], maxVal[2][100];
	bool isPossible;
	scanf("%s", inFile);
	scanf("%s", outFile);
	fin = fopen(inFile, "r");
	fout = fopen(outFile,"w");

	fscanf(fin, "%d", &testNum);
	for (int i = 1; i <= testNum; i++)
	{
		isPossible = true;
		fscanf(fin, "%d %d", &n, &m);
		for (int j = 0; j < n; j++)
		{
			maxVal[0][j] = 0;
			for (int k = 0; k < m; k++)
			{
				fscanf(fin, "%d", &lawn[j][k]);
				if (lawn[j][k] > maxVal[0][j])
				{
					maxVal[0][j] = lawn[j][k];
				}
			}
		}
		for (int j = 0; j < m; j++)
		{
			maxVal[1][j] = 0;
			for (int k = 0; k < n; k++)
			{
				if (lawn[k][j] > maxVal[1][j])
				{
					maxVal[1][j] = lawn[k][j];
				}
			}
		}

		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < m; k++)
			{
				if (lawn[j][k] < maxVal[0][j]
				&& lawn[j][k] < maxVal[1][k])
				{
					isPossible = false;
					break;
				}
			}
			if (!isPossible)
			{
				break;
			}
		}
		if (isPossible)
		{
			fprintf(fout, "Case #%d: YES\n", i);
		}
		else
		{
			fprintf(fout, "Case #%d: NO\n", i);
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
