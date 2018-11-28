#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
    string st[5];
    int i, j, k, l, inc, crnt, x, o, t, d, caseno = 0, T;
    char win;
    scanf ( "%d", &T );

    for ( k = 0; k < T; k++ )   {
        inc = 0;
        win = 0;
        for ( i = 0; i < 4; i++ )   {
            cin >> st[i];
            if ( st[i].size() == 0 )   i--;
        }

        for ( i = 0; i < 4 && !win; i++ )   {
            x = 0, o = 0, t = 0;
            for ( j = 0; j < 4; j++ )   {
                if ( st[i][j] == '.' )  {
                    inc = 1;
                    break;
                }

                switch (st[i][j])   {
                    case 'X':
                        x++;
                        break;
                    case 'O':
                        o++;
                        break;
                    case 'T':
                        t++;
                        break;
                }
            }
            if ( x == 4 || (x==3 && t== 1) )    win = 'X';
            else if ( o == 4 || (o==3&&t==1))   win = 'O';
            else    win = 0;
        }

        if ( !win ) {
            for ( i = 0; i < 4 && !win; i++ )   {
                x = 0, o = 0, t = 0;
                for ( j = 0; j < 4; j++ )   {
                    if ( st[j][i] == '.' )  {
                        inc = 1;
                        break;
                    }

                    switch (st[j][i])   {
                        case 'X':
                            x++;
                            break;
                        case 'O':
                            o++;
                            break;
                        case 'T':
                            t++;
                            break;
                    }
                }
                if ( x == 4 || (x==3 && t== 1) )    win = 'X';
                else if ( o == 4 || (o==3&&t==1))   win = 'O';
                else    win = 0;
            }
        }

        crnt = st[0][0];
        if ( !win ) {
            x = 0, o = 0, t = 0;
            for ( j = 0; j < 4; j++ )   {
                if ( st[j][j] == '.' )  {
                    inc = 1;
                    break;
                }
                switch (st[j][j])   {
                    case 'X':
                        x++;
                        break;
                    case 'O':
                        o++;
                        break;
                    case 'T':
                        t++;
                        break;
                }
            }
            if ( x == 4 || (x==3 && t== 1) )    win = 'X';
            else if ( o == 4 || (o==3&&t==1))   win = 'O';
            else    win = 0;
        }

        if ( !win ) {
            x = 0, o = 0, t = 0;
            for ( j = 0; j < 4; j++ )   {
                if ( st[3-j][j] == '.' )  {
                    inc = 1;
                    break;
                }

                switch (st[3-j][j])   {
                    case 'X':
                        x++;
                        break;
                    case 'O':
                        o++;
                        break;
                    case 'T':
                        t++;
                        break;
                }
            }
            if ( x == 4 || (x==3 && t== 1) )    win = 'X';
            else if ( o == 4 || (o==3&&t==1))   win = 'O';
            else    win = 0;
        }
        printf ( "Case #%d: ", ++caseno );
        if ( win )  printf ( "%c won\n", win );
        else if ( !inc )    printf ( "Draw\n" );
        else    printf ( "Game has not completed\n");
    }
    return 0;
}
