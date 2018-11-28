#include <iostream>
using namespace std;

void solveIt(int testId, int answer1, int answer2, int table1[5][5], int table2[5][5]);

int main(int argc, char *argv[])
{
	int T;

	cin >> T;

	for (int ti = 1; ti <= T; ++ti)
	{
		int answer1, answer2;
		int table1[5][5], table2[5][5];

		cin >> answer1;

		for(int r = 1; r <= 4; ++r)
		{
			for(int c = 1; c <= 4; c++)
			{
				cin >> table1[r][c];
			}
		}

		cin >> answer2;

		for(int r = 1; r <= 4; ++r)
		{
			for(int c = 1; c <= 4; c++)
			{
				cin >> table2[r][c];
			}
		}

		solveIt(ti, answer1, answer2, table1, table2);
	}

	return 0;
}

void solveIt(int testId, int answer1, int answer2, int table1[5][5], int table2[5][5])
{
	bool exists[17] = {false};
	int found = 0;

	for (int i = 1; i <= 4; ++i)
	{
		exists[ table1[answer1][i] ] = true;
	}

	for (int i = 1; i <= 4; ++i)
	{
		int item = table2[answer2][i];

		if(exists[item])
		{
			if(found) // second number
			{
				cout << "Case #" << testId << ": Bad magician!" << endl;
				return;
			}
			else
			{
				found = item;
			}
		}
	}

	if(found)
	{
		cout << "Case #" << testId << ": " << found << endl;
	}
	else
	{
		cout << "Case #" << testId << ": Volunteer cheated!" << endl;	
	}
}