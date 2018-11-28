#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <vector>

using namespace std;

int main()
{
	int temp, cases, row, arr[17];
	cin >> cases;
	
	for (int C = 1; C <= cases; C++)
	{
		for(int i =0; i < 17; i++)
			arr[i] = 0;
			
		for (int R=0; R < 2; R++)
		{
			cin >> row; 
				for(int i = 0; i < 4; i++)
					for(int j = 0; j < 4; j++)
					{
						cin >> temp;
						if (i == row-1)
							arr[temp]++;
					}
		}

		int multipleCards = 0, whichCard = 0;
		for(int i =1; i < 17; i++)
		{
			if (arr[i] > 1)
			{
				multipleCards++;
				whichCard = i;
			}
		}
		
		cout << "Case #"<< C << ": ";
		if (multipleCards == 0)
			cout << "Volunteer cheated!" << endl;
		else if (multipleCards == 1)
			cout << whichCard << endl;
		else
			cout << "Bad magician!" << endl;
	}
}
