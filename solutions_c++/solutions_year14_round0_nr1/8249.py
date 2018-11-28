#include <iostream>
#include <string>
#include <ctime>

using namespace std;

int main()
{
	int firstCards[4][4], secondCards[4][4];
	int firstRow[4], secondRow[4];
	int firstChoice, secondChoice,n;
	int x;
	bool arrEqual = true;

	cout << "Enter number of tests: " << endl;

	cin >> n;
	int counter = 0;
	string * prints = new string[n];
	for (int index = 0; index < n; index++)
	{
		arrEqual = true;
		x = 0;
		counter = 0;

		cin >> firstChoice;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> firstCards[i][j];
			}
		}


		for (int i = 0; i < 4; i++)
		{
			firstRow[i] = firstCards[firstChoice - 1][i];
		}

		cin >> secondChoice;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> secondCards[i][j];
			}
		}

		for (int i = 0; i < 4; i++)
		{
			secondRow[i] = secondCards[secondChoice-1][i];
		}

		for (int i = 0; i < 4; i++)// rows are equal or not.
		{
			if (firstRow[i] != secondRow[i])
				arrEqual = false;
		}

		if (!arrEqual)
		{

			for (int i = 0; i < 4; i++)
			{
				for (int j = 0; j < 4; j++)
				{
					if (firstRow[i] == secondRow[j])
					{
						counter++;
						if (counter == 1)
							x = i;
					}
				}
			}
		}
		else{
			prints[index] = "Bad magician!";
		}

		if (counter > 1)
			prints[index] = "Bad magician!";
		else if(counter==1) 
			prints[index] = to_string(firstRow[x]);
		else if (counter == 0)
			prints[index] = "Volunteer cheated!";
		else if (counter==0 && !arrEqual && secondChoice == firstChoice)
			prints[index] = "Volunteer cheated!";
	}

	for (int i = 0; i<n; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		cout << prints[i] << endl;
	}

	cin.ignore(2);
	return 0;
}
