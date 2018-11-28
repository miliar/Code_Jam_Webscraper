#include <fstream>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int grid[4][4];
int ok[17];

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t; fin >> t;

	for (int i = 1; i <= t; i++)
	{
		for (int j = 1; j <= 16; j++)
			ok[j] = 0;

		int r1; fin >> r1;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				fin >> grid[j][k];
		
		for (int j = 0; j < 4; j++)
			ok[grid[r1 - 1][j]]++;

		int r2; fin >> r2;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				fin >> grid[j][k];

		for (int j = 0; j < 4; j++)
			ok[grid[r2 - 1][j]]++;

		int total = 0;
		for (int j = 1; j <= 16; j++)
			if (ok[j] == 2)
				total++;

		if (total == 0)
		{
			fout << "Case #" << i << ": Volunteer cheated!\n";
		}
		else if (total >= 2)
		{
			fout << "Case #" << i << ": Bad magician!\n";
		}
		else
		{
			for (int j = 1; j <= 16; j++)
				if (ok[j] == 2)
					fout << "Case #" << i << ": " << j << "\n";
		}
	}

}