#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main()
{
	int arr1[4];
	int arr[4][4];
	int arr2[4];
	int i, j, c, x,m,r, n, l = 1;
	FILE *fp, *fp1;
	fp = fopen("A.in", "rb");
	fp1 = fopen("out.txt", "w");
	fscanf(fp, "%d", &n);
	for (int k = 1; k <= n;k++)
	{
		c = 0;
		fscanf(fp, "%d", &r);
		for (i = 0; i <= 3; i++)
		{
			for (j = 0; j <= 3; j++)
			{
				fscanf(fp, "%d", &m);
				arr[i][j] = m;
				printf("%d ", arr[i][j]);
			}
		}
		for (i = 0; i <= 3; i++)
		{
		arr1[i] = arr[r-1][i];
		}
		for (i = 0; i <= 3; i++)
		{
			for (j = 0; j <= 3; j++)
				printf("%d ", arr[i][j]);
			printf("\n");
		}
		fscanf(fp, "%d", &r);
		for (i = 0; i <= 3; i++)
		{
			for (j = 0; j <= 3; j++)
			{
				fscanf(fp, "%d", &m);
				arr[i][j] = m;
				printf("%d ", arr[i][j]);
			}
		}
		for (i = 0; i <= 3; i++)
			{
				arr2[i] = arr[r-1][i];
			}
		for (i = 0; i <= 3; i++)
		{
			for (j = 0; j <= 3; j++)
				{
					if (arr1[i] == arr2[j])
					{
						c++;
						x = arr1[i];
					}

				}
			}
			if (c == 1)
			{
				fprintf(fp1, "Case #%d: %d\n", l, x);
			}
			if (c > 1)
				fprintf(fp1, "Case #%d: Bad magician!\n", l);
			if (c == 0)
				fprintf(fp1, "Case #%d: Volunteer cheated!\n", l);
			l++;
		}
		
	getchar();
}
