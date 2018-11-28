#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
using namespace std;
void main()
{
	int t, n, p, k, f,c;
	char s[1000];
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	fin >> t;
	for (int i = 1; i <= t; i++)
	{
		f = 0;
		p = 0;
		c = 0;
		fin >> k;
		for (int j = 0; j <= k; j++)
		{
			fin >> s[j];

		}
		for (int j = 0; j <= k; j++)
		{
			if (p < j)
			{
				
				f = f + (j - p);
			}
			p = p + int(s[j])-48+ f-c;
			c = f;		
		}
		fout <<"Case #"<< i << ": " << f<<"\n";
	}
}