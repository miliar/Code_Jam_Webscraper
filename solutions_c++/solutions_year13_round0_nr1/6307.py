#include <iostream>
#include <string>
#include <fstream>

using namespace std;

bool isCompleted (char[4][4]);
char checkRow (int, char[4][4]);
char checkCol (int, char[4][4]);
char checkDiag (int diag, char board[4][4]);

int main ()
{
    int testCases, fakeValue;
    char board[4][4];
    string inputStr;
    bool end = false;
	ofstream outfile;
	ifstream infile;
	
	infile.open("A-large.in");
	outfile.open("output.txt");
    
    //cin >> testCases;
    infile >> testCases;
	
    for (int t=0; t<testCases; t++)
    {
        // input
        for (int i=0; i<4; i++)
        {
            infile >> inputStr;
            board[i][0] = inputStr[0];
            board[i][1] = inputStr[1];
            board[i][2] = inputStr[2];
            board[i][3] = inputStr[3];
        }
        
        end = false;
        
		char ret;
		
		for (int i=0; i<4; i++)
		{
			ret = checkRow (i, board);
			if (ret == 'X')
			{
				outfile << "Case #" << t+1 << ": X won\n";
				end = true;
			}
			else if (ret == 'O') 
			{
				outfile << "Case #" << t+1 << ": O won\n";
				end = true;
			}
		}
        
		if (!end)
            for (int i=0; i<4; i++)
            {
                ret = checkCol (i, board);
                if (ret == 'X') 
                {
                    outfile << "Case #" << t+1 << ": X won\n";
                    end = true;
                }
                else if (ret == 'O') 
                {
                    outfile << "Case #" << t+1 << ": O won\n";
                    end = true;
                }
            }
		
		if (!end)
            for (int i=0; i<2; i++)
            {
                ret = checkDiag (i, board);
                if (ret == 'X')
                {
                    outfile << "Case #" << t+1 << ": X won\n";
                    end = true;
                }
                else if (ret == 'O')
                {
                    outfile << "Case #" << t+1 << ": O won\n";
                    end = true;
                }
            }
        
		if (!end)
            if (isCompleted(board)) outfile << "Case #" << t+1 << ": Draw\n";
            else
            {
                outfile << "Case #" << t+1 << ": Game has not completed\n";
            }
    }
    return 0;
}

bool isCompleted (char board [4][4])
{
    for (int i=0; i<4; i++)
        for (int j=0; j<4; j++)
            if (board[i][j] == '.')
                return false;
    return true;
}

char checkDiag (int diag, char board[4][4])
{
    int nOfX = 0, nOfO = 0;
    
    for (int i=0; i<4; i++)
    {
        if (diag == 0)
        {
            if (board[i][i] == 'X') nOfX++;
            else if (board[i][i] == 'O') nOfO++;
            else if (board[i][i] == 'T')
            {
                nOfX++; nOfO++;
            } 
        }
        else if (diag == 1)
        {
            if (board[i][3-i] == 'X') nOfX++;
            else if (board[i][3-i] == 'O') nOfO++;
            else if (board[i][3-i] == 'T')
            {
                nOfX++; nOfO++;
            }
        }
    }
    
    if (nOfX == 4) return 'X';
    else if (nOfO == 4) return 'O';
    else return 'C';
}

char checkCol (int col, char board [4][4])
{
    int nOfX = 0, nOfO = 0;
    
    for (int i=0; i<4; i++)
    {
        if (board[i][col] == 'X') nOfX++;
        else if (board[i][col] == 'O') nOfO++;
        else if (board[i][col] == 'T')
        {
            nOfX++; nOfO++;
        }
    }
    
    if (nOfX == 4) return 'X';
    else if (nOfO == 4) return 'O';
    else return 'C';
}

char checkRow (int row, char board [4][4])
{
    int nOfX = 0, nOfO = 0;
    
    for (int i=0; i<4; i++)
    {
        if (board[row][i] == 'X') nOfX++;
        else if (board[row][i] == 'O') nOfO++;
        else if (board[row][i] == 'T')
        {
            nOfX++; nOfO++;
        }
    }
    
    if (nOfX == 4) return 'X';
    else if (nOfO == 4) return 'O';
    else return 'C';
}
