#include <iostream>
using namespace std;

void readCards(int cards[4][4], int r, int c)
{
	for( int i = 0; i < r; ++i )
	{
		for( int j = 0; j < c; ++j )
		{
			cin >> cards[i][j];
		}
	}
}

int getSelectedCard( int* cards1, int* cards2, int size )
{
	int selectedCard = 0;
	for( int i = 0; i < size; ++i )
	{
		for( int j = 0; j < size; ++j )
		{
			if( cards1[i] == cards2[j] )
			{
				if( selectedCard != 0)
				{
					return -1;
				}
				selectedCard = cards1[i];
			}
		}
	}
	return selectedCard;
}

int main()
{
		int numTC = 0, currentTC = 0;
		int ans1 = 0, ans2 = 0;
		int selectedCard = 0;

		int cards1[4][4] = { 0 };
		int cards2[4][4] = { 0 };

		cin >> numTC;	

		while( ++currentTC <= numTC )
		{
			cin >> ans1;
			readCards( cards1, 4, 4 );

			cin >> ans2;
			readCards( cards2, 4, 4 );

			int uniqueElem = getSelectedCard( cards1[ans1-1], cards2[ans2-1], 4 );
			if( uniqueElem == 0 )
			{
				cout << "Case #" << currentTC <<": " << "Volunteer cheated!\n";
			}
			else if( uniqueElem < 0 )
			{
				cout << "Case #" << currentTC <<": " << "Bad magician!\n";
			}
			else
			{
				cout << "Case #" << currentTC <<": " << uniqueElem <<"\n";
			}
		}

		return 0;
}
