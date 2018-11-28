/*
 ID: Joe Montano
 PROG: pprime
 LANG: C++
 */

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string board[4][4];
bool xWin = false, yWin = false;

void getInput()
{
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			char x;
			cin >> x;
			board[i][j] = x;
		}
	}
}

void printBoard()
{
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			cout << board[i][j];
		}
		cout << endl;
	}

	cout << endl;
}

void checkHor()
{
	
	for(int i=0; i<4; i++)
	{
		int xCount=0, yCount=0;
		int k = 0;
		string str;
		for(int j=0; j<4; j++)
		{
			str+=board[i][j];
		}
		while(k<4 && str[k] == 'X' || k<4 && str[k] == 'T')
		{
			xCount++;
			k++;
			if(xCount == 4)
			{
				xWin = true;
			}
		}
		k=0;
		while(k<4 && str[k] == 'O' || k<4 && str[k] == 'T')
		{
			yCount++;
			k++;
			if(yCount == 4)
			{
				yWin = true;
			}
		}
	}
	//cout << xCount << " " << yCount << endl;
}

void checkVert()
{
	for(int i=0; i<4; i++)
	{
		int xCount=0, yCount=0;
		int k = 0;
		string str;
		for(int j=0; j<4; j++)
		{
			str+=board[j][i];
		}
		while(k<4 && str[k] == 'X' || k<4 && str[k] == 'T')
		{
			xCount++;
			k++;
			if(xCount == 4)
			{
				xWin = true;
			}
		}
		k=0;
		while(k<4 && str[k] == 'O' || k<4 && str[k] == 'T')
		{
			yCount++;
			k++;
			if(yCount == 4)
			{
				yWin = true;
			}
		}
	}
}

void checklrDiag()
{
	for(int i=0; i<4; i++)
	{
		int xCount=0, yCount=0;
		int k = 0;
		string str;
		int spot=0;
		for(int j=0; j<4; j++)
		{
			str+=board[spot][spot];
			spot++;
		}
		while(k<4 && str[k] == 'X' || k<4 && str[k] == 'T')
		{
			xCount++;
			k++;
			if(xCount == 4)
			{
				xWin = true;
			}
		}
		k=0;
		while(k<4 && str[k] == 'O' || k<4 && str[k] == 'T')
		{
			yCount++;
			k++;
			if(yCount == 4)
			{
				yWin = true;
			}
		}
	}
}

void checkrlDiag()
{
	for(int i=0; i<4; i++)
	{
		int xCount=0, yCount=0;
		int k = 0;
		string str;
		int spot=3;
		for(int j=0; j<4; j++)
		{
			str+=board[j][spot];
			spot--;
		}
		while(k<4 && str[k] == 'X' || k<4 && str[k] == 'T')
		{
			xCount++;
			k++;
			if(xCount == 4)
			{
				xWin = true;
			}
		}
		k=0;
		while(k<4 && str[k] == 'O' || k<4 && str[k] == 'T')
		{
			yCount++;
			k++;
			if(yCount == 4)
			{
				yWin = true;
			}
		}
	}
}

bool checkCompleted()
{
	if(!xWin && !yWin)
	{
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{	
				string str = board[i][j];
				if(str == ".")
				{
					return false;
				}
			}
		}
	}

	return true;
}

int main()
{
	//freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);

	int cases;

	cin >> cases;

	int runs = 1;

	while(runs <= cases)
	{
		getInput();

		checkHor();

		checkVert();

		checklrDiag();

		checkrlDiag();

		if(!checkCompleted())
		{
			cout << "Case #" << runs << ": " << "Game has not completed" << endl;
		}

		if(xWin && yWin)
		{
			cout << "Case #" << runs << ": " << "Draw" << endl;
		}
		else if(xWin)
		{
			cout << "Case #" << runs << ": " << "X won" << endl;
		}
		else if(yWin)
		{
			cout << "Case #" << runs << ": " << "O won" << endl;
		}
		else if(!xWin && !yWin && checkCompleted())
		{
			cout << "Case #" << runs << ": " << "Draw" << endl;
		}
		//printBoard();

		runs++;
		xWin = false;
		yWin = false;
	}

	return 0;
}