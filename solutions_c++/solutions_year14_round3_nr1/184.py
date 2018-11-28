#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

FILE *fin, *fout;

void open_files()
{
	int i;
	char path[260];
	gets(path);
	for (i = 0; path[i] && path[i] <= 32; ++i);
	strcpy(path, path + i);
	for (i = strlen(path); --i >= 0 && path[i] <= 32;);
	path[i + 1] = 0;
	if (*path == '\'' || *path == '"')
	{
		strcpy(path, path + 1);
		path[strlen(path) - 1] = 0;
	}
	fin = fopen(path, "r");
	strcat(path, ".out");
	fout = fopen(path, "w");
}

long long gcd(long long a, long long b)
{
	long long t;
	if (a < b)
		t = a, a = b, b = t;
	while (b)
		t = a % b, a = b, b = t;
	return a;
}

int main()
{
	int itest, ntest;
	open_files();
	fscanf(fin, "%d", &ntest);
	for (itest = 0; ++itest <= ntest;)
	{
		int i, j;
		long long p, q, d;
		fscanf(fin, "%lld/%lld", &p, &q);
		d = gcd(p, q);
		p /= d;
		q /= d;
		fprintf(fout, "Case #%d: ", itest);
		if (q != (q & -q))
			fprintf(fout, "impossible\n");
		else
		{
			for (i = j = 0; q >> i; ++i);
			while (!(p >> --i & 1))
				++j;
			fprintf(fout, "%d\n", j);
		}
	}
	return 0;
}
