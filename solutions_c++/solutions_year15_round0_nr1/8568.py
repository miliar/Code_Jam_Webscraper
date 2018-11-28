#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int main()
{
	int i;
	int number=0;
	int clap = 0;
	int sum = 0; 
	char temp[2000];
	int max; 
	FILE *f1, *f2;
	f1 = fopen("A-large.in", "r+");
	f2 = fopen("result.txt", "w+");
	fscanf(f1, "%d", &i);

	for (int cnt = 0; cnt < i; cnt++)
	{
		fscanf(f1, "%d", &max);
		fscanf(f1, "%s", temp);
		for (int cnt_2 = 0; cnt_2 <= max;)
		{
			number = temp[cnt_2]-48;
			clap += number;
			if (++cnt_2 > clap)
			{
				int k = cnt_2 - clap;
				sum += k;
				clap += k;				
			}				
			
		}

		fprintf(f2, "Case #%d: %d\n", cnt+1 ,sum);
		sum = 0;
		clap = 0;
	}
	return 0;
}