#include <iostream>

using namespace std;

int main()
{
	unsigned int cases;
	cin >> cases;
	for(int i = 0 ; i < cases ; i++)
	{
		unsigned int row, value[4], temp, valueNew[4], newRow, count = 0;
		cin >> row;
		for(int j = 0 ; j < 4 ; j++)
			for(int k = 0 ; k < 4 ; k++)
				if(j == row - 1)
					cin >> value[k];
				else
					cin >> temp;
			
		
		cin >> newRow;
		for(int j = 0 ; j < 4 ; j++)
			for(int k = 0 ; k < 4 ; k++)
				if(j == newRow - 1)
					cin >> valueNew[k];
				else
					cin >> temp;
		
		int val;
		for(int j = 0 ; j < 4 ; j++)
			for(int k = 0 ; k < 4 ; k++)
			{
				if(value[j] == valueNew[k])
				{
					val = value[j];
					count++;
				}
			}

		if(count == 0)
			cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		else if(count == 1)
			cout << "Case #" << i+1 << ": " << val << endl;
		else
			cout << "Case #" << i+1 << ": Bad magician!" << endl;
	}
}