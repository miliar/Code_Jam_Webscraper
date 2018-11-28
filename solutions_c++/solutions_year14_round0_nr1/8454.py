#include <iostream>
using namespace std;

void solveA(int t)
{
	int table1[16];
	int table2[16];
	int row1Index, row2Index;

	cin >> row1Index;
	for (int i = 0; i < 16; i++)
	{
		cin >> table1[i];
	}

	cin >> row2Index;
	for (int i = 0; i < 16; i++)
	{
		cin >> table2[i];
	}

	int matchedCount = 0;
	int rez;

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (table1[(row1Index-1)*4 + i] == table2[(row2Index-1)*4 + j])
			{
				rez = table1[(row1Index-1)*4 + i];
				matchedCount++;
			}
		}
	}

	cout << "Case #" << t << ": ";
	if (matchedCount == 0)
		cout << "Volunteer cheated!";
	else if (matchedCount > 1)
		cout << "Bad magician!";
	else
		cout << rez;
	cout << endl;
}

void a()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		solveA(i+1);
	}
}

int main()
{
	a();
	return 0;
}