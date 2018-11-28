#include <iostream>

using namespace std;

int checkwin(char *board, int i1, int j1, int i2, int j2, int i3, int j3, int i4, int j4)
{
    char x = board[i1*4 + j1] == 'T'? board[i2*4 + j2]: board[i1*4 + j1];

    if (x == '.')
        return false;

    if ((board[i1*4 + j1] == x || board[i1*4 + j1] == 'T') && (board[i2*4 + j2] == x || board[i2*4 + j2] == 'T') && (board[i3*4 + j3] == x || board[i3*4 + j3] == 'T') && (board[i4*4 + j4] == x || board[i4*4 + j4] == 'T'))
        return true;
    return false;
}

void print_win(char *board, int i, int j)
{
    cout << board[i*4 + j] << " won\n";
}

void print_progress()
{
    cout << "Game has not completed\n";
}

void print_draw()
{
    cout << "Draw\n";
}

int main()
{
    int t;
    cin >> t;

    for (int z = 0; z < t; z++)
    {
        char board[16];
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> board[i*4 + j];

        cout << "Case #" << (z+1) << ": ";

        for (int i = 0; i < 4; i++)
        {
            if (checkwin(board, i, 0, i, 1, i, 2, i, 3))
            {
                print_win(board, i, 0);
                goto OUT;
            }

            if (checkwin(board, 0, i, 1, i, 2, i, 3, i))
            {
                print_win(board, 0, i);
                goto OUT;
            }
        }


        if (checkwin(board, 0, 0, 1, 1, 2, 2, 3, 3))
        {
            print_win(board, 0, 0);
            goto OUT;
        }

        if (checkwin(board, 0, 3, 1, 2, 2, 1, 3, 0))
        {
            print_win(board, 0, 3);
            goto OUT;
        }

        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (board[i*4 + j] == '.')
                {
                    print_progress();
                    goto OUT;
                }

        print_draw();
        OUT:
        ;
    }

    return 0;
}
