#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("A-small-attempt0.in"); 
	ofstream fout("output.txt");
	int instance;
	fin >> instance;
	int deck_a[4][4];
	int deck_b[4][4];
	for (int x = 0; x < instance; x++)
	{
		int first;
		fin >> first;
		for (int i = 0; i < 4; i++)
		{
			fin >> deck_a[i][0] >> deck_a[i][1] >> deck_a[i][2] >> deck_a[i][3];
		}

		int second;
		fin >> second;
		for (int i = 0; i < 4; i++)
		{
			fin >> deck_b[i][0] >> deck_b[i][1] >> deck_b[i][2] >> deck_b[i][3];
		}

		int row[4];
		for (int i = 0; i < 4; i++)
		{
			row[i] = deck_a[first - 1][i];
		}
		bool answer = false;
		bool cheated = false;
		int answervalue;
		int seconda[4];
		for (int i = 0; i < 4; i++)
		{
			seconda[i] = deck_b[second - 1][i];
		}
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (row[i] == seconda[j])
				{
					if (answer)
					{
						cheated = true;
					}

					if (!answer)
					{
						answer = true;
						answervalue = row[i];
					}

					
					//then you found the answer, just implement bool values
				}
			}
		}

		if (cheated)
		{
			fout << "Case #" << x + 1<< ": Bad magician!" << endl;
			cheated = false;
			answer = false;
			continue;
		}

		if (answer)
		{
			fout << "Case #" << x + 1 << ": " << answervalue << endl;
			cheated = false;
			answer = false;
		}

		else if (!answer)
		{
			fout << "Case #" << x + 1 << ": " << "Volunteer cheated!" << endl;
			cheated = false;
			answer = false;
		}

		
	}
	system("PAUSE");
	return 0;
}