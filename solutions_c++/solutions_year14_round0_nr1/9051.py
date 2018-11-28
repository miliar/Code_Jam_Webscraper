#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	int test_cases = 0, entry, ***cards, *answers[2], test_row[2][4], ans[2], index, count = 0;
	ifstream fin("A-small-attempt0 (1).in");
	ofstream fout("output.txt");
	int total_count = 0;
	fin >> test_cases;
	cards = new int **[2];

	for (int i = 0; i < 2; i++)
	{
		cards[i] = new int *[4];
		for (int j = 0; j < 4; j++)
			cards[i][j] = new int[4];
	}

	if (test_cases >= 1 && test_cases <= 100)
	{	
		for (int z = 0; z < test_cases;z++)
		{
			
			for (int i = 0; i < 2; i++)
			{
				fin >> ans[i];
				for (int j = 0; j < 4; j++)
					for (int k = 0; k < 4; k++)
					{
						fin >> cards[i][j][k];
						if (j  == ans[i]-1)
							test_row[i][k] = cards[i][j][k];

					}

			}
			
			for (int i = 0; i < 4; i++)
			{
				for (int j = 0; j < 4; j++)
				if (test_row[0][i] == test_row[1][j])
				{
					count++;
					index = test_row[0][i];
				}
			}
			if (count == 1)
				fout << "Case #" <<z+1<< ": " << index << endl;
			else if (count>1)
				fout << "Case #" << z + 1 << ": " << "Bad magician!" << endl;
			else if (count == 0)
				fout << "Case #" << z + 1 << ": " << "Volunteer cheated!" << endl;
			count = 0;
		}

	}
	return 0;
}