/*
* Google Code Jam 2014
* Qualification Round
* Adrian Dale
* A - Magic Trick
*/
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int T; // No of test cases

void SolveTestCase(string FR, string SR)
{
	vector<int> firstRow;

	istringstream row1parser(FR);
	for (int i = 0; i < 4; ++i)
	{
		int digit;
		row1parser >> digit;
		firstRow.push_back(digit);
	}

	istringstream row2parser(SR);
	int digitFound = -1;
	bool duplicateFound = false;
	for (int i = 0; i < 4; ++i)
	{
		int digit;
		row2parser >> digit;
		if (find(firstRow.begin(), firstRow.end(), digit) != firstRow.end())
		{
			if (digitFound != -1)
				duplicateFound = true;
			digitFound = digit;
		}
	}

	if (digitFound == -1)
		cout << "Volunteer cheated!";
	else if (duplicateFound == true)	
		cout << "Bad magician!";
	else
		cout << digitFound;

}

void ReadTestCases()
{
	string line;

	getline(cin, line);
	istringstream parser(line);
	parser >> T;

	int TestNo = 1;
	while (TestNo <= T)
	{
		getline(cin, line);
		parser.str(line);
		parser.clear();
		int FirstRowGuess;
		parser >> FirstRowGuess;
		string FirstInterestedRow;
		// Read the rows
		for (int r = 1; r <= 4 ; ++r)
		{
			getline(cin, line);
			if (r == FirstRowGuess)
				FirstInterestedRow = line;
		}
		
		getline(cin, line);
		parser.str(line);
		parser.clear();
		int SecondRowGuess;
		parser >> SecondRowGuess;
		string SecondInterestedRow;
		// Read the rows
		for (int r = 1; r <= 4; ++r)
		{
			getline(cin, line);
			if (r == SecondRowGuess)
				SecondInterestedRow = line;
		}

		cout << "Case #" << TestNo << ": ";
		SolveTestCase(FirstInterestedRow, SecondInterestedRow);
		cout << endl;

		++TestNo;
	}
}

int main()
{
	ReadTestCases();
	return 0;
}
