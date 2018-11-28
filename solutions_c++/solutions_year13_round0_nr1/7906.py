#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;

vector< vector<char> > board(4);

bool CheckHorizontal(int a, int b)
{
	char checkChar = board[a][b];

	if(checkChar == '.')
	{
		return false;
	}
	else if(checkChar == 'T')
	{
		checkChar = board[a][b+1];
		for (int i = 1; i < board[a].size(); i++)
		{
			if(board[a][i] != checkChar)
				return false;
		}
	}
	else
	{
		for (int i = 1; i < board[a].size(); i++)
		{
			if(board[a][i] != checkChar && board[a][i] != 'T')
				return false;
		}
	}

	return true;
}

bool CheckVertical(int a, int b)
{
	char checkChar = board[a][b];

	if(checkChar == '.')
	{
		return false;
	}
	else if(checkChar == 'T')
	{
		checkChar = board[a+1][b];
		for (int i = 1; i < board.size(); i++)
		{
			if(board[i][b] != checkChar)
				return false;
		}
	}
	else
	{
		for (int i = 1; i < board.size(); i++)
		{
			if(board[i][a] != checkChar && board[i][a] != 'T')
				return false;
		}
	}

	return true;
}

bool CheckDiagonal(int a, int b)
{
	char checkChar = board[a][b];

	if(checkChar == '.')
	{
		return false;
	}
	else if(checkChar == 'T')
	{
		checkChar = board[a+1][b+1];
		for (int i = 1; i < board.size(); i++)
		{
			if(board[i][i] != checkChar)
				return false;
		}
	}
	else
	{
		for (int i = 1; i < board.size(); i++)
		{
			if(board[i][i] != checkChar && board[i][i] != 'T')
				return false;
		}
	}

	return true;
}

bool CheckSecondDiagonal(int a, int b)
{
	char checkChar = board[a][b];

	if(checkChar == '.')
	{
		return false;
	}
	else if(checkChar == 'T')
	{
		checkChar = board[a+1][b-1];
		for (int i = 1; i < board.size(); i++)
		{
			if(board[i][board.size() - i - 1] != checkChar)
				return false;
		}
	}
	else
	{
		for (int i = 1; i < board.size(); i++)
		{
			if(board[i][board.size() - i - 1] != checkChar && board[i][board.size() - i - 1] != 'T')
				return false;
		}
	}

	return true;
}

void main()
{
	for (int i = 0; i < board.size(); i++)
	{
		board[i].resize(4);
	}
	
	ifstream in("A-small-attempt1.in");
	ofstream out("A-small-out.out");

	int T;
	in>>T;
	
	for(int Case=0;Case<T;Case++)
	{
		string answer = "";
		bool found = false;
		for (int i = 0; i < board.size(); i++)
		{
			for (int j = 0; j < board[i].size(); j++)
			{
				in>>board[i][j];
			}
		}
		//check horizonts
		for (int i = 0; i < board.size(); i++)
		{
			if(CheckHorizontal(i,0))
			{
				if(board[i][0] == 'X')
				{
					answer = "X won";
					found = true;
				}
				else if(board[i][0] == 'O')
				{
					answer = "O won";
					found = true;
				}
			}
		}
		//check verticals
		if(!found)
		{
			for (int i = 0; i < board[0].size(); i++)
			{
				if(CheckVertical(0,i))
				{
					if(board[0][i] == 'X')
					{
						answer = "X won";
						found = true;
					}
					else if(board[0][i] == 'O')
					{
						answer = "O won";
						found = true;
					}
				}
			}
		}
		//check diagonal
		if(!found)
		{
			
			if(CheckDiagonal(0,0))
			{
				if(board[0][0] == 'X')
				{
					answer = "X won";
					found = true;
				}
				else if(board[0][0] == 'O')
				{
					answer = "O won";
					found = true;
				}
			}
			if(CheckSecondDiagonal(0,3))
			{
				if(board[0][3] == 'X')
				{
					answer = "X won";
					found = true;
				}
				else if(board[0][3] == 'O')
				{
					answer = "O won";
					found = true;
				}
			}
		}
		//if not found
		if(!found)
		{
			for (int i = 0; i < board.size(); i++)
			{
				for (int j = 0; j < board[i].size(); j++)
				{
					if(board[i][j] == '.')
					{
						answer = "Game has not completed";
						found = true;
						break;
					}
				}
			}
		}
		if(!found)
			answer = "Draw";
		

		out<<"Case #"<<Case+1<<": " << answer<<endl;
	}
	in.close();
	out.close();
}