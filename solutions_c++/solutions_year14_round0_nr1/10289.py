// gcj_1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <conio.h>

using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("A-small-attempt3.in");
	out.open("sub.out");

	int n;
	int a[4][4];
	int b[4][4];
	int f_r, s_r;

	in >> n;
	for (int p = 0; p < n; p++)
	{
		in >> f_r;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> a[i][j];
			}
		}
		in >> s_r;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> b[i][j];
			}
		}
		int bm = 0,number=0;

		f_r--;
		s_r--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (a[f_r][i] == b[s_r][j])
				{
					bm++;
					number = a[f_r][i];
				}
			}
		}
		if (number == 0) out << "Case #" << (p+1) << ": Volunteer cheated!"<<endl;
		else if (bm>1) out << "Case #" << (p + 1) << ": Bad magician!" << endl;
		else out << "Case #" << (p + 1) <<": "<<number<< endl;
	}
	in.close();
	out.close();
	return 0;
}

