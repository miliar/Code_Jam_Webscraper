// A. Senate Evacuation.cpp : Defines the entry point for the console application.
//

#include <stdio.h>

bool debug = false;

int main()
{
	FILE *inputFile, *outputFile;
	if (!debug)
	{
		inputFile = fopen("A-large.in", "r");
		outputFile = fopen("OUTPUT.txt", "w");
	}


	int T, i, j,k, N;

	if (!debug)
	{
		fscanf(inputFile, "%d", &T);
	}
	else
	{
		scanf("%d", &T);
	}

	for (i = 1;i <= T;i++)
	{
		int P[26] = { 0 };

		if (!debug)
		{
			fscanf(inputFile, "%d", &N);
			for (j = 0;j < N;j++)
			{
				fscanf(inputFile, "%d", &P[j]);
			}
		}
		else
		{
			scanf("%d", &N);
			for (j = 0;j < N;j++)
			{
				scanf("%d", &P[j]);
			}
		}

		if (!debug)
		{
			fprintf(outputFile, "Case #%d: ", i);
		}
		else
		{
			printf("Case #%d: ", i);
		}



		int largInd = 0;
		for (j = 0;j < N;j++)
		{
			if (P[j] > P[largInd])
			{
				largInd = j;
			}
		}
		
		int second;
		if (largInd != N - 1)
		{
			second = largInd + 1;
		}
		else
		{
			second = 0;
		}
		for (j = 0;j < N;j++)
		{
			if (j != largInd)
			{
				if (P[j] > P[second])
				{
					second = j;
				}
			}
		}


		while (P[largInd] > P[second])
		{
			if (!debug)
			{
				fprintf(outputFile, "%c ", 'A' + largInd);
			}
			else
			{
				printf("%c ", 'A' + largInd);
			}
			P[largInd]--;
		}

		for (j = 0;j < N;j++)
		{
			if (j != largInd && j != second)
			{
				for (k = 0;k < P[j];k++)
				{
					if (!debug)
					{
						fprintf(outputFile, "%c ", 'A' + j);
					}
					else
					{
						printf("%c ", 'A' + j);
					}
				}
			}
		}


		for (j = 0;j < P[largInd];j++)
		{
			if (!debug)
			{
				fprintf(outputFile, "%c%c ", 'A' + largInd,'A'+second);
			}
			else
			{
				printf("%c%c ", 'A' + largInd, 'A' + second);
			}
		}


		if (!debug)
		{
			fprintf(outputFile, "\n");
		}
		else
		{
			printf("\n");
		}

	}










	if (!debug)
	{
		fclose(inputFile);
		fclose(outputFile);
	}

	return 0;
}

