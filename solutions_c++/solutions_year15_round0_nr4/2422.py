#include<stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	FILE* inputFile;
	FILE* outputFile;
	int T = 0;
	int X = 0, R = 0, C = 0;
	char *ret;
	char g[10] = "GABRIEL";
	char r[10] = "RICHARD";
	int i;
	fopen_s(&inputFile, "D-small-attempt5.in", "rt");
	fopen_s(&outputFile, "output_4_5_1.txt", "wt");

	if (inputFile == NULL)
	{
		printf_s("error");
	}
	else
	{
		fscanf_s(inputFile, "%d", &T);

		printf("%d\n", T);
	}




	for (i = 0; i < T; i++)
	{
		fscanf_s(inputFile, "%d ", &X);
		fscanf_s(inputFile, "%d ", &R);
		fscanf_s(inputFile, "%d", &C);

		if (R == 1 && C == 1 && X == 1)
		{
			printf("%d %d %d \n", R, C, X);
		}

		
		if ((R*C) == 16 && X != 3)
		{
			ret = g;
		}
		else if ((R*C) == 8 && (X == 2 || X == 1))
		{
			ret = g;
		}
		else if (R*C == 12)
		{
			ret = g;
		}
		else if (R*C == 4 && (X == 1 || X == 2))
		{
			ret = g;
		}
		else if (R*C == 9 && (X == 1 || X == 3))
		{
			ret = g;
		}
		else if (R*C == 6 && (X != 4))
		{
			ret = g;
		}
		else if ((R*C == 3 || R*C == 2) && X == 1)
		{
			ret = g;
		}
		else if (R*C == 2 && X == 2)
		{
			ret = g;
		}
		else if (R == 1 && C == 1 && X == 1)
		{
			ret = g;
		}
		else
		{
			ret = r;
		}
		fprintf_s(outputFile, "Case #%d: %s\n", i + 1, ret);
	}

	fclose(inputFile);
	fclose(outputFile);

	return 0;
}

