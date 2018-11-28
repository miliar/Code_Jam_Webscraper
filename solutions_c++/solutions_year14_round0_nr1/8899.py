#include <iostream>

using namespace std;

void ComputeTest()
{
	int answer1;
	int answer2;
	int tabA[4][4];
	int tabB[4][4];
	
	cin >> answer1;
	
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			cin >> tabA[i][j];
	
	cin >> answer2;
	
	answer1--;
	answer2--;
	
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			cin >> tabB[i][j];

	int numberOfCards = 0;
	int foundNumber = -1;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (tabA[answer1][i] == tabB[answer2][j])
			{
				foundNumber = tabA[answer1][i];
				++numberOfCards;
			}
		}
	}
	
	if (numberOfCards == 0)
	{
		cout << "Volunteer cheated!";
	}
	else if (numberOfCards > 1)
	{
		cout << "Bad magician!";
	}
	else
	{
		cout << foundNumber;
	}
}

int main()
{
	int tests;
	
	cin >> tests;
	for (int i = 1; i <= tests; ++i)
	{
		cout << "Case #" << i << ": ";
		
		ComputeTest();
		
		cout << "\n";
	}
	
	return 0;
}