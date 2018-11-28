#include <iostream>
#include <fstream>

using namespace std;

enum State
{
	NOT_COMPLETED, DRAW, X_STATE, O_STATE
};

enum Player
{
	X, O, T
};

int main()
{
	ifstream in("1.in");
	ofstream out("1.out");
	int n;
	char board[4][4];
	in >> n;
	State current;
	for(int count = 0; count < n; count++)
	{
		current = DRAW;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				in >> board[i][j];
				if(board[i][j] == '.')
					current = NOT_COMPLETED;
			}
		}
		
		//check rows
		for(int i = 0; i < 4; i++)
		{
			Player c = T;
			bool t_hit = false;
			for(int j = 0; j < 4; j++)
			{
				if(board[i][j] == 'T')
				{
					if(t_hit)
						break;
					t_hit = true;
				}
				else if(board[i][j] == 'X')
				{
					if(c == O)
					{
						c = T;
						break;
					}
					c = X;
				}
				else if(board[i][j] == 'O')
				{
					if(c == X)
					{
						c = T;
						break;
					}
					c = O;
				}
				else if(board[i][j] == '.')
				{
					c = T;
					break;
				}
			}
			if(c == O)
			{
				current = O_STATE;
				goto end;
			}
			else if(c == X)
			{
				current = X_STATE;
				goto end;
			}
		}

		//check columns
		for(int j = 0; j < 4; j++)
		{
			Player c = T;
			bool t_hit = false;
			for(int i = 0; i < 4; i++)
			{
				if(board[i][j] == 'T')
				{
					if(t_hit)
						break;
					t_hit = true;
				}
				else if(board[i][j] == 'X')
				{
					if(c == O)
					{
						c = T;
						break;
					}
					c = X;
				}
				else if(board[i][j] == 'O')
				{
					if(c == X)
					{
						c = T;
						break;
					}
					c = O;
				}
				else if(board[i][j] == '.')
				{
					c = T;
					break;
				}
			}
			if(c == O)
			{
				current = O_STATE;
				goto end;
			}
			else if(c == X)
			{
				current = X_STATE;
				goto end;
			}
		}

		for(int i = 0; i < 1; i++)
		{
			Player c = T;
			bool t_hit = false;
			for(int j = 0; j < 4; j++)
			{
				if(board[j][j] == 'T')
				{
					if(t_hit)
						break;
					t_hit = true;
				}
				else if(board[j][j] == 'X')
				{
					if(c == O)
					{
						c = T;
						break;
					}
					c = X;
				}
				else if(board[j][j] == 'O')
				{
					if(c == X)
					{
						c = T;
						break;
					}
					c = O;
				}
				else if(board[j][j] == '.')
				{
					c = T;
					break;
				}
			}
			if(c == O)
			{
				current = O_STATE;
				goto end;
			}
			else if(c == X)
			{
				current = X_STATE;
				goto end;
			}
		}

		//check right diagonal
		for(int i = 0; i < 1; i++)
		{
			Player c = T;
			bool t_hit = false;
			for(int j = 0; j < 4; j++)
			{
				if(board[j][3 - j] == 'T')
				{
					if(t_hit)
						break;
					t_hit = true;
				}
				else if(board[j][3 - j] == 'X')
				{
					if(c == O)
					{
						c = T;
						break;
					}
					c = X;
				}
				else if(board[j][3 - j] == 'O')
				{
					if(c == X)
					{
						c = T;
						break;
					}
					c = O;
				}
				else if(board[j][3 - j] == '.')
				{
					c = T;
					break;
				}
			}
			if(c == O)
			{
				current = O_STATE;
				goto end;
			}
			else if(c == X)
			{
				current = X_STATE;
				goto end;
			}
		}
	//end
end:
		out << "Case #" << count + 1 << ": ";
		if(current == X_STATE)
			out << "X won";
		else if(current == O_STATE)
			out << "O won";
		else if(current == NOT_COMPLETED)
			out << "Game has not completed";
		else if(current == DRAW)
			out << "Draw";
		out << endl;
	}
}