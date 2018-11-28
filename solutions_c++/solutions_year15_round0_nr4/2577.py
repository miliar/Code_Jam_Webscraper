#pragma warning(disable:4996)
#include <stdio.h>
#include <malloc.h>
#include <conio.h>

int main()
{
	FILE *fp;
	int Loop, loop;
	int* result;
	int x, r, c;

	fp = fopen("C:\\data\\googleCodeJam.txt", "rt");
	if (fp == NULL){ printf("open error!!\n"); getch();  return 0; }
	fscanf(fp, "%d\n", &Loop);
	result = (int*)calloc(sizeof(int), Loop);

	for (loop = 0; loop < Loop; loop++)
	{
		fflush(stdin);
		fscanf(fp, "%d %d %d\n", &x, &r, &c);

		if (x > 6) continue;
//		
		if ((r*c) % x != 0) continue;
		else
		{
			if (r*c == x)
			{
				if (r*c == 1)
				{
					result[loop] = 1;
					continue;
				}
				else if (r*c == 2)
				{
					result[loop] = 1;
					continue;
				}
				else continue;
			}
if (r * c < (x-1)*(x-1)) continue;
			result[loop] = 1;
		}
	}
	fclose(fp);

	fp = fopen("C:\\data\\output.txt", "wt");
	for (loop = 0; loop < Loop; loop++)
	{
		if (result[loop]==0)	fprintf(fp, "Case #%d: RICHARD\n", loop + 1);
		else					fprintf(fp, "Case #%d: GABRIEL\n", loop + 1);
	}
	free(result);
	fclose(fp);

	return 0;
}
