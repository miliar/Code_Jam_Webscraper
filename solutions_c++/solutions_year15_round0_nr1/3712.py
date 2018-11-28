#include<stdio.h>
#include<stdlib.h>
#pragma warning (disable : 4996)
int main()
{
	FILE * fin = fopen("A-large.in", "r");
	long number;
	fscanf(fin,"%d", &number);
	FILE *fp = fopen("output.txt", "w");
	for (long i = 0; i < number; i++)
	{
		long num;
		fscanf(fin,"%d", &num);
		char * string = (char*)malloc(sizeof(char) * num + sizeof(char) * 3);
		fscanf(fin,"%s", string);
		long sum = 0;
		long plus = 0;
		for (long j = 0; j < num + 1; j++)
		{
			if (sum < j)
			{
				plus += j - sum;
				sum += j - sum;
			}
			sum += string[j]-'0';
		}
		fprintf(fp,"Case #%ld: %ld\n", i+1, plus);
	}
	fclose(fp);
}