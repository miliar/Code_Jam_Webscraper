#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

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
		double c, f, x, g, res, t = 0;
		fscanf(fin, "%lf%lf%lf", &c, &f, &x);
		g = 2;
		res = x / g;
		while (t < res)
		{
			t += c / g;
			g += f;
			res = min(res, t + x / g);
		}
		fprintf(fout, "Case #%d: %.7lf\n", itest, res);
	}
	return 0;
}
