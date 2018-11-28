#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T = 0; cin >> T;
	for (int x = 1; x <= T; x++)
	{
		cout << "Case #" << x << ": ";
		int nDOT = 0;
		bool isWin = false;
		string tic[4];
		int i, j;
		for (i = 0; i < 4; i++) cin >> tic[i];
		for (i = 0; i < 4; i++)
		{
			// row
			int O = 0, X = 0, Tt = 0, DOT = 0;
			for (j = 0; j < 4; j++)
			{
				if (tic[i][j] == 'O')
					O++;
				else if (tic[i][j] == 'X')
					X++;
				else if (tic[i][j] == '.')
					DOT++;
				else if (tic[i][j] == 'T')
					Tt++;
				if (X == 4 || (X == 3 && Tt == 1))
				{
					isWin = true;
					cout << "X won";
					break;
				}
				else if (O == 4 || (O == 3 && Tt == 1))
				{
					isWin = true;
					cout << "O won";
					break;
				}					
			}
			if (isWin) break;
			nDOT += DOT;
			// column
			O = 0; X = 0; Tt = 0;
			for (j = 0; j < 4; j++)
			{
				if (tic[j][i] == 'O')
					O++;
				else if (tic[j][i] == 'X')
					X++;
				else if (tic[j][i] == 'T')
					Tt++;
				if (X == 4 || (X == 3 && Tt == 1))
				{
					isWin = true;
					cout << "X won";
					break;
				}
				else if (O == 4 || (O == 3 && Tt == 1))
				{
					isWin = true;
					cout << "O won";
					break;
				}					
			}
			if (isWin) break;		
		}
		//diagonal
		if (!isWin)
		{
			int O = 0, X = 0, Tt = 0;
			for (i = 0; i < 4; i++)
			{
				if (tic[i][i] == 'O')
					O++;
				else if (tic[i][i] == 'X')
					X++;
				else if (tic[i][i] == 'T')
					Tt++;
			}
			if (X == 4 || (X == 3 && Tt == 1))
			{
				isWin = true;
				cout << "X won";
			}
			else if (O == 4 || (O == 3 && Tt == 1))
			{
				isWin = true;
				cout << "O won";
			}						
		}
		if (!isWin)
		{
			int O = 0, X = 0, Tt = 0;
			for (i = 0; i < 4; i++)
			{
				if (tic[i][3-i] == 'O')
					O++;
				else if (tic[i][3-i] == 'X')
					X++;
				else if (tic[i][3-i] == 'T')
					Tt++;
			}
			if (X == 4 || (X == 3 && Tt == 1))
			{
				isWin = true;
				cout << "X won";
			}
			else if (O == 4 || (O == 3 && Tt == 1))
			{
				isWin = true;
				cout << "O won";
			}						
		}		
		if (!isWin)
		{
			if (nDOT)
				cout << "Game has not completed";
			else
				cout << "Draw";
		}
		cout << endl;
	}
	return 0;
}