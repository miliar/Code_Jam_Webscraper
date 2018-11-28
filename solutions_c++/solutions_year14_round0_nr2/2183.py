// googlecodejam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

using namespace std;

bool MagicTrick()
{
	ifstream fin("A-small-attempt1.in");
	ofstream fout("outmagic.txt");

	int T = 0;
	fin >> T;

	int cards1[4][4] = {{0}};
	int cards2[4][4] = {{0}};

	for (int t = 0; t < T; t++)
	{
		int row1 = 0, row2 = 0;
		int num = -1; //positive for common, 0 for Bad magician and -1 for cheated

		fin >> row1;
		row1--; //the num array index start from 0;
		for (int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				fin >> cards1[i][j];

		fin >> row2;
		row2--;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				fin >> cards2[i][j];

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (cards1[row1][i] == cards2[row2][j])
				{
					if (num > 0)	//repeated, Bad magician
					{
						num = 0;
					}
					else
					{
						num = cards1[row1][i];
					}
					break;					
				}
			}
			if (num == 0)
			{
				break;
			}
		}

		fout << "Case #" << t + 1 << ": ";
		if (num > 0)
		{
			fout << num;
		}
		else if (num == 0)
		{
			fout << "Bad magician!";
		}
		else
		{
			fout << "Volunteer cheated!";
		}
		fout << endl;

		cout << "Case #" << t + 1 << ": ";
		if (num > 0)
		{
			cout << num;
		}
		else if (num == 0)
		{
			cout << "Bad magician!";
		}
		else
		{
			cout << "Volunteer cheated!";
		}
		cout << endl;
	}


	return true;
}

bool CookieClicker()
{
	ifstream fin("B-large.in");
	ofstream fout("outb.txt");

	//show 7 decimal places
	fout.setf(ios::showpoint | ios::fixed);
	fout.precision(7);

	cout.setf(ios::showpoint | ios::fixed);
	cout.precision(7);

	int T = 0;
	fin >> T;

	for (int t = 0; t < T; t++)
	{
		double C = 0, F = 0, X = 0;
		fin >> C >> F >> X;

		double v = 2;

		if (X < C)
		{
			cout << "Case #" << t + 1 << ": " << X/v << endl;
			fout << "Case #" << t + 1 << ": " << X/v << endl;
			continue;
		}

		double y = 0;
		bool isbuy = true;

		while(isbuy) 
		{
			y += C/v;

			double t1 = (X - C) / v;

			v += F;
			double t2 = X / v;

			if (t1 < t2)
			{
				isbuy = false;
				y += t1;
			} 
		}

		cout << "Case #" << t + 1 << ": " << y << endl;
		fout << "Case #" << t + 1 << ": " << y << endl;
	}

	return true;
}
int _tmain(int argc, _TCHAR* argv[])
{
	//MagicTrick();

	CookieClicker();

	return 0;
}

