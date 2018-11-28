#include <iostream>
#include <cstring>

using namespace std;

string checkBoard (char board[4][4])
{
        //check for horizontal X wins
        for(int j = 0; j < 4; j++)
        {
            if(board[j][0] == 'X' || board[0][0] == 'T'){
                if(board[j][1] == 'X' || board[0][1] == 'T'){
                    if(board[j][2] == 'X' || board[0][2] == 'T'){
                        if(board[j][3] == 'X' || board[0][3] == 'T'){
                            return "X won";
                        }
                    }
                }
            }
        }

        //check for horizontal O wins
        for(int j = 0; j < 4; j++)
        {
            if(board[j][0] == 'O' || board[0][0] == 'T'){
                if(board[j][1] == 'O' || board[0][1] == 'T'){
                    if(board[j][2] == 'O' || board[0][2] == 'T'){
                        if(board[j][3] == 'O' || board[0][3] == 'T'){
                            return "O won";
                        }
                    }
                }
            }
        }

        //check for vertical X wins
        for(int j = 0; j < 4; j++)
        {
            if(board[0][j] == 'X' || board[0][0] == 'T'){
                if(board[1][j] == 'X' || board[0][1] == 'T'){
                    if(board[2][j] == 'X' || board[0][2] == 'T'){
                        if(board[3][j] == 'X' || board[0][3] == 'T'){
                            return "X won";
                        }
                    }
                }
            }
        }

        //check for vertical O wins
        for(int j = 0; j < 4; j++)
        {
            if(board[0][j] == 'O' || board[0][0] == 'T'){
                if(board[1][j] == 'O' || board[0][1] == 'T'){
                    if(board[2][j] == 'O' || board[0][2] == 'T'){
                        if(board[3][j] == 'O' || board[0][3] == 'T'){
                            return "O won";
                        }
                    }
                }
            }
        }

        //check for diagonal X wins
        if(board[0][0] == 'X' || board[0][0] == 'T'){
            if(board[1][1] == 'X' || board[1][1] == 'T'){
                if(board[2][2] == 'X' || board[2][2] == 'T'){
                    if(board[3][3] == 'X' || board[3][3] == 'T'){
                        return "X won";
                    }
                }
            }
        }

        if(board[3][0] == 'X' || board[3][0] == 'T'){
            if(board[2][1] == 'X' || board[2][1] == 'T'){
                if(board[1][2] == 'X' || board[1][2] == 'T'){
                    if(board[0][3] == 'X' || board[0][3] == 'T'){
                        return "X won";
                    }
                }
            }
        }

        //check for diagonal O wins
        if(board[0][0] == 'O' || board[0][0] == 'T'){
            if(board[1][1] == 'O' || board[1][1] == 'T'){
                if(board[2][2] == 'O' || board[2][2] == 'T'){
                    if(board[3][3] == 'O' || board[3][3] == 'T'){
                        return "O won";
                    }
                }
            }
        }

        if(board[3][0] == 'O' || board[3][0] == 'T'){
            if(board[2][1] == 'O' || board[2][1] == 'T'){
                if(board[1][2] == 'O' || board[1][2] == 'T'){
                    if(board[0][3] == 'O' || board[0][3] == 'T'){
                        return "O won";
                    }
                }
            }
        }

        //check if the game's over
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                if(board[j][k] == '.'){
                    return "Game has not completed";
                }
            }
        }

        return "Draw";
}

int main()
{
    int testCases;
    char board[4][4];
    string result;

    cin >> testCases;

    for(int i = 0; i < testCases; i++)
    {
        //load the current board
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                cin >> board[j][k];
            }
        }

        cout << "Case #"<< i+1 << ": " << checkBoard(board) << "\n";
    }
}
