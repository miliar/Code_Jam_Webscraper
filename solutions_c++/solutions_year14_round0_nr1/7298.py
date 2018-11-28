#include <iostream>

using namespace std;

int main()
{
	int testcases;
	cin >> testcases;

	for(int i = 0; i < testcases; i++)
	{
		int row1, row2, temp;
		cin >> row1;

		int array1[4] = {};
		int array2[4] = {};

		for(int j = 0; j < 16; j++)
		{
			cin >> temp;
			
			if(j >= (row1 - 1)*4 && j < (row1)*4) array1[j - ((row1 - 1)*4)] = temp;
		}

		cin >> row2;
		for(int j = 0; j < 16; j++)
		{
			cin >> temp;
			if(j >= (row2 - 1)*4 && j < (row2)*4) array2[j - ((row2 - 1)*4)] = temp;
		}

		int count = 0, res = 0;
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				if(array1[j] == array2[k])
				{
					count++;
					res = array1[j];
				}
			}
		}

		switch(count)
		{
			case 0:
				cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
				break;
			case 1:
				cout << "Case #" << i + 1 << ": " << res << endl;
				break;
			default:
				cout << "Case #" << i + 1 << ": Bad Magician!" << endl;
				break;
		}
	}
}