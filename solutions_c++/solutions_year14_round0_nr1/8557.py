#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int n;
int a[4][4];
int b[4][4];

int main()
{
	int i, j;
	char path[260];
	FILE *fin, *fout;
	gets(path);
	if (*path == '\'' || *path == '"')
	{
		for (i = strlen(path); path[--i] != *path;);
		path[i] = 0;
		strcpy(path, path + 1);
	}
	fin = fopen(path, "r");
	strcat(path, ".out");
	fout = fopen(path, "w");
	int itest, ntest;
	fscanf(fin, "%d", &ntest);
	for (itest = 0; ++itest <= ntest;)
	{
		int row, res = (1 << 17) - 2;
		for (j = 0; j < 2; ++j)
		{
			fscanf(fin, "%d", &row);
			--row;
			for (i = 0; i < 16; ++i)
			{
				int x;
				fscanf(fin, "%d", &x);
				if (i / 4 != row)
					res &= ~(1 << x);
				//printf("res = %d\n", res);
			}
		}
		fprintf(fout, "Case #%d: ", itest);
		if (!res)
			fprintf(fout, "Volunteer cheated!\n");
		else if ((res & -res) != res)
			fprintf(fout, "Bad magician!\n");
		else
		{
			for (i = 0; (1 << i) < res; ++i);
			fprintf(fout, "%d\n", i);
		}
	}
	return 0;
}
