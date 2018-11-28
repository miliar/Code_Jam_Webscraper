#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	int T;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	fin >> T;

	int i, j, k;

	for(i = 0; i < T; i++)
	{
		char ** board = new char *[4];
		bool done = false, dots = false;

		for(j = 0; j < 4; j++)
		{
			board[j] = new char[4];
			fin >> board[j];
		}

		for(j = 0; j < 4 && !done; j++)
		{
			bool hWinX = true, hWinO = true;
			for(k = 0; k < 4 && !done; k++)
			{
				hWinX &= (board[j][k] == 'X') || (board[j][k] == 'T');
				hWinO &= (board[j][k] == 'O') || (board[j][k] == 'T');
				if(board[j][k] == '.')
					dots = true;
			}

			if(hWinX && !done)
			{
				fout << "Case #" << i + 1 << ":" << " X won" << std::endl;
				done = true;
				break;
			}

			if(hWinO && !done)
			{
				fout << "Case #" << i + 1 << ":" << " O won" << std::endl;
				done = true;
				break;
			}		
				

		}

		for(k = 0; k < 4 && !done; k++)
		{
			bool vWinX = true, vWinO = true;
			for(j = 0; j < 4 && !done; j++)
			{
				vWinX &= (board[j][k] == 'X') || (board[j][k] == 'T');
				vWinO &= (board[j][k] == 'O') || (board[j][k] == 'T');
			}

			if(vWinX)
			{
				fout << "Case #" << i + 1 << ":" << " X won" << std::endl;
				done = true;
				break;
			}

			if(vWinO)
			{
				fout << "Case #" << i + 1 << ":" << " O won" << std::endl;
				done = true;
				break;
			}
		}

		bool winX = true, winO = true;
		for(j = 0, k = 3; k >= 0 && j < 4 && !done; k--, j++)
		{			
			winX &= (board[j][k] == 'X') || (board[j][k] == 'T');
			winO &= (board[j][k] == 'O') || (board[j][k] == 'T');
		}

		if(winX && !done)
		{
			fout << "Case #" << i + 1 << ":" << " X won" << std::endl;
			done = true;
		}

		if(winO && !done)
		{
			fout << "Case #" << i + 1 << ":" << " O won" << std::endl;
			done = true;
		}
		
		winX = true, winO = true;
		for(j = 0, k = 0; k < 4 && j < 4 && !done; k++, j++)
		{			
			winX &= (board[j][k] == 'X') || (board[j][k] == 'T');
			winO &= (board[j][k] == 'O') || (board[j][k] == 'T');
		}

		if(winX && !done)
		{
			fout << "Case #" << i + 1 << ":" << " X won" << std::endl;
			done = true;
		}

		if(winO && !done)
		{
			fout << "Case #" << i + 1 << ":" << " O won" << std::endl;
			done = true;
		}

		if(!done && !dots)
		{
			fout << "Case #" << i + 1 << ":" << " Draw" << std::endl;
			done = true;
		}

		if(!done && dots)
		{
			fout << "Case #" << i + 1 << ":" << " Game has not completed" << std::endl;
			done = true;
		}
	}
	
	fin.close();
	fout.close();

}