// ConsoleApplication1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;


int main()
{
	ifstream fin("A-large.in");
	ofstream fout("out.txt");
	int T;
	fin >> T;
	for (int t = 1;t <= T;t++)
	{
		int n;
		fin >> n;
		int *p = new int[n];
		int nonull = 0;
		int max = -1, prmax = 0;
		int i_max = -1,i_prmax=-1;
		for (int i = 0;i < n;i++)
		{
			fin >> p[i];
		}
		fout << "Case #" << t << ": ";
		while (max != 0)
		{
			max = 0, i_max = -1;
			prmax = 0, i_prmax = -1;
			nonull = 0;
			for (int i = 0;i < n;i++)
			{
				if (p[i] > 0) nonull++;
				if (p[i] > max)
				{
					prmax = max;
					i_prmax = i_max;
					max = p[i];
					i_max = i;
				}
				else if (p[i] > prmax)
				{
					prmax = p[i];
					i_prmax = i;
				}
			}
			if ((max == 2 && prmax==1 && nonull%2==0)|| (max == 1 && prmax == 1 && nonull%2 == 1))
			{
				fout << (char)('A' + i_max);
				p[i_max]--;
				fout << ' ';
			}
			else if (i_max != -1) {
				if (i_prmax == -1) { fout << (char)('A' + i_max);p[i_max]--;}
				else { fout << (char)('A' + i_max) << (char)('A' + i_prmax);p[i_max]--, p[i_prmax]--;}
				fout << ' ';
			}
			/*int sum = 0;
			for (int o = 0;o < n;o++)
				sum += p[o];
			for (int o = 0;o < n;o++)
				if (sum != 0 && p[o] / sum>0.5)
				{
					cout << endl;
					for (int j = 0;j < n;j++)
						cout << p[j] << ' ';
					cout << endl << o <<"___"<<t<< endl;
				}*/
		}
		fout << endl;
	}
	fout.close();
    return 0;
}

