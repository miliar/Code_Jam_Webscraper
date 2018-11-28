#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>

#define mod 1000000007

using namespace std;

FILE *fin, *fout;

void open_files()
{
	int i;
	char path[260];
	gets(path);
	for (i = 0; path[i] && path[i] <= 32; ++i);
	strcpy(path, path + i);
	for (i = strlen(path); --i > 0 && path[i] <= 32;);
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

int n;
char ch_next[128], ch_prev[128], ch_ismiddle[128], mark[128];
int ch_n[128];
int f[128];
int nc, c[128];

int read()
{
	int i, j, len;
	char x[1024], start, end;
	fscanf(fin, " %s", x);
	len = strlen(x);
	start = *x;
	end = x[len - 1];
	if (start == end)
	{
		for (i = 0; x[i]; ++i)
		if (x[i] != start)
			return 0;
		++ch_n[start];
		return 1;
	}
	else
	{
		if (ch_next[start] || ch_prev[end])
			return 0;
		ch_next[start] = end;
		ch_prev[end] = start;
	}
	while (len > 0 && x[len - 1] == end)
		--len;
	for (i = 0; i < len && x[i] == start; ++i);
	for (j = i; j < len; ++j)
	{
		if (i < j && x[j] == x[j - 1])
			continue;
		if (ch_ismiddle[x[j]])
			return 0;
		ch_ismiddle[x[j]] = 1;
	}
	return 1;
}

int main()
{
	int i, j;
	int itest, ntest;
	for (f[i = 0] = 1; ++i < 128;)
		f[i] = i * (long long)f[i - 1] % mod;
	open_files();
	fscanf(fin, "%d", &ntest);
	for (itest = 0; ++itest <= ntest;)
	{
		int bad = 0, res = 0;
		memset(ch_next, 0, sizeof(ch_next));
		memset(ch_prev, 0, sizeof(ch_prev));
		memset(ch_ismiddle, 0, sizeof(ch_ismiddle));
		memset(ch_n, 0, sizeof(ch_n));
		fscanf(fin, "%d", &n);
		for (i = 0; i < n; ++i)
		if (!read())
			bad = 1;
		for (i = 0; i < 128; ++i)
		if (ch_ismiddle[i] && (ch_next[i] || ch_prev[i] || ch_n[i]))
			bad = 1;
		if (!bad)
		{
			nc = 0;
			res = 1;
			memset(mark, 0, sizeof(mark));
			for (i = 0; ++i < 128;)
			if (!ch_prev[i] && !ch_ismiddle[i] && (ch_n[i] || ch_next[i]))
			{
				int t = 1;
				for (j = i; j && !mark[j]; j = ch_next[j])
				{
					mark[j] = 1;
					t = t * (long long)f[ch_n[j]] % mod;
				}
				if (j)
					res = 0;
				++nc;
				res = res * (long long)t % mod;
			}
			res = res * (long long)f[nc] % mod;
			for (i = 0; i < 128; ++i )
			if (!mark[i] && (ch_next[i] || ch_prev[i] || ch_n[i]))
				res = 0;
		}
		fprintf(fout, "Case #%d: %d\n", itest, res);
	}
	return 0;
}
