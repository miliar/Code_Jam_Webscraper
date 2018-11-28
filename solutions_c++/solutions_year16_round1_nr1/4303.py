#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
#include<math.h>
using namespace std;
int al[100][100], an[100][100], r, c, m;
long long no;
int co[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
bool ch = false;

void main()
{
	long long t, n, p, j = 1, i, temp;
	long long k;
	char c;
	char s[1000], f[2001];
	int co1[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	fin >> t;

	for (i = 1; i <= t; i++)
	{
		fout << "Case #" << i << ": ";
		fin >> s;
		n = strlen(s);
		f[1000] = s[0];
		int cou = 1000, max = 1000, min = 1000;
		for (j = 1; j < n; j++)
		{
			if (int(f[min] - s[j]) <= int(s[j] - f[min]))
			{
				--min;
				f[min] = s[j];
			}
			else
			{
				++max;
				f[max] = s[j];
			}

		}
		for (int x = min; x <= max; x++)
			fout << f[x];
		fout << "\n";
	}
	fin.close();
	fout.close();
}
