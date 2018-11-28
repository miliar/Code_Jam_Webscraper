#include <iostream>

using namespace std;

int main ()
{
	int T;
	cin >> T;
	//cout << "T = " << T << endl;
	char board [4][4];
	
	int global_flag = 0, tmp_flag = 0;
	/* 	1 - "X won" (the game is over, and X won)
		2 - "O won" (the game is over, and O won)
		0 - "Draw" (the game is over, and it ended in a draw)
		3 - "Game has not completed" (the game is not over yet)
	 */
	
		
	for (int t = 0; t < T; t ++)
	{
		global_flag = 0;
		
		cin.ignore();
		//cout << "=====================================\nCase #" << t << endl;
		// Reading each board of tour
		for (int i = 0; i < 4; i ++)
		{
			for (int j = 0; j < 4; j ++)
			{
				cin.get (board[i][j]);		
			}
			cin.ignore ();
		}
		// Writing each board of tour		
		/*for (int i = 0; i < 4; i ++)
		{
			for (int j = 0; j < 4; j ++)
			{
				cout << board[i][j];
			}
			cout << endl;
		}*/
		
		//cout << "Possible varints:" << endl;
		for (int i = 0; i < 4; i ++)
		{
			tmp_flag = 0;
			
			//cout << "Varint: ";
			for (int j = 0; j < 4; j ++)
			{
				//cout << board[i][j];
				
				if (board[i][j] == '.')
				{
					tmp_flag = 3; // "Game has not completed"
				}
				else if ( tmp_flag != 3 )
				{
					if ( (board[i][j] == 'X' || board[i][j] == 'T') && tmp_flag != 2 )
						tmp_flag = 1;	// "X won"
					else if ( (board[i][j] == 'O' || board[i][j] == 'T') && tmp_flag != 1 )
						tmp_flag = 2;	// "O won"
					else
					{
						tmp_flag = 0;	// "Draw"
						break;
					}
				}
			}
			
	/* 	1 - "X won" (the game is over, and X won)
		2 - "O won" (the game is over, and O won)
		0 - "Draw" (the game is over, and it ended in a draw)
		3 - "Game has not completed" (the game is not over yet)
	 */
	 
			if ( (global_flag > tmp_flag && tmp_flag != 0 ) || global_flag == 0 )
				global_flag = tmp_flag;
			/*if ( global_flag == 0 )
				cout << "\tDraw" << endl;
			else if ( global_flag == 1 )
				cout << "\tX won" << endl;
			else if ( global_flag == 2 )
				cout << "\tO won" << endl;
			else if ( global_flag == 3 )
				cout << "\tGame has not completed" << endl;*/
			
		}
		//cout << endl;
		
		for (int i = 0; i < 4; i ++)
		{
			tmp_flag = 0;
			
			//cout << "Varint: ";
			for (int j = 0; j < 4; j ++)
			{
				//cout << board[j][i];
				
				if (board[j][i] == '.')
				{
					tmp_flag = 3; // "Game has not completed"
				}
				else if ( tmp_flag != 3 )
				{
					if ( (board[j][i] == 'X' || board[j][i] == 'T') && tmp_flag != 2 )
						tmp_flag = 1;	// "X won"
					else if ( (board[j][i] == 'O' || board[j][i] == 'T') && tmp_flag != 1 )
						tmp_flag = 2;	// "O won"
					else
					{
						tmp_flag = 0;	// "Draw"
						break;
					}
				}
			}
			
			if ( (global_flag > tmp_flag && tmp_flag != 0 ) || global_flag == 0 )
				global_flag = tmp_flag;
			/*if ( global_flag == 0 )
				cout << "\tDraw" << endl;
			else if ( global_flag == 1 )
				cout << "\tX won" << endl;
			else if ( global_flag == 2 )
				cout << "\tO won" << endl;
			else if ( global_flag == 3 )
				cout << "\tGame has not completed" << endl;*/
				
		}
		//cout << endl;
		
		tmp_flag = 0;
		//cout << "Varint: ";
		for (int i = 0; i < 4; i ++)
		{
			//cout << board[i][i];
			
			if (board[i][i] == '.')
				{
					tmp_flag = 3; // "Game has not completed"
				}
				else if ( tmp_flag != 3 )
				{
					if ( (board[i][i] == 'X' || board[i][i] == 'T') && tmp_flag != 2 )
						tmp_flag = 1;	// "X won"
					else if ( (board[i][i] == 'O' || board[i][i] == 'T') && tmp_flag != 1 )
						tmp_flag = 2;	// "O won"
					else
					{
						tmp_flag = 0;	// "Draw"
						break;
					}
				}
		}
		
		if ( (global_flag > tmp_flag && tmp_flag != 0 ) || global_flag == 0 )
				global_flag = tmp_flag;
		/*if ( global_flag == 0 )
				cout << "\tDraw" << endl;
			else if ( global_flag == 1 )
				cout << "\tX won" << endl;
			else if ( global_flag == 2 )
				cout << "\tO won" << endl;
			else if ( global_flag == 3 )
				cout << "\tGame has not completed" << endl;*/
		
		tmp_flag = 0;
		//cout << "Varint: ";
		for (int i = 0; i < 4; i ++)
		{
			//cout << board[i][3-i];
			
			if (board[i][3-i] == '.')
				{
					tmp_flag = 3; // "Game has not completed"
				}
				else if ( tmp_flag != 3 )
				{
					if ( (board[i][3-i] == 'X' || board[i][3-i] == 'T') && tmp_flag != 2 )
						tmp_flag = 1;	// "X won"
					else if ( (board[i][3-i] == 'O' || board[i][3-i] == 'T') && tmp_flag != 1 )
						tmp_flag = 2;	// "O won"
					else
					{
						tmp_flag = 0;	// "Draw"
						break;
					}
				}
		}
		
		if ( (global_flag > tmp_flag && tmp_flag != 0 ) || global_flag == 0 )
				global_flag = tmp_flag;
		/*if ( global_flag == 0 )
				cout << "\tDraw" << endl;
			else if ( global_flag == 1 )
				cout << "\tX won" << endl;
			else if ( global_flag == 2 )
				cout << "\tO won" << endl;
			else if ( global_flag == 3 )
				cout << "\tGame has not completed" << endl;*/
				
		//cout << endl;
		if ( global_flag == 0 )
			cout << "Case #" << t+1 << ": Draw" << endl;
		else if ( global_flag == 1 )
			cout << "Case #" << t+1 << ": X won" << endl;
		else if ( global_flag == 2 )
			cout << "Case #" << t+1 << ": O won" << endl;
		else if ( global_flag == 3 )
			cout << "Case #" << t+1 << ": Game has not completed" << endl;																					
	}
	
		
	cin.ignore();
	return 0;
}
