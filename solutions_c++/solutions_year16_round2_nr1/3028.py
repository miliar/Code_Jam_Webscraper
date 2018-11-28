#include <stdio.h>

int index, index2, index3;

int min(int a, int b, int c, int aa, int bb, int cc)
{
	if (a <= b && a <= c)
	{
		index = aa;
		index2 = bb;
		index3 = cc;
		return a;
	}
	if (b <= c && b <= a)
	{
		index = bb;
		index2 = aa;
		index3 = cc;
		return b;
	}
	if (c <= a && c <= b)
	{
		index = cc;
		index2 = bb;
		index3 = aa;
		return c;
	}
}

int main()
{
	FILE *fpw, *fpr;
	int ii, test, i, j, list[26], len, ans[26];
	char c, str[2002];
	fpw = fopen("AL_output.txt", "w");
	fpr = fopen("A-large.in", "r");


	fscanf(fpr, "%d", &test);
	fscanf(fpr, "%c", &c);
	for (ii = 1;ii <= test;ii++)
	{
		fprintf(fpw, "Case #%d: ", ii);
		fscanf(fpr, "%s", str);
		fscanf(fpr, "%c", &c);
		for (i = 0;i < 26;i++) {
			list[i] = 0;
			ans[i] = 0;
		}
		for (i = 0;str[i] != NULL;i++);
		len = i;
		for (i = 0;i < len;i++)
			list[(int)str[i] - 'A']++;
		if (list[25] > 0) //0
		{
			j = list[25];
			list[25] = 0;
			list['E' - 'A'] -= j;
			list['R' - 'A'] -= j;
			list['O' - 'A'] -= j;
			ans[0] = j;
		}
		if (list[22] > 0) //2
		{
			j = list[22];
			list[22] = 0;
			list['T' - 'A'] -= j;
			list['O' - 'A'] -= j;
			ans[2] = j;
		}
		if (list[20] > 0) //4
		{
			j = list[20];
			list[20] = 0;
			list['F' - 'A'] -= j;
			list['O' - 'A'] -= j;
			list['R' - 'A'] -= j;
			ans[4] = j;
		}
		if (list[23] > 0) //6
		{
			j = list[23];
			list[23] = 0;
			list['I' - 'A'] -= j;
			list['S' - 'A'] -= j;
			ans[6] = j;
		}
		if (list[14] > 0) //1
		{
			j = list[14];
			list[14] = 0;
			list['N' - 'A'] -= j;
			list['E' - 'A'] -= j;
			ans[1] = j;
		}
		if (list[5] > 0) //5
		{
			j = list[5];
			list[5] = 0;
			list['I' - 'A'] -= j;
			list['V' - 'A'] -= j;
			list['E' - 'A'] -= j;
			ans[5] = j;
		}
		if (list[21] > 0) //7
		{
			j = list[21];
			list[21] = 0;
			list['S' - 'A'] -= j;
			list['E' - 'A'] -= (j * 2);
			list['N' - 'A'] -= j;
			ans[7] = j;
		}
		if (list[6] > 0) //8
		{
			j = list[6];
			list[6] = 0;
			list['E' - 'A'] -= j;
			list['I' - 'A'] -= j;
			list['H' - 'A'] -= j;
			list['T' - 'A'] -= j;
			ans[8] = j;
		}
		if (list[13] > 0) //9
		{
			j = list[13] / 2;
			list[13] = 0;
			list['I' - 'A'] -= j;
			list['E' - 'A'] -= j;
			ans[9] = j;
		}
		ans[3] = list[19];
		for (i = 0;i < 10;i++)
			for (j = 0;j < ans[i];j++)
				fprintf(fpw, "%d", i);
		fprintf(fpw, "\n");
	}
	return 0;
}