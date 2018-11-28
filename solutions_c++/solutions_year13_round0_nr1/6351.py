#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen ("in.txt", "r", stdin);
    freopen ("AoutLarge.txt", "w", stdout);
    int t;
    char M[4][4];
    cin >> t;
    for (int k=1; k<=t; k++)
    {
        int c = 0;
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                cin >> M[i][j];
                if (M[i][j] == 'X' || M[i][j] == 'O' || M[i][j] == 'T')
                    c++;
            }
        }
        char ans = '.', act;
        bool X = false, Y = false;
        if ( (M[0][0] == 'X' || M[0][0] == 'T') &&
             (M[1][1] == 'X' || M[1][1] == 'T') &&
             (M[2][2] == 'X' || M[2][2] == 'T') &&
             (M[3][3] == 'X' || M[3][3] == 'T'))
             X = true;
        if ( (M[0][0] == 'O' || M[0][0] == 'T') &&
             (M[1][1] == 'O' || M[1][1] == 'T') &&
             (M[2][2] == 'O' || M[2][2] == 'T') &&
             (M[3][3] == 'O' || M[3][3] == 'T'))
             Y = true;
        if ( (M[3][0] == 'X' || M[3][0] == 'T') &&
             (M[2][1] == 'X' || M[2][1] == 'T') &&
             (M[1][2] == 'X' || M[1][2] == 'T') &&
             (M[0][3] == 'X' || M[0][3] == 'T'))
             X = true;
        if ( (M[3][0] == 'O' || M[3][0] == 'T') &&
             (M[2][1] == 'O' || M[2][1] == 'T') &&
             (M[1][2] == 'O' || M[1][2] == 'T') &&
             (M[0][3] == 'O' || M[0][3] == 'T'))
             Y = true;

        for (int i=0; i<4; i++)
        {
            if ( (M[i][0] == 'X' || M[i][0] == 'T') &&
                 (M[i][1] == 'X' || M[i][1] == 'T') &&
                 (M[i][2] == 'X' || M[i][2] == 'T') &&
                 (M[i][3] == 'X' || M[i][3] == 'T'))
                    X = true;
            if ( (M[i][0] == 'O' || M[i][0] == 'T') &&
                 (M[i][1] == 'O' || M[i][1] == 'T') &&
                 (M[i][2] == 'O' || M[i][2] == 'T') &&
                 (M[i][3] == 'O' || M[i][3] == 'T'))
                    Y = true;
            if ( (M[0][i] == 'X' || M[0][i] == 'T') &&
                 (M[1][i] == 'X' || M[1][i] == 'T') &&
                 (M[2][i] == 'X' || M[2][i] == 'T') &&
                 (M[3][i] == 'X' || M[3][i] == 'T'))
                    X = true;
            if ( (M[0][i] == 'O' || M[0][i] == 'T') &&
                 (M[1][i] == 'O' || M[1][i] == 'T') &&
                 (M[2][i] == 'O' || M[2][i] == 'T') &&
                 (M[3][i] == 'O' || M[3][i] == 'T'))
                    Y = true;
        }
        cout << "Case #" << k << ": ";
        if (X && Y || (c == 16 && !X && !Y))
            cout << "Draw" << endl;
        else if (X && !Y)
            cout << "X won" << endl;
        else if (!X && Y)
            cout << "O won" << endl;
        else if (!X && !Y)
            cout << "Game has not completed" << endl;

    }
    fclose (stdout);
    return 0;
}
