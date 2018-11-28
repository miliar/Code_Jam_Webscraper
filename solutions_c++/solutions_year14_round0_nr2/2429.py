#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <fstream>
#include <iomanip>
using namespace std;

/*int magic()
{
	fstream fin("A.in");
	fstream fout("O.txt");
	int T;
	fin >> T;
	for (int i = 1; i <= T; i++)
	{
		int ans1, ans2;		
		int M1[4][4], M2[4][4];

		fin >> ans1;
		ans1--;
		for (int p = 0; p < 4; p++)
			for (int q = 0; q < 4; q++)
				fin >> M1[p][q];

		fin >> ans2;
		ans2--;
		for (int p = 0; p < 4; p++)
			for (int q = 0; q < 4; q++)
				fin >> M2[p][q];

		int flag = 0;
		int result = 0;
		for (int p = 0; p < 4; p++)
			for (int q = 0; q < 4; q++)
			{
				if (M1[ans1][p] == M2[ans2][q])
				{
					flag++;
					result = M1[ans1][p];
				}
			}
		if (flag == 0)
			fout << "Case #" << i << ": Volunteer cheated!\n";
		else if (flag == 1)
			fout << "Case #" << i << ": " << result << endl;
		else
			fout << "Case #" << i << ": Bad magician!\n";
	}
	return 0;
}*/

int cookie()
{
	fstream fin("B.in");
	fstream fout("O.txt");
	int T;
	fin >> T;
	for (int i = 1; i <= T; i++)
	{
		double C, F, X, R = 2.0, Time = 0.0;
		fin >> C >> F >> X;
		while (X / R > (C / R) + (X / (R + F)))
		{
			Time += C/R;
			R = R + F;
		}
		Time += X / R;
		fout.precision(7);
		fout << std::fixed << "Case #" << i << ": " << Time << endl;
	}
	return 0;
}