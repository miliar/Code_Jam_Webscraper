#include<iostream>
#include<string>
using namespace std;

string tictactoe(char board[4][4])
{
	for (int i = 0; i < 4; i++)
		if ((board[i][0] == 'O' || board[i][0] == 'T') && (board[i][1] == 'O' || board[i][1] == 'T') && (board[i][2] == 'O' ||  board[i][2] == 'T') && (board[i][3] == 'O' ||  board[i][3] == 'T'))
		   return "O won";
  		else if ((board[0][i] == 'O' || board[0][i] == 'T') && (board[1][i] == 'O' || board[1][i] == 'T') && (board[2][i] == 'O' ||  board[2][i] == 'T') && (board[3][i] == 'O' ||  board[3][i] == 'T'))   
		   	 return "O won";
		else if ((board[0][0] == 'O' || board[0][0] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') && (board[2][2] == 'O' ||  board[2][2] == 'T') && (board[3][3] == 'O' ||  board[3][3] == 'T'))  
	       	 return "O won";
  		else if ((board[0][3] == 'O' || board[0][3] == 'T')&&  (board[1][2] == 'O' || board[1][2] == 'T') && (board[2][1] == 'O' ||  board[2][1] == 'T') && (board[3][0] == 'O' ||  board[3][0] == 'T'))   
 		   	 return "O won";
		else if ((board[i][0] == 'X' || board[i][0] == 'T') && (board[i][1] == 'X' || board[i][1] == 'T') && (board[i][2] == 'X' ||  board[i][2] == 'T') && (board[i][3] == 'X' ||  board[i][3] == 'T'))
		   return "X won";
  		else if ((board[0][i] == 'X' || board[0][i] == 'T') && (board[1][i] == 'X' || board[1][i] == 'T') && (board[2][i] == 'X' ||  board[2][i] == 'T') && (board[3][i] == 'X' ||  board[3][i] == 'T'))  
		   	 return "X won";
		else if ((board[0][0] == 'X' || board[0][0] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') && (board[2][2] == 'X' ||  board[2][2] == 'T') && (board[3][3] == 'X' ||  board[3][3] == 'T'))   
	       	 return "X won";
  		else if ((board[0][3] == 'X' || board[0][3] == 'T') && (board[1][2] == 'X' || board[1][2] == 'T') && (board[2][1] == 'X' ||  board[2][1] == 'T') && (board[3][0] == 'X' ||  board[3][0] == 'T'))  
 		   	 return "X won";   	 
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (board[i][j] == '.')
			   return "Game has not completed";
		}
	}
	return "Draw";
}

int main()
{
	int T;
	cin >> T;
	char board[4][4];
	for (int a = 1; a < T+1; a++)
	{
		for (int b = 0; b < 4; b++)
		{
			for (int c = 0; c < 4; c++)	
			{
				cin >> board[b][c];
			}
		}
		cout << "Case #" << a << ": " << tictactoe(board) << endl;
	}
	return 0;
}
