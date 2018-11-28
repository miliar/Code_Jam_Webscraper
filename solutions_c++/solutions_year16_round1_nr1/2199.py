// A. The Last Word.cpp : Defines the entry point for the console application.
//

#include <stdio.h>


int main()
{
	FILE *inputFile, *outputFile;
	inputFile = fopen("A-large.in", "r");
	outputFile = fopen("OUTPUT.txt", "w");
	int T, i, j, first, last;
	char ip[1001], op[2001];

	fscanf(inputFile, "%d", &T);
	//scanf("%d", &T);
	for (i = 1;i <= T;i++)
	{
		fscanf(inputFile, "%s", ip);
		//scanf("%s", ip);
		first = last = 1000;
		op[first] = ip[0];
		j = 1;
		while (ip[j] != '\0')
		{
			if (ip[j] >= op[first])
			{
				op[--first] = ip[j];
			}
			else
			{
				op[++last] = ip[j];
			}
			j++;
		}
		fprintf(outputFile, "Case #%d: ", i);
		//printf("Case #%d: ", i);
		for (j = first;j <= last;j++)
		{
			fprintf(outputFile, "%c", op[j]);
			//printf("%c", op[j]);
		}
		fprintf(outputFile, "\n");
		//printf("\n");
	}





	return 0;
}

