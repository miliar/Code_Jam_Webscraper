// Standing Ovation.cpp : Defines the entry point for the console application.
//

#include <stdio.h>


int main()
{
	int T;
	char input[1005];
	FILE *inputFile, *outputFile;
	int i,j, standing, ans, tmp, maxShyness;
	inputFile = fopen("A-large.in", "r");
	outputFile = fopen("OUTPUT.txt", "w");
	fscanf(inputFile,"%d", &T);
		
	for (int j = 1; j <= T; j++)
	{
		fscanf(inputFile, "%d%s", &maxShyness, input);
		i = ans = 0;
		standing = (int)input[0] - (int)'0';
		for (i = 1; i <= maxShyness; i++)
		{
			if ((int)input[i] - (int)'0' > 0)
			{
				if (standing < i)
				{
					ans = ans + i - standing;
					standing = i;
				}
				
					standing = standing + (int)input[i] - (int)'0';
			}
		}
		fprintf(outputFile, "Case #%d: %d\n", j, ans);
	}
	fclose(inputFile);
	fclose(outputFile);
	return 0;
}

