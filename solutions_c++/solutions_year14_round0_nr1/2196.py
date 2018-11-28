#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

const int N = 5;

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int T;
int first[N][N], second[N][N];
int answer1 = 0, answer2 = 0;

int main()
{
	fscanf(f, "%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		fscanf(f, "%d", &answer1);
		for (int i = 1; i < N; ++i)
		{
			for (int j = 1; j < N; ++j)
			{
				fscanf(f, "%d", &first[i][j]);
			}
		}
		fscanf(f, "%d", &answer2);
		for (int i = 1; i < N; ++i)
		{
			for (int j = 1; j < N; ++j)
			{
				fscanf(f, "%d", &second[i][j]);
			}
		}

		int numberOfResults = 0, result = -1;
		for (int i = 1; i < N; ++i)
		{
			for (int j = 1; j < N; ++j)
			{
				if (first[answer1][i] == second[answer2][j])
				{
					numberOfResults++;
					result = first[answer1][i];
				}
			}
		}

		if (numberOfResults == 0)
		{
			fprintf(g, "Case #%d: Volunteer cheated!\n", t);
		}
		else if (numberOfResults == 1)
		{
			fprintf(g, "Case #%d: %d\n", t, result);
		}
		else
		{
			fprintf(g, "Case #%d: Bad magician!\n", t);
		}
	}

	fclose(f);
	fclose(g);
}