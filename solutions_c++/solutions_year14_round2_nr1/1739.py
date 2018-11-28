#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

int n, b[1024];
char a[1024][1024], *pa[1024];

int main()
{
	char path[260];
	gets(path);
	ifstream fin(path);
	strcat(path, ".out");
	ofstream fout(path);
	int itest, ntest;
	fin >> ntest;
	for (itest = 0; ++itest <= ntest;)
	{
		fin >> n;
		int i, j, res = 0;
		for (i = 0; i < n; ++i)
			fin >> (pa[i] = a[i]);
		while (**pa)
		{
			char ch = **pa;
			for (i = 0; ++i < n && *pa[i] == ch;);
			if (i < n)
				break;
			for (i = 0; i < n; ++i)
			{
				for (j = 0; *pa[i] == ch; ++pa[i])
					++j;
				b[i] = j;
			}
			sort(b, b + n);
			j = b[n >> 1];
			for (i = 0; i < n; ++i)
				res += abs(b[i] - j);
		}
		fout << "Case #" << itest << ": ";
		for (i = 0; i < n && !*pa[i]; ++i);
		if (i < n)
			fout << "Fegla Won";
		else
			fout << res;
		fout << endl;
	}
	return 0;
}
