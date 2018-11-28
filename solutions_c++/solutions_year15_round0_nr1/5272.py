#include <cstdio>

int main()
{
	FILE *fin, *fout;
	int friendNum, audienceNum, t, smax;
	char str[1005];

	fin = fopen("a.in", "r");
	fout = fopen("a.out", "w");

	fscanf(fin, "%d", &t);
	for (int k = 0; k < t; k++)
	{
		fscanf(fin, "%d %s", &smax, str);
		friendNum = 0;
		audienceNum = 0;
		for (int i = 0; i <= smax; i++)
		{
			if (str[i] == '0')
				continue;
			if (audienceNum >= i)
				audienceNum += str[i] - '0';
			else
			{
				friendNum += i - audienceNum;
				audienceNum = i + str[i] - '0';
			}
		}
		fprintf(fout, "Case #%d: %d\n", k + 1, friendNum);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}