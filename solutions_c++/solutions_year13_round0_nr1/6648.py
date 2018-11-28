#include<iostream>
#include<fstream>
using namespace std;
const int SIZE=4;
void setWinnerState(char **board);
char columnCheck(char **board);
char rowCheck(char **board);
char diagCheck(char ** board);
bool checkWinner(char ** board);
bool isDraw(char ** board);

char state;
const char STATE_X='X';
const char STATE_O='O';
const char STATE_DRAW='D';
const char STATE_NOT_COMPLETED='N';

int main()
{
	int i=0,t;
	ofstream f;
	f.open("out.txt");
	char **board,*out;
	board=new char*[SIZE];
	for(int j=0;j<SIZE;j++)
	{
		board[j]=new char[SIZE];
	}

	cin>>t;
	out=new char[t];

	while(i<t)
	{
		for(int j=0;j<SIZE;j++)
		{
			for(int k=0;k<SIZE;k++)
			{
				cin>>board[j][k];
			}
		}
		setWinnerState(board);
		out[i]=state;
		i++;
	}

	for(i=0;i<t;i++)
	{
		switch(out[i])
		{
			case STATE_DRAW:
			f<<"Case #"<<i+1<<": Draw"<<"\n";
			break;

			case STATE_X:
			f<<"Case #"<<i+1<<": X won"<<"\n";
			break;

			case STATE_O:
			f<<"Case #"<<i+1<<": O won"<<"\n";
			break;

			default:
			f<<"Case #"<<i+1<<": Game has not completed"<<"\n";
		}
	}
	f.close();

	delete [] board;
	delete [] out;
	return 0;
}

void setWinnerState(char **board)
{
	if(!checkWinner(board))
	{
		//cout<<"Check : "<<checkWinner(board);
		for(int j=0;j<SIZE;j++)
		{
			for(int k=0;k<SIZE;k++)
			{
				if(board[j][k]=='T')
				{
						board[j][k]='X';
						if(!checkWinner(board))
						{
							board[j][k]='O';
							if(checkWinner(board))
							{
								state=STATE_O;							
							}
						}
						else
						{
							state=STATE_X;
						}
						break;
				}
			}
		}

		if(state=='f')
		{
			if(isDraw(board))
			{
				state=STATE_DRAW;
			}
			else
			{
				state=STATE_NOT_COMPLETED;
			}
		}

	}
}

bool checkWinner(char ** board)
{
	state='f';
	char winner=rowCheck(board);
	if(winner!='f')
	{
		state=winner;
	}
	else
	{
		winner=columnCheck(board);
		if(winner!='f')
		{
			state=winner;
		}
		else
		{
			winner=diagCheck(board);
			if(winner!='f')
			{
				state=winner;
			}
		}
	}
	if(state!='f')
		return true;
	else
		return false;
}


char columnCheck(char **board)
{
	int j=0;
	for(int k=0;k<SIZE;k++)
		{
			for(j=0;j<SIZE-1;j++)
			{
				if(board[j][k]=='.' || board[j][k]!=board[j+1][k])
					break;
			}
			if(j==SIZE-1)
			{
				return board[j-1][k];
			}
		}
	return 'f';
}


char rowCheck(char **board)
{
	int k=0;
	for(int j=0;j<SIZE;j++)
		{
			for(k=0;k<SIZE-1;k++)
			{
				if(board[j][k]=='.' || board[j][k]!=board[j][k+1])
					break;
			}
			if(k==SIZE-1)
			{
				return board[j][k-1];
			}
		}
	return 'f';
}


char diagCheck(char ** board)
{
	if(board[0][0]!='.' && board[0][0]==board[1][1] && board[1][1]==board[2][2] && board[2][2]==board[3][3])
	{
		return board[0][0];
	}
	else if(board[0][3]!='.' && board[0][3]==board[1][2] && board[1][2]==board[2][1] && board[2][1]==board[3][0])
	{
		return board[0][3];
	}
	else
		return 'f';
}


bool isDraw(char ** board)
{
	for(int j=0;j<SIZE;j++)
		{
			for(int k=0;k<SIZE;k++)
			{
				if(board[j][k]=='.')
					return false;
			}
		}
		return true;
}
