#pragma warning (disable :4996)
#include<stdio.h>
int main()
{
	int number;
	FILE *fi = fopen("B-large.in", "r");
	FILE *fp = fopen("B-small-attempt.out", "w");
	fscanf(fi,"%ld", &number);
	for (long i = 0; i < number; i++)
	{
		long num;
		fscanf(fi,"%ld", &num);
		long ary[10001] = { 0, };
		long max=0;
		for (long j = 0; j<num; j++)
		{
			int temp;
			fscanf(fi,"%ld", &ary[j]);
			if (max < ary[j])
				max = ary[j];
		}
		long min = max; 
		for (long j = 2; j < max; j++)
		{
			long cnt = 0;
			for (long k = 0; k < num; k++)
			{
				if (ary[k]>j)
					cnt += ((ary[k]-1)/ j);
			}
			cnt += j;
			if (min > cnt)
				min = cnt;
		}
		fprintf(fp,"Case #%ld: %ld\n", i+1, min);
	}
	fclose(fp);
}