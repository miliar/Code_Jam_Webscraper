#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
#include<math.h>
using namespace std;
int l, d, n, t, len;
char a[100], b[100], o;
void main()
{
	int t, n, p, s, j, i, temp;
	double k;
	double count=0;
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	fin >> t;
	for (i = 1; i <= t; i++)
	{
			fin >> a;
		j=strlen(a);
		fout << "Case #" << i << ": ";
		for (s = 0; s < j-1; s++)
		{
			if (a[s] !=a[s + 1])
			{
				count = count + 1;
			}
		}
		if (a[j - 1] == '-')
			count += 1;
		fout << count << "\n";
		count = 0;
	}
}