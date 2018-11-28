#include <fstream>
#include <iostream>
#include <vector>

using namespace std;
int main()
{
	ifstream fin("A-small-attempt0 (1).in");
	ofstream fout("output.out");
	int cases;
	fin >> cases;
	int ans1, ans2;
	int numbers[4][4];
	int numbers2[4][4];

	for (int i = 0; i < cases; ++i)
	{
		fin >> ans1;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				fin >> numbers[j][k];
			}
		}
		vector<int> line1(4);
		for (int j = 0; j < 4; ++j)
		{
			line1.at(j) = numbers[ans1 - 1][j];
		}
		fin >> ans2;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				fin >> numbers2[j][k];
			}
		}
		vector<int> line2(4);
		for (int j = 0; j < 4; ++j)
		{
			line2.at(j) = numbers2[ans2 - 1][j];
		}
		int matching = 0;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				if (line1.at(j) == line2.at(k))
					++matching;
			}
		}
		if (matching > 1)
			fout << "Case #" << i + 1 << ": Bad magician!\n";
		else if (matching == 0)
			fout << "Case #" << i + 1 << ": Volunteer cheated!\n";
		else
		{
			for (int j = 0; j < 4; ++j)
			{
				for (int k = 0; k < 4; ++k)
				{
					if (line1.at(j) == line2.at(k))
						matching = line1.at(j);
				}
			}
			fout << "Case #" << i + 1 << ": " << matching << "\n";
		}
	}
	fout.close();
	fin.close();
	return 0;
}