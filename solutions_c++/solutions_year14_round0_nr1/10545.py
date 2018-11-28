#include <iostream>

using namespace std;

void readTo(unsigned int b[4][4]);

int main()
{
	unsigned int T; // number of test cases
	unsigned int firstPick, secondPick; // voluteer picks
	unsigned int firstBoard[4][4];
	unsigned int secondBoard[4][4];
	unsigned int possibleNum[4];
	unsigned int rowOfNum[4];
	unsigned int selectedNum;
	bool isBad;
	bool isCheated;
	
	cin >> T;

	for (unsigned int t = 1; t <= T; t++)
	{
		isBad = false;
		isCheated = true;
		
		cin >> firstPick; // read first pick
		readTo(firstBoard); // read first board
		
		// transfer possible numbers
		for (unsigned int i = 0; i < 4; i++)
			possibleNum[i] = firstBoard[firstPick - 1][i];
		
		cin >> secondPick; // read second pick
		readTo(secondBoard); // read second board
		
		// search for all possible numbers
		// consumes O(n^3) in time but efficient
		// enough for small dataset
		for (unsigned int i = 0; i < 4; i++)
			for (unsigned int k = 0; k < 4; k++)
				for (unsigned int m = 0; m < 4; m++)
					if (possibleNum[m] == secondBoard[i][k])
						rowOfNum[m] = i + 1;
		
		// check is the magician is bad guy
		unsigned int count = 0;
		for (unsigned int i = 0; i < 4; i++)
			if (rowOfNum[i] == secondPick)
				count++;

		if (count > 1)
			isBad = true;
		
		// check is the volunteer is trying to cheat
		for (unsigned int i = 0; i < 4; i++)
		{
			if (secondPick == rowOfNum[i])
			{
				isCheated = false;
				selectedNum = possibleNum[i];
			}
		}
		
		cout << "Case #" << t << ": ";
		
		if (isBad)
			cout << "Bad magician!";
		else if (isCheated)
			cout << "Volunteer cheated!";
		else
			cout << selectedNum;
		
		cout << "\n";
	}
	
	return 0;
}

void readTo(unsigned int b[4][4])
{
	for (unsigned int i = 0; i < 4; i++)
	{
		for (unsigned int k = 0; k < 4; k++)
		{
			cin >> b[i][k];
		}
	}
}
