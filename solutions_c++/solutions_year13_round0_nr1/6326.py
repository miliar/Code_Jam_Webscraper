#include <vector>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

bool myBool(char x, char y, char z, char t)
{
	string str="";

	if (x=='.' || y=='.' || z=='.' || t=='.')
	{
		return false;
	}
	else
	{
		str+=x;
		str+=y;
		str+=z;
		str+=t;

		if (str=="XXXX" || str=="XXXT" || str=="XXTX" || str=="XTXX" || str=="TXXX" ||
			str=="OOOO" || str=="OOOT" || str=="OOTO" || str=="OTOO" || str=="TOOO" )
		{
			return true;
		}
		else
		{
			return false;
		}
	}

}
int main()
{
	char tmp;
	ifstream inputFile;
	unsigned int numberOfInputs;
	unsigned int inputNumber=0;
	inputFile.open("A-large.in");

	if ( inputFile.good() )
	{
		inputFile >> numberOfInputs;
		while (inputNumber<numberOfInputs)
		{
			unsigned int i;
			bool isFinished = true;
			bool oWon = false;
			bool xWon = false;
			char game [4][4];

			for (i=0; i<16 && inputFile>>tmp; i++)
			{
				game[(int) i/4][i%4] = tmp;
			}

			for( int i=0; i<4; i++)
			{
				for( int j=0; j<4; j++)
				{
					if (game[i][j] == '.')
					{
						isFinished = false;
					}
				}
			}

			for (int i=0; i<4; i++)
			{
				if ( myBool(game[i][0], game[i][1], game[i][2], game[i][3]) )
				{
					if (game[i][0] != 'T')
					{
						if (game[i][0] == 'O')
						{
							oWon = true;
						}
						else if( game[i][0] == 'X')
						{
							xWon = true;
						}
					}
					else if (game[i][1] != 'T')
					{
						if (game[i][1] == 'O')
						{
							oWon = true;
						}
						else if( game[i][1] == 'X')
						{
							xWon = true;
						}
					}
				}
			}

			for (int j=0; j<4; j++)
			{
				if ( myBool(game[0][j], game[1][j], game[2][j], game[3][j]) )
				{
					if (game[0][j] != 'T')
					{
						if (game[0][j] == 'O')
						{
							oWon = true;
						}
						else if( game[0][j] == 'X')
						{
							xWon = true;
						}
					}
					else if (game[1][j] != 'T')
					{
						if (game[1][j] == 'O')
						{
							oWon = true;
						}
						else if( game[1][j] == 'X')
						{
							xWon = true;
						}
					}
				}
			}

			if ( myBool(game[0][0], game[1][1], game[2][2], game[3][3]) )
			{
				if (game[0][0] != 'T')
				{
					if (game[0][0] == 'O')
					{
						oWon = true;
					}
					else if( game[0][0] == 'X')
					{
						xWon = true;
					}
				}
				else if (game[1][1] != 'T')
				{
					if (game[1][1] == 'O')
					{
						oWon = true;
					}
					else if( game[1][1] == 'X')
					{
						xWon = true;
					}
				}
			}

			if ( myBool(game[0][3], game[1][2], game[2][1], game[3][0]) )
			{
				if (game[3][0] != 'T')
				{
					if (game[3][0] == 'O')
					{
						oWon = true;
					}
					else if( game[3][0] == 'X')
					{
						xWon = true;
					}
				}
				else if (game[1][2] != 'T')
				{
					if (game[1][2] == 'O')
					{
						oWon = true;
					}
					else if( game[1][2] == 'X')
					{
						xWon = true;
					}
				}
			}

			if (oWon)
			{
				cout << "Case #" << ++inputNumber << ": O won" << endl;
			}
			else if(xWon)
			{
				cout << "Case #" << ++inputNumber << ": X won" << endl;
			}
			else if(isFinished)
			{
				cout << "Case #" << ++inputNumber << ": Draw" << endl;
			}
			else
			{
				cout << "Case #" << ++inputNumber << ": Game has not completed" << endl;
			}
		}
	}

	return 0;
}
