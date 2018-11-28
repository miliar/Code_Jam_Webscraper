#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream inFile;
	ofstream outFile;
	int T, firstAnswer, secondAnswer;
	int firstCards[4][4], secondCards[4][4];
	int theCard;
	int caseIndex, i, j;

	inFile.open("E:\\C++\\GCJ\\Google Code Jam 2014\\Qualification Round\\A Magic Trick\\A-small-attempt1.in");
	outFile.open("E:\\C++\\GCJ\\Google Code Jam 2014\\Qualification Round\\A Magic Trick\\A-small-attempt1.out");

	inFile >> T;
	for (caseIndex = 1; caseIndex <= T; caseIndex++)
	{
		inFile >> firstAnswer;
		for (i = 0; i < 4; i++)
		{
			for (j = 0; j < 4; j++)
			{
				inFile >> firstCards[i][j];
				if (i == firstAnswer - 1)
				{
					cout << firstCards[i][j] << ' ';
				}
			}
		}
		cout << endl;
		inFile >> secondAnswer;
		for (i = 0; i < 4; i++)
		{
			for (j = 0; j < 4; j++)
			{
				inFile >> secondCards[i][j];
				if (i == secondAnswer - 1)
				{
					cout << secondCards[i][j] << ' ';
				}
			}
		}
		cout << endl;

		for (i = 0, theCard = 0; i < 4; i++)
		{
			for (j = 0; j < 4; j++)
			{
				if (firstCards[firstAnswer - 1][i] == secondCards[secondAnswer - 1][j])
				{
					if (theCard != 0)
					{
						cout << "Case #" << caseIndex << ": " << "Bad magician!\n";
						outFile << "Case #" << caseIndex << ": " << "Bad magician!\n";
						goto nextCase;
					}
					theCard = secondCards[secondAnswer - 1][j];
				}
			}
		}//for (i = 0, theCard = 0; i < 4; i++)
		if (theCard == 0)
		{
			cout << "Case #" << caseIndex << ": " << "Volunteer cheated!\n";
			outFile << "Case #" << caseIndex << ": " << "Volunteer cheated!\n";
		}
		else
		{
			cout << "Case #" << caseIndex << ": " << theCard << endl;
			outFile << "Case #" << caseIndex << ": " << theCard << endl;
		}
nextCase:
		;
	}//for (caseIndex = 1; caseIndex <= T; caseIndex++)


	inFile.close();
	outFile.close();

	system("pause");
	return 0;
}