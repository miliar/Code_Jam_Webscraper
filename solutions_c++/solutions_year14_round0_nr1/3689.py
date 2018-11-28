#include <iostream>
#include <fstream>

using namespace std;
int main(void)
{
	ifstream input;
	ofstream output;
	input.open("input.txt");
	output.open("output.txt");

	int textCases;

	input >> textCases;

	for (int testCase = 1; testCase <= textCases; testCase++)
	{
		int rowNumber;
		int skip;
		int numbersInRows[2][4];
		int numberOfMatches = 0;
		int matchedNumber;

		input >> rowNumber;

		if (rowNumber > 1){
			for (int i = 0; i < (rowNumber - 1) * 4; i++)
			{
				input >> skip;
			}
		}

		for (int i = 0; i < 4; i++)
		{
			input >> numbersInRows[0][i];
		}

		if (rowNumber < 4){
			for (int i = 0; i < (4 - rowNumber) * 4; i++)
			{
				input >> skip;
			}
		}

		/////////////////////////////////////////////
		input >> rowNumber;

		if (rowNumber > 1){
			for (int i = 0; i < (rowNumber - 1) * 4; i++)
			{
				input >> skip;
			}
		}

		for (int i = 0; i < 4; i++)
		{
			input >> numbersInRows[1][i];
		}

		if (rowNumber < 4){
			for (int i = 0; i < (4 - rowNumber) * 4; i++)
			{
				input >> skip;
			}
		}

		for (int i = 0; i < 4; ++i){
			int elem = numbersInRows[0][i];
			for (int j = 0; j < 4; ++j){
				if (elem == numbersInRows[1][j]){
					numberOfMatches++;
					matchedNumber = elem;
				}
			}
		}

		output << "Case #" << testCase << ": ";
		switch (numberOfMatches)
		{
		case 0:
			output << "Volunteer cheated!";
			break;
		case 1:
			output << matchedNumber;
			break;
		default:
			output << "Bad magician!";
			break;
		}

		output << endl;
	}

	return 0;
}