#include <fstream>
#include <iostream>

using namespace std;

#define DEBUG 1

int main()
{
	ofstream output;
	ifstream input ("A-small-attempt0.in");
	output.open("A-small-attempt0.out");

	int t;

	input >> t;

	for (int i=0; i<t; i++)
	{
		int card[2][4];	
		int guess[2];

		output << "Case #"<<i+1<<": ";

		for (int r = 0; r < 2;  r++)
		{
			input >> guess[r];
			for(int k=0; k < 4; k++)
			{
				if (k != guess[r] - 1)
				{
					int temp;
					for (int ii=0; ii < 4; ii++)
						input >>  temp;
				}
				else
				{
					for (int ii=0; ii < 4; ii++)
					{
						input >> card[r][ii];
					}
				}
			}
		}

#if DEBUG 
		for (int j = 0; j < 2; j++)
		{
			for (int jj = 0; jj < 4; jj++)
				cout << card[j][jj] << " ";
			cout << endl;
		}
#endif

		int same_number = 0;
		int card_number = 0;
		for (int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				if (card[0][j] == card[1][k])
				{
					card_number = card[0][j];
					same_number ++;
				}
				
			}
		}

		if (same_number == 0)
			output<<"Volunteer cheated!"<<endl;
		else if (same_number > 1)
			output<<"Bad magician!"<<endl;
		else
			output<<card_number<<endl;
	}
}
