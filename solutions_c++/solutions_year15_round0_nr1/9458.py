#include <stdio.h>

#define SMALL_SET 6
#define LARGE_SET 1000

#define DATA_SET LARGE_SET

void do_task(FILE* fout, FILE* fin)
{
	int t;
	int s_max;
	char s_str[DATA_SET + 2];
	unsigned int invited;
	unsigned int sum;

	fscanf(fin, "%d\r\n", &t);

	for(int i = 0; i < t; i++)
	{
		fscanf(fin, "%d %s\r\n", &s_max, s_str);

		invited = 0;
		for(int j = 1; s_str[j]; j++)
		{
			sum = 0;
			for(int k = j - 1; 0 <= k; k--)
				sum += (s_str[k] - '0');
			sum += invited;

			if(sum < j)
				invited++;
		}

		fprintf(fout, "Case #%d: %d\r\n", i + 1, invited);
	}
}

int main()
{
	FILE* fin = fopen("A-large.in", "a+");

	if(fin)
	{
		FILE* fout = fopen("A-large.out", "w");

		if(fout)
		{
			do_task(fout, fin);

			fclose(fout);
		}
		else
			printf("error.\n");

		fclose(fin);
	}
	else
		printf("error.\n");

	return 0;
}
