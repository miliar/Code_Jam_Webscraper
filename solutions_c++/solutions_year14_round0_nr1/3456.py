#include <iostream>

using namespace std;

int main()
{
	int cases = 0;
	int count = 1;
	cin >> cases;
	while(count <= cases)
	{
		int fRow, sRow;
		int first[4][4] = {{0}};
		int second[4][4] = {{0}};
		cin >> fRow;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> first[i][j];
			}
		}	
		cin >> sRow;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> second[i][j];
			}
		}	
		int possibilites = 0;
		int result = 0;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(first[fRow - 1][i] == second[sRow - 1][j])
				{
					possibilites++;
					result = first[fRow - 1][i];
				}
			}
		}
		cout << "Case #" << count << ": ";
		if(possibilites > 1)
		{
			cout << "Bad magician!" << endl;
		}
		else if(possibilites == 1)
		{
			cout << result << endl;
		}
		else
		{
			cout << "Volunteer cheated!" << endl;
		}
		count++;
	}
	return 0;

}
