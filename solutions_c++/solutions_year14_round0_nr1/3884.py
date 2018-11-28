#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");
	int t, a1, a2;
	int g1[4][4], g2[4][4];
	fin >> t;
	for (int urns = 0; urns < t; ++urns)
	{
		fout << "Case #" << urns+1 << ": ";
		fin >> a1;
		for (int j = 0; j < 4; ++j)
			for (int i = 0; i < 4; ++i)
				fin >> g1[j][i];
		fin >> a2;
		for (int j = 0; j < 4; ++j)
			for (int i = 0; i < 4; ++i)
				fin >> g2[j][i];
		--a1;
		--a2;
		int ans = -1;
		for (int i = 0; i < 4 && ans != 50; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				if (g1[a1][i] == g2[a2][j])
				{
					if (ans != -1)
					{
						ans = 50;
						break;
					}
					ans = g1[a1][i];
				}
			}
		}

		if (ans == -1) fout << "Volunteer cheated!" << endl;
		else if (ans == 50) fout << "Bad magician!" << endl;
		else fout << ans << endl;

	}
}
