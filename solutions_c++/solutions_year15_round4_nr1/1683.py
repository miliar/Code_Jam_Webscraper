#include <iostream>
using namespace std;

char board[10][10];
char boardCopy[10][10];
int r, c;
int minimum;

bool canWalk(int row, int col)
{
    if (boardCopy[row][col] == '.') return true;
    bool visited[10][10];
    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            visited[i][j] = false;
    visited[row][col] = true;
    while (row >= 0 && row < r&&col >= 0 && col < c)
    {
        int dx = 0, dy = 0;
        if (boardCopy[row][col] == '^'){ dx = -1; dy = 0; }
        else if (boardCopy[row][col] == '>'){ dx = 0; dy = 1; }
        else if (boardCopy[row][col] == '<'){ dx = 0; dy = -1; }
        else if (boardCopy[row][col] == 'v'){ dx = 1; dy = 0; }
        row += dx; col += dy;
        while (row >= 0 && row < r&&col >= 0 && col < c)
        {
            if (board[row][col] == '.')
            {
                row += dx; col += dy; continue;
            }
            if (visited[row][col]) goto Done;
            visited[row][col] = true;
        }
    }
Done:;
    return row >= 0 && row < r&&col >= 0 && col < c;
}

int check()
{
    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            if (!canWalk(i, j))
                return -1;
    int need = 0;
    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            if (board[i][j] != boardCopy[i][j])
                ++need;
    return need;
}

void calculate(int row, int col, int diff)
{
    if (minimum != -1 && minimum <= diff) return;
    if (row == r)
    {
        // check
        int need = check();
        if (need != -1)
            if (minimum == -1 || minimum > need)
            {
                minimum = need;
                //cout << minimum << endl;
            }
        return;
    }
    if (col == c)
    {
        calculate(row + 1, 0, diff);
        return;
    }
    if (board[row][col] == '.')
    {
        calculate(row, col + 1, diff);
    }
    else
    {
        if (row != 0)
        {
            boardCopy[row][col] = '^';
            calculate(row, col + 1, diff + (boardCopy[row][col] == board[row][col] ? 0 : 1));
        }
        if (col != c - 1)
        {
            boardCopy[row][col] = '>';
            calculate(row, col + 1, diff + (boardCopy[row][col] == board[row][col] ? 0 : 1));
        }
        if (row != r - 1)
        {
            boardCopy[row][col] = 'v';
            calculate(row, col + 1, diff + (boardCopy[row][col] == board[row][col] ? 0 : 1));
        }
        if (col != 0)
        {
            boardCopy[row][col] = '<';
            calculate(row, col + 1, diff + (boardCopy[row][col] == board[row][col] ? 0 : 1));
        }
    }
}

int main()
{
    int cases;
    cin >> cases;
    for (int t = 1; t <= cases; ++t)
    {
        cout << "Case #" << t << ": ";
        cin >> r >> c;
        
        for (int i = 0; i < r; ++i)
            cin >> board[i];
        
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j)
                boardCopy[i][j] = board[i][j];

        minimum = -1;
        calculate(0, 0, 0);
        if (minimum == -1) cout << "IMPOSSIBLE" << endl;
        else cout << minimum << endl;
    }
    return 0;
}
