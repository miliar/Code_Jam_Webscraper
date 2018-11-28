#include <iostream>
using namespace std;

int main()
{
	int t;
	int first;
	int first_cards[5][5];
	int second;
	int second_cards[5][5];
	int count;
	int card;

	cin >> t;
	for (int ii = 0; ii < t; ++ii)	
	{
		cin >> first;	
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> first_cards[i][j];
		
		cin >> second;	
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> second_cards[i][j];
		
		count=0;	
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
					if (first_cards[first-1][i] == second_cards[second-1][j])
					{
							card = first_cards[first-1][i];
							++count;
					}
			}

		cout << "Case #" << ii + 1 << ": " ;
		if (count == 1)
				cout << card;
		else if (count > 1)
				cout << "Bad magician!";
		else
				cout << "Volunteer cheated!";
		cout << endl;
	}
	return 0;
}
