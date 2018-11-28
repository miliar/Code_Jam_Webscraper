// A. Counting Sheep.cpp : Defines the entry point for the console application.
//

#include <stdio.h>


int main()
{
	int T, i;
	long N;
	FILE *inputFile, *outputFile;
	inputFile = fopen("A-large.in", "r");
	outputFile = fopen("OUTPUT.txt", "w");
	//scanf("%d", &T);
	fscanf(inputFile, "%d", &T);
	for (i = 1;i <= T;i++)
	{
		
		//scanf("%ld", &N);
		fscanf(inputFile, "%ld", &N);

		if (N == 0)
		{
			//printf("Case #%d: INSOMNIA\n", i);
			fprintf(outputFile, "Case #%d: INSOMNIA\n", i);
		}
		else
		{
			int feq[10] = { 0 }, count = 0;
			long ans = 0;
			while (count < 10)
			{
				ans += N;
				long tmp = ans;
				while (tmp != 0)
				{
					if (feq[tmp % 10] == 0)
					{
						count++;
					}
					feq[tmp % 10]++;
					tmp /= 10;
				}
			}


			//printf("Case #%d: %ld\n", i, ans);
			fprintf(outputFile, "Case #%d: %ld\n", i, ans);
		}
	}
	return 0;
}

