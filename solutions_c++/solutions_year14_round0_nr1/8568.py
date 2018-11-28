/* Magic trick */
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	int T, i, j, k, row, card, cont, selected;
	bool cards[17];
	cin >> T;
	for(i = 1; i <= T; i++)
	{
		memset(cards, false, sizeof cards);
		cont = 0;
		// First question
		cin >> row;
		for(j = 1; j <= 4; j++)
		{
			for(k = 1; k <= 4; k++)
			{
				cin >> card;
				// Marks cards in selected row
				if(j == row)
				{
					cards[card] = true;
				}
			}
		}
		// Second question
		cin >> row;
		for(j = 1; j <= 4; j++)
		{
			for(k = 1; k <= 4; k++)
			{
				cin >> card;
				// Check cards in selected row
				if(j == row)
				{
					if(cards[card])
					{
						selected = card;
						cont++;
					}
				}
			}
		}
		// Answer
		cout << "Case #" << i << ": ";
		if(cont == 0)
			cout << "Volunteer cheated!" << endl;
		else if(cont > 1)
			cout << "Bad magician!" << endl;
		else
			cout << selected << endl;
	}
	return 0;
}
