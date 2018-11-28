#include <iostream>

using namespace std;

int main()
{
	int T, i = 0, answer1, answer2, chosenCard, 
	    cards1[16], cards2[16], icards, ichosen, 
	    chosenRow[4], chosenColumn[4];
	int correctCards, lele;

	cin >> T;
	while(i++ < T)
	{
		cin >> answer1;
		for(icards = 0; icards < 16; icards++)
			cin >> cards1[icards];

		cin >> answer2;
		for(icards = 0; icards < 16; icards++)
			cin >> cards2[icards];

		// get the chosen rows
		for(icards = ichosen = 0; icards < 4; icards++, ichosen++)
		{
			chosenRow[ichosen] = cards1[((answer1 - 1) * 4) + icards];
			chosenColumn[ichosen] = cards2[((answer2 - 1) * 4) + icards];
		}

		correctCards = 0;
		for(int l = 0; l < 4; ++l)
		{
			for(int j = 0; j < 4; ++j)
			{
				if(chosenRow[l] == chosenColumn[j])
				{
					correctCards++;
					chosenCard = chosenRow[l];
				}
			}
		}

		cout << "Case #" << i << ": " ;
		if(correctCards == 1)
			cout << chosenCard << endl;
		else if(correctCards == 0)
			cout << "Volunteer cheated!" << endl;
		else
			cout << "Bad magician!" << endl;
	}

	return 0;
}