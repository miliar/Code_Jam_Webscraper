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
	int t, n, p, k, f, c, s;
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	fin >> t;
	for (int i = 1; i <= t; i++)
	{
		fout << "Case #" << i << ":";
		fin >> k >> c >> s;
		if (s < k&&c == 1)
			fout << " IMMPOSIBLE\n";
		else if (s < (k / 2 + k % 2))
			fout << " IMMPOSIBLE\n";
		else if (k == 1)
			fout <<" "<< 1 << "\n";
		else
		{
			if (c == 1)
			{
				for (int x = 0; x < k; x++)
					fout << " " << x + 1;
				fout << "\n";
			}
			else
			{
				for (int x = 0; x < (k / 2); x++)
				{
					fout << " "<<x * 2*k + 2*(x+1);
				}
				if (k % 2 != 0)
					fout << " " << pow(k, 2);
				fout << "\n";
			}
		}
		
			

	}
}