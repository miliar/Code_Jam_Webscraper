#include <iostream>
#include <fstream>
using namespace std;

void main(){

	ifstream inFile;
	ofstream outFile;

	inFile.open("a-small.txt");
	outFile.open("out-small.txt");

	int c = 0;
	int row;
	int number[4];
	int number1[4];
	int dummy;

	inFile >> c;

	for (int i = 0; i < c; i++)
	{
		inFile >> row;
		row--;

		for (int j = 0; j < 4; j++)
		{
			if (j == row)
			{
				inFile >> number[0] >> number[1] >> number[2] >> number[3];
			}
			else
			{
				inFile >> dummy >> dummy >> dummy >> dummy;
			}
		}

		inFile >> row;
		row--;

		for (int j = 0; j < 4; j++)
		{
			if (j == row)
			{
				inFile >> number1[0] >> number1[1] >> number1[2] >> number1[3];
			}
			else
			{
				inFile >> dummy >> dummy >> dummy >> dummy;
			}
		}

		int correctNumber = 0;
		int occurance = 0;

		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (number[j] == number1[k])
				{
					correctNumber = number[j];
					occurance++;
				}

			}
		}

		outFile << "Case #" << i + 1 << ": ";
		if (occurance == 0)
			outFile << "Volunteer cheated!" << endl ;
		else if (occurance > 1)
			outFile << "Bad magician!" << endl;
		else
			outFile << correctNumber << endl;
	}

	inFile.close();
	outFile.close();
}