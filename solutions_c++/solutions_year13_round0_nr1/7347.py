#include <iostream>
#include <cstdio>

using namespace std;
char IsWinner(char array[]);
int main()
{
	FILE *fr,*fw;
	freopen_s(&fr,"input.in","r",stdin);
	freopen_s(&fw,"out.out","w",stdout);

	int T;
	cin >> T;
	for(int t=0; t< T;t++)
	{
		printf("Case #%d: ",t+1);
		char board[4][4];
		for(int i=0; i < 4; i++)
		{
			for(int j=0; j < 4; j++)
			{
				cin >> board[i][j];
			}
		}
		char winningPlayer = 'Z';
		bool solved = false;

		for (int i = 0; i < 4; i++)
		{
			char checkRow[4];
			for (int j = 0; j < 4; j++)
			{
				checkRow[j] = board[i][j];
			}
			char w = IsWinner(checkRow);
			if (w == 'X' || w =='O')
			{
				winningPlayer = w;
				solved = true;
				break;
			}
		}

		for( int i = 0; i < 4 && !solved; i++)
		{
			char array[4];
			for( int j= 0; j < 4; j++)
			{
				array[j] = board[j][i];
			}
			char w = IsWinner(array);
			if(w == 'X' || w =='O')
			{
				winningPlayer =  w;
				solved = true;
				break;
			}
		}

		if (!solved)
		{
			char arr1[4];
			for(int i=0; i < 4; i++)
			{
				arr1[i] = board[i][i];
			}

			char diagonal1Winner = IsWinner(arr1);
			if(diagonal1Winner == 'X' || diagonal1Winner == 'O')
			{
				winningPlayer = diagonal1Winner;
				solved = true;				
			}			
		}

		if (!solved)
		{
			char arr2[4];
			for (int i = 0; i < 4; i++)
			{
				arr2[i] = board[i][4 - i - 1];
			}
			char diagonal2Winner = IsWinner(arr2);            
			if (diagonal2Winner == 'X' || diagonal2Winner == 'O')
			{
				winningPlayer = diagonal2Winner;
				solved = true;				
			} 
		}


		bool completed = true;

		if(solved)
		{
			cout << winningPlayer << " won\n";
		}
		else
		{
			for(int i= 0; i < 4; i++)
			{
				for (int j=0; j < 4; j++)
				{
					if(board[i][j] == '.')
					{
						completed = false;
						break;
					}
				}
			}
			if(completed)
			{
				cout << "Draw\n";
			}
			else
			{
				cout << "Game has not completed\n";
			}
		}				
	}
	return 0;
}

char IsWinner(char* array) 
{
	char winner = 'Z';
	int cx, co, ct, cd;
	cx = co = ct= cd =0;
	for(int i=0; i < 4; i++)
	{		
		if(array[i]== 'X')
			cx++;
		else if(array[i] == 'O')
			co++;
		else if(array[i] == 'T')
			ct++;
		else if(array[i] =='.')
			cd++;
	}
	if( cx==4 || (cx == 3 && ct==1))
		winner='X';
	else if( co==4 || (co == 3 && ct==1))
		winner='O';


	return winner;


	return 0;
}
