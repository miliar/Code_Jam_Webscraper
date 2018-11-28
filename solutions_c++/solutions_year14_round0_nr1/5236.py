#include<stdio.h>
int main(void)
{
	int T, tmp, tmp2, arr[16], count, num;
	FILE *fp, *fp2;
	fp = fopen("A-small-attempt2.in", "rt");
	fp2 = fopen("output.txt", "wt");
	fscanf(fp, "%d", &T);
	for (int i = 0; i < T; i++)
	{
		count = 0;
		for (int j = 0; j < 16; j++)
			arr[j] = 0;
		fscanf(fp, "%d", &tmp);
		tmp--;
		for (int j = 0; j < 16; j++)
		{
			fscanf(fp, "%d", &tmp2);
			if (j / 4 == tmp)
				arr[tmp2-1] = 1;
		}
		fscanf(fp, "%d", &tmp);
		tmp--;
		for (int j = 0; j < 16; j++)
		{
			fscanf(fp, "%d", &tmp2);
			if (j / 4 == tmp && arr[tmp2-1] == 1)
			{
				count++;
				num = tmp2;
			}
		}
		if (count == 0)
			fprintf(fp2, "Case #%d: Volunteer cheated!\n", i + 1);
		else if (count == 1)
			fprintf(fp2, "Case #%d: %d\n", i + 1, num);
		else
			fprintf(fp2, "Case #%d: Bad magician!\n", i + 1);
	}
	fclose(fp);
	fclose(fp2);

	return 0;
}