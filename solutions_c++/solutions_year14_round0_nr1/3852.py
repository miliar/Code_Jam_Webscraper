// Magician.cpp : Defines the entry point for the console application.
//

#include <iostream>

using namespace std;

#define	MaxCards	4


int main()
{
	int T, testCounter = 1;
	cin>>T;
	while (T--)
	{
		int CardSquare1[MaxCards][MaxCards];
		int CardSquare2[MaxCards][MaxCards];
		int ans1, ans2;

		//Read input
		cin>>ans1;
		ans1--;
		for (int i=0; i<MaxCards; i++)
		{
			for (int j=0; j<MaxCards; j++)
			{
				cin>>CardSquare1[i][j];
			}
		}

		cin>>ans2;
		ans2--;
		for (int i=0; i<MaxCards; i++)
		{
			for (int j=0; j<MaxCards; j++)
			{
				cin>>CardSquare2[i][j];
			}
		}

		int guess, matchCount = 0;

		for (int i=0; i<MaxCards; i++)
		{
			for (int j=0; j<MaxCards; j++)
			{
				if (CardSquare1[ans1][i] == CardSquare2[ans2][j])
				{
					matchCount++;
					guess = CardSquare1[ans1][i];
				}
			}
		}

		if (matchCount == 1)
		{
			cout<<"Case #"<<testCounter<<": "<<guess<<"\n";
		}
		else if (matchCount == 0)
		{
			cout<<"Case #"<<testCounter<<": "<<"Volunteer cheated!\n";			
		}
		else
		{
			cout<<"Case #"<<testCounter<<": "<<"Bad magician!\n";
		}		
		testCounter++;
	}
	return 0;
}