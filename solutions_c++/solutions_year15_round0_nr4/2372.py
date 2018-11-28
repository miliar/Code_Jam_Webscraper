#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
#include<math.h>
using namespace std;
void main()
{
	int t, n, p, d, x, y,s;
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	fin >> t;
	for (int i = 1; i <= t; i++)
	{
		fin >> n >> x >> y;
		if (n == 1)
		{
			fout << "Case #" << i << ": GABRIEL\n";
			continue;
		}
		if (n == 2 && (x % 2 == 0 || y % 2 == 0))
		{
			fout << "Case #" << i << ": GABRIEL\n";
			continue;
		}
		if (n>=7)
		{
			fout << "Case #" << i << ": RICHARD\n";
			continue;
		}
		if (x < n&&y < n)
		{
			fout << "Case #" << i << ": RICHARD\n";
			continue;
		}
		if ((x*y) % n != 0)
		{
			fout << "Case #" << i << ": RICHARD\n";
			continue;
		}
		if ((x)<(n / 2 + n % 2)||(y)<(n / 2 + n % 2))
		{
			
			fout << "Case #" << i << ": RICHARD\n";
			continue;
		}
		p = y;
		s = x;
		if (x < y)
		{
			p = x;
			s = y;
		}
		if (p<n&&s%n==0&&n>=4)
		{
			if (n == 4 && (p == 3))
			{
				fout << "Case #" << i << ": GABRIEL\n";
				continue;
			}
			else	if (n == 5 && (p >= 4))
			{
				fout << "Case #" << i << ": GABRIEL\n";
					continue;
			}
			else	if (n == 6 && (p >= 4))
			{
				fout << "Case #" << i << ": GABRIEL\n";
				continue;
			}
			else
			{
				fout << "Case #" << i << ": RICHARD\n";
				continue;
			}

		}
		fout << "Case #" << i << ": GABRIEL\n";
		continue;
	}
	
}
