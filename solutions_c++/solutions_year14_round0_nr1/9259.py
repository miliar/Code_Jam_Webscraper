#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int c = 0; c < numCases; ++c) 
	{
		int row1;
		cin >> row1;

		vector<int> cards(4);
		for (int j = 0; j < 4; ++j)
		{
			for (int i = 0; i < 4; ++i)
			{
				int m;
				cin >> m;
				if (j + 1 == row1)
					cards[i] = m;
			}
		}

		int row2;
		cin >> row2;

		int guess = -1;
		int numCards = 0;

		for (int j = 0; j < 4; ++j)
		{
			for (int i = 0; i < 4; ++i)
			{
				int m;
				cin >> m;
				if (j + 1 == row2)
				{
					if (std::find(cards.begin(), cards.end(), m) != cards.end()) {
						guess = m;
						++numCards;
					}
				}
			}
		}
				
		cout << "Case #" << c + 1 << ": ";

		if (numCards == 1)
			cout << guess << endl;
		else if (numCards > 1)
			cout << "Bad magician!" << endl;
		else
			cout << "Volunteer cheated!" << endl;
	}
		
	return 0;
}
