#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define M 7
#define T 100

void main()
{
	FILE *pf1;
	FILE *pf2;

	int m[T],num;//num cases, each smax is m
	int i, j, k;
	int count, need;
	int tmp;
	int t[M];
	int s[M];//data of each case
	fopen_s(&pf1, "E://google pratice//test1//A-small-attempt4.in", "r");
	if (pf1 == NULL)
	{
		printf("Cannot open file1!\n");
		return;
	}
	fopen_s(&pf2, "E://google pratice//test1//result.in", "w");
	if (pf2 == NULL)
	{
		printf("Cannot open file2!\n");
		return;
	}
	fscanf_s(pf1, "%d", &num);

	for (j = 0; j < num; j++)
	{
		fprintf(pf2, "Case #%d: ", j+1);
		fscanf_s(pf1, "%d", &m[j]);
		if (m[j] == 0)//if max level=0
		{
			fprintf(pf2, "%d\n", m[j]);
			fscanf_s(pf1, "%d", &tmp);
			continue;
		}
		else
		{
			fscanf_s(pf1, "%d", &tmp);
			k = m[j];
			while (tmp > 0)
			{
				t[k] = tmp % 10;
				k--;
				tmp = tmp / 10;
			}
			for (i = 0; i <=k; i++)
				t[i] = 0;
		
			count = 0;
			need = 0;

			for (i = 0; i < m[j]+1; i++)
			{
//				fscanf_s(pf1, "%d", &s[i]);
				s[i] = t[i];
			}

			for (i = 1; i < m[j]+1; i++)
			{
				count += s[i - 1];
				if (i>count)
				{
					need += i - count;
					count = count + i - count;
				}
			}
			fprintf(pf2, "%d\n", need);
//			printf("%d,%d\n",j, need);
		}
	}
}