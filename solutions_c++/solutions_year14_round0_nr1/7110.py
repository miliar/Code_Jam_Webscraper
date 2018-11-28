#include <iostream>

using namespace std;

void readCards(int *cards)
{
	int i;

	for(i = 0; i < 16; i++)
		cin >> cards[i];
}

int compareRows(int *cards1, int row1, int *cards2, int row2)
{
	int i, j, numMatches = 0, cardNum;

	for(i = row1*4; i < (row1+1)*4; i++)
		for(j = row2*4; j < (row2+1)*4; j++)
			if(cards1[i] == cards2[j])
			{
				cardNum = cards1[i];
				numMatches++;
			}


	if(numMatches == 0)
		return -2;  // Volunteer cheated!

	if(numMatches == 1)
		return cardNum;  

	return -1;  // Bad magician!
}

int main()
{
	int t, T;

	cin >> T;

	for(t = 0; t < T; t++)
	{
		int row1, row2, result;
		int cards1[16], cards2[16];

		cin >> row1;
		readCards(cards1);
		
		cin >> row2;
		readCards(cards2);
		
		result = compareRows(cards1, row1-1, cards2, row2-1);

		cout << "Case #" << t+1 << ": ";

		if(result > 0)
			cout << result;
		else if(result == -1)
			cout << "Bad magician!";
		else if(result == -2)
			cout << "Volunteer cheated!";
		else
			cout << "Unknown error";

		cout << endl;
	}
}
