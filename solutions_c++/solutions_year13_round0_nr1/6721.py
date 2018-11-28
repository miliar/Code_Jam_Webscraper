#include <iostream>

using namespace std;

bool checkAll(char*, char);
bool checkHorizontal(char*, char);
bool checkVertical(char*, char);
bool checkDiagonal(char*, char);

bool draw(char*);

int main() 
{
    
    int numCases;

    cin >> numCases;

    char* board = new char[16];
    for (int i = 0; i < numCases; i++)
    {
        for (int j = 0; j < 16; j++) {
            cin >> board[j];
        }

        cout << "Case #" << i + 1 << ":"; 
        if (checkAll(board, 'X'))
        {
            cout << " X won\n";
        }
        else if (checkAll(board, 'O'))
        {
            cout << " O won\n";
        }
        else if (draw(board))
        {
            cout << " Draw\n";
        }
        else 
        {
            cout << " Game has not completed\n";
        }
    }

    return 0;
}

bool checkAll(char* board, char player)
{
    return checkHorizontal(board, player) || checkVertical(board, player) || checkDiagonal(board, player);
}

bool checkHorizontal(char* board, char player) 
{
    return 
       (
        ((board[0]  == player || board[0]  == 'T') && (board[1]  == player || board[1]  == 'T') &&
         (board[2] == player || board[2] == 'T') && (board[3] == player || board[3] == 'T')) ||

        ((board[4]  == player || board[4]  == 'T') && (board[5]  == player || board[5]  == 'T') &&
         (board[6] == player || board[6] == 'T') && (board[7] == player || board[7] == 'T')) ||

        ((board[8]  == player || board[8]  == 'T') && (board[9]  == player || board[9]  == 'T') &&
         (board[10] == player || board[10] == 'T') && (board[11] == player || board[11] == 'T')) ||

        ((board[12]  == player || board[12]  == 'T') && (board[13]  == player || board[13]  == 'T') &&
         (board[14]  == player || board[14]  == 'T') && (board[15] == player || board[15] == 'T'))
        );
}

bool checkVertical(char* board, char player) 
{
    return 
       (
        ((board[0]  == player || board[0]  == 'T') && (board[4]  == player || board[4]  == 'T') &&
         (board[8] == player || board[8] == 'T') && (board[12] == player || board[12] == 'T')) ||

        ((board[1]  == player || board[1]  == 'T') && (board[5]  == player || board[5]  == 'T') &&
         (board[9] == player || board[9] == 'T') && (board[13] == player || board[13] == 'T')) ||

        ((board[2]  == player || board[2]  == 'T') && (board[6]  == player || board[6]  == 'T') &&
         (board[10] == player || board[10] == 'T') && (board[14] == player || board[14] == 'T')) ||

        ((board[3]  == player || board[3]  == 'T') && (board[7]  == player || board[7]  == 'T') &&
         (board[11]  == player || board[11]  == 'T') && (board[15] == player || board[15] == 'T'))
        );
}

bool checkDiagonal(char* board, char player) 
{
    return 
       (
        ((board[0]  == player || board[0]  == 'T') && (board[5]  == player || board[5]  == 'T') &&
         (board[10] == player || board[10] == 'T') && (board[15] == player || board[15] == 'T')) ||

        ((board[3]  == player || board[3]  == 'T') && (board[6]  == player || board[6]  == 'T') &&
         (board[9]  == player || board[9]  == 'T') && (board[12] == player || board[12] == 'T'))
        );
}

bool draw(char* board) 
{
    bool foundOpen = false;

    for (int i = 0; i < 16; i++)
    {
        if (board[i] == '.')
        {
            foundOpen = true;
            break;
        }
    }
    return !foundOpen;
}

