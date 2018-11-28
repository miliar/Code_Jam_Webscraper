#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;

bool WinX;
bool WinO;

void check(int sum)
{
    if (sum == 4 || sum == 3)
        WinX = true;
    else if (sum == 15 || sum == 20)
        WinO = true;
}

int main(int argc, char** argv)
{
        ifstream in ("tic.in", ifstream::in);
        ofstream out ("tic.out", ofstream::out);

        int N;

	in >> N;

        char symbol;
        int board[4][4];

	for (int game = 1; game <= N; game++)
	{
	    bool emptyCells = false;

            for (int x = 0; x < 4; x++)
            {
                for (int y = 0;y < 4; y++)
                {
                    in >> symbol;

                    if (symbol == 'X')
                        board[x][y] = 1;
                    else if (symbol == 'O')
                        board[x][y] = 5;
                    else if (symbol == '.')
                    {
                        board[x][y] = -30;
                        emptyCells = true;
                    }
                    else if (symbol == 'T')
                        board[x][y] = 0;
                }
            }

            WinX = false;
            WinO = false;

            check(board[0][0]+board[1][1]+board[2][2]+board[3][3]);
            check(board[0][3]+board[1][2]+board[2][1]+board[3][0]);

            for (int i = 0; i < 4; i++)
            {
                check(board[0][i]+board[1][i]+board[2][i]+board[3][i]);
                check(board[i][0]+board[i][1]+board[i][2]+board[i][3]);
            }

            out << "Case #" << game << ": ";

            if (WinX && WinO || (!WinX && !WinO && !emptyCells))
                out << "Draw\n";
            else if (!WinX && !WinO)
                out << "Game has not completed\n";
            else if (WinX)
                out << "X won\n";
            else 
                out << "O won\n";
        }

        out.close();
        in.close();

}
