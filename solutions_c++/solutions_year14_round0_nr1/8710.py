#include <iostream>
#include <vector>

using namespace std;

int NUMCARDS = 16;
int LENGTH = 4;
vector< vector<int> > board;

void setVector()
{
	board.resize(LENGTH);
	for (int i = 0; i < LENGTH; ++i)
	{
		board[i].resize(LENGTH);
	}
}

void setCards()
{
	int card;
	for (int i = 0; i < LENGTH; ++i)
	{
		for (int j = 0; j < LENGTH; ++j)
		{
			cin >> card;
			board[i][j] = card;
		}
	}
}

void printBoard()
{
	for (int i = 0; i < LENGTH; ++i)
	{
		for (int j = 0; j < LENGTH; ++j)
		{
			cout << board[i][j];
		}
	}
}

int main()
{
	setVector();
	int numTrials;
	cin >> numTrials;
	char c;
	for(int i = 1; i <= numTrials; ++i)
	{
		c = 'a';
		int ans1, ans2;
		cin >> ans1;
		setCards();
		vector<int> row1 = board[ans1 - 1];
		cin >> ans2;
		setCards();
		vector<int> row2 = board[ans2 - 1];

		int output = 0;
		for (int j = 0; j < LENGTH; ++j)
		{
			for (int k = 0; k < LENGTH; ++k)
			{
				if(row1[j] == row2[k])
				{
					if(output > 0 && c != 'b')
					{
						cout << "Case #" << i << ": Bad Magician!\n";
						c = 'b';
					}
					output = row1[j];
				}
			}
		}
		if(c != 'b')
		{
			if(output > 0)
				cout << "Case #" << i << ": " << output << endl;
			else
			{
				cout << "Case #" << i << ": Volunteer cheated!\n";
			}
		}
	}
}