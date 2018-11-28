// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int cnt;

	ifstream f("in.txt");
	ofstream fo("out.txt");

	f >> cnt;
	for (int i = 0; i < cnt; i++)
	{
		int a,b;
		int x[4][4];
		int y[4][4];
		f >> a;
		for(int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				f >> x[j][k];
			}
		}
		f >> b;
		for(int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				f >> y[j][k];
			}
		}
		
		int z_cnt = 0;
		int z_val = 0;
		for(int j = 0; j < 4; j++)
		{
			if ((x[a-1][j] == y[b-1][0]) || (x[a-1][j] == y[b-1][1]) || (x[a-1][j] == y[b-1][2]) || (x[a-1][j] == y[b-1][3]))
			{
				z_cnt++;
				z_val = x[a-1][j];
			}
		}
		if (z_cnt == 0)
		{
			fo << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		}
		else if (z_cnt > 1)
		{
			fo << "Case #" << i+1 << ": Bad magician!" << endl;
		}
		else
		{
			fo << "Case #" << i+1 << ": " << z_val << endl;
		}
	}

	f.close();
	fo.close();

	return 0;
}

