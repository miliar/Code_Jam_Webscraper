#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main()
{

	int T = 0; // Test cases
	string row;
	getline(cin,row);
	istringstream(row) >>T;

	for(int i=0; i<T; ++i)
	{
		char board[4][4];
		
		
		for(int r=0; r<4; ++r)
		{
			getline(cin,row);
			istringstream(row) >> board[r][0] >> board[r][1] >> board[r][2] >> board[r][3];
		}
		getline(cin,row);

		bool xWin = false;
		bool oWin = false;
		bool gameCompleted = true;

		char diagL[4] = { board[0][0], board[1][1], board[2][2], board[3][3]} ;
		char diagR[4]= { board[0][3], board[1][2], board[2][1], board[3][0]} ;

		

		for(int r=0; r<4; ++r)
		{
			int xAmount = 0;
			int oAmount = 0;
			bool tFound = false;
			for(int c=0; c<4; ++c)
			{

				if(board[r][c] == '.')
				{
					gameCompleted = false;
					break;
					
				}
				if(board[r][c] == 'X') xAmount++;
				if(board[r][c] == 'O') oAmount++;
				if(board[r][c] == 'T') tFound = true;

			}

			if( (xAmount == 4) || (tFound && xAmount == 3 ) )
			{
				xWin = true;
				break;
			}

			if( (oAmount == 4) || (tFound && oAmount == 3 ) )
			{
				oWin = true;
				break;
			}
		}


		for(int c=0; c<4; ++c)
		{
			int xAmount = 0;
			int oAmount = 0;
			bool tFound = false;
			for(int r=0; r<4; ++r)
			{

				if(board[r][c] == '.')
				{
					gameCompleted = false;
					break;
					
				}
				if(board[r][c] == 'X') xAmount++;
				if(board[r][c] == 'O') oAmount++;
				if(board[r][c] == 'T') tFound = true;

			}

			if( (xAmount == 4) || (tFound && xAmount == 3 ) )
			{
				xWin = true;
				break;
			}

			if( (oAmount == 4) || (tFound && oAmount == 3 ) )
			{
				oWin = true;
				break;
			}
		}

		int xAmount = 0;
		int oAmount = 0;
		bool tFound = false;
		for(int i=0; i<4; ++i)
		{
			
			if(diagL[i] == '.')
			{
				gameCompleted = false;
				break;
			}
			if(diagL[i] == 'X') xAmount++;
			if(diagL[i] == 'O') oAmount++;
			if(diagL[i] == 'T') tFound = true;
		}
		if( (xAmount == 4) || (tFound && xAmount == 3 ) )
		{
			xWin = true;
		}

		if( (oAmount == 4) || (tFound && oAmount == 3 ) )
		{
			oWin = true;
		}
		xAmount = 0;
		oAmount = 0;
		tFound = false;
		for(int i=0; i<4; ++i)
		{
			
			if(diagR[i] == '.')
			{
				gameCompleted = false;
				break;
			}
			if(diagR[i] == 'X') xAmount++;
			if(diagR[i] == 'O') oAmount++;
			if(diagR[i] == 'T') tFound = true;
		}
		if( (xAmount == 4) || (tFound && xAmount == 3 ) )
		{
			xWin = true;
		}

		if( (oAmount == 4) || (tFound && oAmount == 3 ) )
		{
			oWin = true;
		}

		string winText = "";

		if(xWin) winText = "X won";
		if(oWin) winText = "O won";
		if(gameCompleted && !xWin && !oWin) winText = "Draw";
		if(!gameCompleted && !xWin && !oWin) winText = "Game has not completed";

		cout << "Case #" << i+1 << ": " << winText <<  endl;

	}
	return 0;
}