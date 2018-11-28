#include <cstdio>
#include<algorithm>

using namespace std;

FILE *fout;
FILE *fin;

void trouveSol(int curT)
{
	int nbL, nbCols;
	int pelouse[100 + 1][100 + 1];
	int maxLignes[100 + 1] = {0};
	int maxCols[100 + 1] = {0};

	fscanf(fin, "%d%d", &nbL, &nbCols);
	for(int curL = 0; curL < nbL; curL++)
		for(int curC = 0; curC < nbCols; curC++)
		{
			fscanf(fin, "%d", &pelouse[curL][curC]);
			if(pelouse[curL][curC] > maxLignes[curL])
				maxLignes[curL] = pelouse[curL][curC];
			if(pelouse[curL][curC] > maxCols[curC])
				maxCols[curC] = pelouse[curL][curC];
		}
	for(int curL = 0; curL < nbL; curL++)
		for(int curC = 0; curC < nbCols; curC++)
		{
			if(pelouse[curL][curC] < maxCols[curC] && pelouse[curL][curC] < maxLignes[curL])
			{
				fprintf(fout, "Case #%d: NO\n", curT);
				return;
			}
		}
	fprintf(fout, "Case #%d: YES\n", curT);
}

int main()
{
	fin = fopen ("B-Small.in", "r");
	fout = fopen ("B-Small.out", "w");

	int nbTests;
	fscanf(fin, "%d", &nbTests);
	for(int curT = 1; curT <= nbTests; curT++)
	{
		trouveSol(curT);
	}
    return 0;
}
