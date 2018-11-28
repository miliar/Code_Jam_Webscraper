#include <iostream>
#include <sstream>
#include <vector>
#include <string>

#include <cstdio>

using namespace std;

char board[4][4];
bool hasDot;

char check(int x, int y, int dx, int dy)
{
    char winner = board[x][y];
    if (winner == 'T')
        winner = board[x + dx][y + dy];

    for (int i = 0; i < 4; i++)
    {
        if (board[x][y] == '.') hasDot = true;

        if (board[x][y] != winner && board[x][y] != 'T')
            winner = 'N';

        x += dx; y += dy;
    }
    
    return (winner != '.') ? winner : 'N';
}

string isWinner(char a)
{
    string tmp;
    stringstream ss;
    ss << a;
    ss >> tmp;

    return (tmp + " won");
}

string solve()
{
    hasDot = false;
    for (int r = 0; r < 4; r++)
        scanf("%c%c%c%c\n", &board[r][0], &board[r][1], 
                            &board[r][2], &board[r][3]);

    // Check rows
    for (int r = 0; r < 4; r++)
    {
        char res = check(r, 0, 0, 1);
        if (res != 'N') 
        {
            return isWinner(res);
        }
    }
    
    // Check columns
    for (int c = 0; c < 4; c++)
    {
        char res = check(0, c, 1, 0);
        if (res != 'N') 
        {
            return isWinner(res);
        }
    }
    
    // Check diagonals
    char diag1 = check(0, 0, 1, 1);
    if (diag1 !='N') return isWinner(diag1);

    char diag2 = check(3, 0, -1, 1);
    if (diag2 !='N') return isWinner(diag2);

    if (hasDot) 
        return "Game has not completed";

    return "Draw";
}

int main()
{
    int T;
    scanf("%d\n", &T);

    for (int i = 0; i < T; i++)
    {
        printf ("Case #%d: %s\n", i+1, solve().c_str());
    }
    
        
    return 0;
}
