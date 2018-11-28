/*
 * main.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: hades
 */

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("A-small-attempt1.in");
	ofstream fout("A-small-attempt1.out");

	//ifstream fin("magictrick.inp");
	//ofstream fout("magictrick.out");

	int T;
	fin >> T;

	for (int k = 0; k < T; k ++)
	{
		int row1, row2;
		int a1[10][10];
		int a2[10][10];

		int result = 0;
		int data = 0;

		fin >> row1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				fin >> a1[i][j];

		fin >> row2;
		for (int i = 0; i < 4; i++)
					for (int j = 0; j < 4; j++)
						fin >> a2[i][j];

		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			if (a1[row1-1][i] == a2[row2-1][j])
			{
				result += 1;
				data = a1[row1-1][i];
			}

		fout << "Case #" << (k+1) << ": ";

		if (result == 0)
			fout << "Volunteer cheated!" << endl;
		else if (result > 1)
			fout << "Bad magician!" << endl;
		else
			fout << data << endl;
	}
	return 0;
}


