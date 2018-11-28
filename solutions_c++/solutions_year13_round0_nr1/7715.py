#include <iostream>
#include <cstdio>
#include <vector>

#define forn(i, n) for(int i = 0; i < n; i++)
#define fornx(i, x, n) for(int i = x; i < n; i++)

using namespace std;

typedef vector<char> vchar;
typedef vector<vchar> vvchar;

const int n = 4;

bool no_space_left(vvchar& board)
{
	forn(i, n)
	{
		forn(j, n)
		{
			if (board[i][j] == '.')
			{
				return false;
			}
		}
	}

	return true;
}

int main(void)
{
	int casos;
	cin >> casos;    
  
	forn(caso, casos)
	{		
		vvchar board (n, vchar(n));

		forn(i, n)
		{
			forn(j, n)
			{
				cin >> board[i][j];
			}
		}

		// forn(i, n)
		// {
		// 	forn(j, n)
		// 	{
		// 		cout << board[i][j] << " ";
		// 	}
		// 	cout << endl;
		// }

		// cout << "Hello" << endl;
		
		bool finished = no_space_left(board);
		bool winner = false;
		char sol;

		/* Rows */
		forn(i, n)
		{
			char c = board[i][0];

			if (c == '.')
				continue;

			bool res = true;
			fornx(j, 1, n)
			{
				if (not((board[i][j] == c) or (board[i][j] == 'T')))
					res = false;
			}

			if (res)
			{
				if (c == 'T')
					c = board[i][n - 1];

				sol = c;
				winner = true;
				break;
			}
		}

		/* Cols */
		forn(j, n)
		{
			char c = board[0][j];

			if (c == '.')
				continue;

			bool res = true;

			fornx(i, 1, n)
			{
				if (not((board[i][j] == c) or (board[i][j] == 'T')))
					res = false;
			}

			if (res)
			{
				if (c == 'T')
					c = board[n - 1][j];

				sol = c;
				winner = true;
				break;
			}
		}

		/* Diag1 */
		char c = board[0][0];
		bool res = true;
		if (c != '.')
		{
			fornx(i, 1, n)
			{
				if (not((board[i][i] == c) or (board[i][i] == 'T')))
					res = false;
			}

			if (res)
			{
				if (c == 'T')
					c = board[n - 1][n - 1];

				sol = c;
				winner = true;
			}
		}

		/* Diag2 */
		c = board[0][n - 1];		
		res = true;
		if (c != '.')
		{
			fornx(i, 1, n)
			{
				if (not((board[i][(n - 1) - i] == c) or (board[i][(n - 1) - i] == 'T')))
					res = false;
			}

			if (res)
			{
				if (c == 'T')
					c = board[n - 1][0];

				sol = c;
				winner = true;
			}
		}
    
    cout << "Case #" << caso + 1 << ": ";    
    
    if (winner)
    {
    	cout << (char) toupper(sol) << " won" << endl;
    }
    else
    {
    	if (finished)
    	{
    		cout << "Draw" << endl;
    	}
    	else
    	{
    		cout << "Game has not completed" << endl;
    	}
    }
	}

	return 0;
}