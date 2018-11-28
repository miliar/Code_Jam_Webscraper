#include <stdio.h>

int main()
{
	int ii, test, l, r, i, len, ans;
	char c, list[101], tmp[101];
	FILE *fp_w, *fp_r;
	fp_w = fopen("BL_output.txt", "w");
	fp_r = fopen("B-large.in", "r");

	fscanf(fp_r, "%d", &test);
	fscanf(fp_r, "%c", &c);
	for (ii = 1;ii <= test;ii++)
	{
		fprintf(fp_w, "CASE #%d: ", ii);
		fscanf(fp_r, "%s", list);
		fscanf(fp_r, "%c", &c);
		ans = 0;
		for (i = 0;list[i] != NULL;i++);
		len = i;
		r = len - 1;
		if (len == 1)
		{
			if (list[0] == '+')
				fprintf(fp_w, "0\n");
			else
				fprintf(fp_w, "1\n");
			continue;
		}
		while (r >= 0)
		{
			if (list[r] == '+')
			{
				r--;
				continue;
			}
			if (list[0] == '-')
			{
				ans++;
				for (i = 0;i <= r;i++)
					tmp[r - i] = list[i];
				for (i = 0;i <= r;i++)
				{
					if (tmp[i] == '+')
						list[i] = '-';
					else
						list[i] = '+';
				}
			}
			else
			{
				ans++;
				l = 0;
				while (list[l] == '+')
					list[l++] = '-';
			}
		}
		fprintf(fp_w, "%d\n", ans);
	}



	fclose(fp_w);
	fclose(fp_r);
	return 0;
}