// Ominous Omino.cpp : Defines the entry point for the console application.
//

#include <stdio.h>


int sizeCriteria(int size, int width, int height)
{
	int tmp;
	if (width > height)
	{
		tmp = width;
		width = height;
		height = tmp;
	}
	switch (size)
	{
	case 1:
		if (width >= 1 && height >= 1)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	case 2:
		if (width >= 1 && height >= 2)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	case 3:
		if (width >= 2 && height >= 3)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	case 4:
		if (width >= 3 && height >= 4)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	case 5:
		if (width >= 2 && height >= 5)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	case 6:
		if (width >= 3 && height >= 6)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	default:
		return 0;
	}
}



int main()
{
	int T, i;
	int X, R, C;
	FILE *inputFile, *outputFile;
	inputFile = fopen("D-small-attempt1.in", "r");
	outputFile = fopen("OUTPUT.txt", "w");
	fscanf(inputFile, "%d", &T);
	for (i = 1; i <= T; i++)
	{
		fscanf(inputFile, "%d%d%d", &X, &R, &C);
		if (X < 7)
		{
			if (sizeCriteria(X, R, C))
			{
				if ((R*C) % X == 0)
				{
					fprintf(outputFile, "Case #%d: GABRIEL\n", i);
				}
				else
				{
					fprintf(outputFile, "Case #%d: RICHARD\n", i);
				}
			}
			else
			{
				fprintf(outputFile, "Case #%d: RICHARD\n", i);
			}
		}
		else
		{
			fprintf(outputFile, "Case #%d: RICHARD\n", i);
		}
	}
	fclose(inputFile);
	fclose(outputFile);
	return 0;
}

