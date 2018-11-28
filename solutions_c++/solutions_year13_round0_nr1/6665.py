#include <iostream>
using namespace std;

char board[4][4];


void solve(void)
{
    char first;
    bool w;

    /*for(int row = 0; row < 4; row++)
        for(int col = 0; col < 4; col++)
        {
            cout << board[row][col];
        }*/

    //check rows
    for(int row = 0; row < 4; row++)
    {
        //first = board[1][1];
        //if(board[row][0] == '.') continue;

        if(board[row][0] != 'T') first = board[row][0];
        else first = board[row][1];

        if(first == '.') continue;

        //cout << "First is " << first << " or "<< board[1][1] << endl;

        w = true;

        for(int col = 1; col < 4; col++)
        {
            if (board[row][col] == first || board[row][col] == 'T') continue;
            else {w = false; break;}
        }

        if(w)
        {
            cout << first << " won" << endl;
            return;
        }
    }

    //check cols
    for(int col = 0; col < 4; col++)
    {
        if(board[0][col] == '.') continue;

        if(board[0][col] != 'T') first = board[0][col];
        else first = board[1][col];

        if(first == '.') continue;

        w = true;

        for(int row = 1; row < 4; row++)
        {
            if (board[row][col] == first || board[row][col] == 'T') continue;
            else {w = false; break;}
        }

        if(w)
        {
            cout << first << " won" << endl;
            return;
        }
    }

    //check prime diagonal
    if(board[0][0] != 'T') first = board[0][0];
    else first = board[1][1];

    w = true;
    if(first == '.') w = false;


    for(int i=0; i<4; i++)
    {
        if(board[i][i] == first || board[i][i] == 'T') continue;
        else {w = false; break;}
    }

    if(w)
    {
        cout << first << " won" << endl;
        return;
    }

    //check secondary diagonal
    if(board[0][3] != 'T') first = board[0][3];
    else first = board[1][2];

    w = true;
    if(first == '.') w = false;

    for(int i=0; i<4; i++)
    {
        if(board[i][3-i] == first || board[i][3-i] == 'T') continue;
        else {w = false; break;}
    }

    if(w)
    {
        cout << first << " won" << endl;
        return;
    }

    //check if draw
    for(int row = 0; row < 4; row++)
        for(int col = 0; col < 4; col++)
        {
            if(board[row][col] == '.')
            {
                cout << "Game has not completed" << endl;
                return;
            }
        }

    cout << "Draw" << endl;


}

int main()
{
    int T;
    //char board[4][4];

    cin >> T;

    for(int i=0; i<T; i++)
    {
        for(int row = 0; row < 4; row++)
            for(int col = 0; col < 4; col++)
            {
                cin >> board[row][col];
            }

        /*for(int row = 0; row < 4; row++)
            for(int col = 0; col < 4; col++)
            {
                cout << board[row][col];
            }*/

        cout << "Case #" << i+1 << ": ";
        solve();
    }


}
