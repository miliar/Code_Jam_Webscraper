#include <iostream>
#include <stdlib.h>

int comp (const void * elem1, const void * elem2) 
{
    double f = *((double*)elem1);
    double s = *((double*)elem2);
    if (f < s) return  1;
    if (f > s) return -1;
    return 0;
}

int main()
{
	FILE* fIn, *fOut;
	fopen_s(&fIn, "D-large.in", "rt");
	fopen_s(&fOut, "D-large.out", "wt");
	int T;
	fscanf(fIn, "%d", &T);
	int iCase=0;
	while(T>iCase++)
	{
		int N;
		double *playerA, *playerB;
		fscanf(fIn, "%d", &N);
		playerA = (double*)malloc(sizeof(double)*N);
		playerB = (double*)malloc(sizeof(double)*N);
		for (int i = 0; i < N; i++)
		{
			fscanf(fIn, "%lf", &playerA[i]);
		}
		for (int i = 0; i < N; i++)
		{
			fscanf(fIn, "%lf", &playerB[i]);
		}
		
		qsort (playerA, N, sizeof(double), comp);
		qsort (playerB, N, sizeof(double), comp);
		
		int idxB=N-1;
		int windWar = N;
		for (int i = N-1; i >= 0; i--)
		{
			if (playerA[i]<playerB[idxB])
			{
				windWar--;
			}
			else
			{
				idxB--;
			}
		}

		int winWar = 0;
		idxB=0;
		for (int i = 0; i < N; i++)
		{
			if (playerA[i]>playerB[idxB])
			{
				winWar++;
			}
			else
			{
				idxB++;
			}
		}

		fprintf(fOut, "Case #%d: %d %d\n", iCase, windWar, winWar);

		free(playerA);
		free(playerB);
	}
	fclose(fIn);
	fclose(fOut);
	return 1;
}