#include "stdafx.h"
#include <stdlib.h>

int main(int argc, char* argv[])
{
	int t, S_max;
	int i, j, k;
	int count, sum;
//	int temp;
	char S[1100]; 
	FILE *IN, *OUT;
	
	IN = fopen ("A-large.in" , "r");
	OUT = fopen ("A-large.out" , "w");
	fscanf(IN, "%d", &t);
	for (i=0; i<t; i++)
	{
		count = 0;
		sum = 0;
		fscanf(IN, "%d %s", &S_max, S);
		for(j=0; j<=S_max; j++)
		{
//			temp = (int)[j];
			if (j <= sum)
			{
				sum = sum + (int)(S[j] - '0');
			}
			else 
			{
				sum++;
				count++;
				sum = sum + (int)(S[j] - '0');
			}
		}
		//printf("%d %s\n", S_max, S);
		printf("Case #%d: %d\n", i+1, count);
		fprintf(OUT, "Case #%d: %d\n", i+1, count);
	}
	fclose (IN);
	fclose (OUT);
	system("pause");

	return 0;
}

