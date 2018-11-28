#include <iostream>

using namespace std;

int main()
{
	int count;
	cin >> count;

	for(int i = 0; i < count; i++)
	{
		int row1,row2;
		int arrangement1[4][4];
		int arrangement2[4][4];
		
		cin >> row1;
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				cin >> arrangement1[j][k];
			}
		}

		cin >> row2;
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				cin >> arrangement2[j][k];
			}
		}

		int guess = 0;
		int card = 0;
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				if(arrangement1[row1 - 1][j] == arrangement2[row2 - 1][k])
				{
					card = arrangement1[row1 - 1][j];
					guess++;
				}
			}
		}
		
		cout << "Case #" << (i + 1) << ": ";
		if(guess == 0)
		{
			cout << "Volunteer cheated!";
		}
		else if(guess == 1)
		{
			cout << card;
		}
		else
		{
			cout << "Bad magician!";
		} 
		cout << endl;
	}

	return 0;
}
