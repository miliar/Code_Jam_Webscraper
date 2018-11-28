#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
#include<math.h>
using namespace std;
int t, s[1000], n = -1, k, co = 0;
char a[1000];
bool bo = true;
void inline swap(int j)
{
	for (int a = 0; a < k; a++)
	{
		if (s[j + a] == 1)
			s[j + a] = 0;
		else
			s[j + a] = 1;
	}
}
void main()
{

	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	fin >> t;
	for (int i = 1; i <= t; i++)
	{
		bo = true;
		co = 0;
		fin >> a;
		n = strlen(a);
		for (int j = 0; j < n; j++)
			if (a[j] == '+')
				s[j] = 1;
			else if (a[j] == '-')
				s[j] = 0;
		fin >> k;
		for (int j = 0; j < n; j++)
		{
			if (s[j] == 0)
			{
				if (n - j < k)
				{
					bo = false;
					j = n;
				}
				else
					swap(j);
				co += 1;
			}
		}
		if (bo)
			fout << "Case #" << i << ": " << co << "\n";
		else
			fout << "Case #" << i << ": " << "IMPOSSIBLE" << "\n";
	}
}
