// B. Revenge of the Pancakes.cpp : Defines the entry point for the console application.
//

#include <stdio.h>


int main()
{
	int T, i, j, ans;
	char S[101];
	FILE *inputFile, *outputFile;
	inputFile = fopen("B-large.in", "r");
	outputFile = fopen("OUTPUT.txt", "w");
	//scanf("%d", &T);
	fscanf(inputFile, "%d", &T);
	for (i = 1;i <= T;i++)
	{
		//scanf("%s", S);
		fscanf(inputFile, "%s", S);
		char prev = '+';
		int len = 0;
		ans = 0;
		while (S[len] != '\0')
		{
			len++;
		}
		while (--len >= 0)
		{
			if (S[len] != prev)
			{
				ans++;
				prev = S[len];
			}
		}



		//printf("Case #%d: %ld\n", i, ans);
		fprintf(outputFile, "Case #%d: %ld\n", i, ans);





	}







	fclose(inputFile);
	fclose(outputFile);
	return 0;
}

