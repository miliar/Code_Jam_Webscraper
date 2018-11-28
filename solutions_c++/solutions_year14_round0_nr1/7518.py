// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("A.in");
	ofstream fout("A.out");

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++)
	{
		fout << "Case #" << t << ": ";

		int selected[2][4];

		{
			int rows[4][4];
			int index;
			fin >> index; index--;

			for (int i = 0; i < 4; i++)
				for (int j = 0; j < 4; j++)
					fin >> rows[i][j];

			copy(rows[index], rows[index]+4, selected[0]);
		}

		{
			int rows[4][4];
			int index;
			fin >> index; index--;

			for (int i = 0; i < 4; i++)
				for (int j = 0; j < 4; j++)
					fin >> rows[i][j];

			copy(rows[index], rows[index] + 4, selected[1]);
		}

		bool one = false;
		int res;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (selected[0][i] == selected[1][j])
				{
					if (one)
					{
						fout << "Bad magician!\n";
						goto exit;
					}
					else
					{
						res = selected[0][i];
						one = true;
					}
				}
			}
		}

	if (!one)
		fout << "Volunteer cheated!\n";
	else
		fout << res << endl;

	exit:
		continue;
	}

	return 0;
}

