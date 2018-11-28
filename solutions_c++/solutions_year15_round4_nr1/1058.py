#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>
using namespace std;
const int MAXN = 105;

int Lowest[MAXN], Uppest[MAXN] , Right[MAXN] , Left[MAXN];
char f[MAXN][MAXN];

int main()
{
    freopen("inputA.in" , "r" , stdin );
    freopen("output.out" , "w" , stdout );

    int T;
    cin >> T;

    for ( int _t = 1; _t <= T; _t++ )
    {
        int R , C;
        cin >> R >> C;

        for ( int i = 1; i < MAXN ; i++ )
            Uppest[i] = Lowest[i] = Left[i] = Right[i] = 0;

        for ( int i = 1; i <= R; i++)
        {
            for ( int j = 1; j <= C; j++)
            {
                cin >> f[i][j];

                if ( f[i][j] == '.' )
                    continue;

                if ( Left[i] == 0 )
                    Left[i] = j;

                Right[i] = j;

                if ( Uppest[j] == 0 )
                    Uppest[j] = i;

                Lowest[j] = i;
            }
        }

        bool bad = false;
        int ans = 0;
        for ( int i = 1; i <= R; i++)
        {
            if ( Left[i] == Right[i] && Left[i] != 0 && Uppest[ Left[i] ] == Lowest[ Left[i] ])
                bad = true;

            if ( f[i][Left[i]] == '<' )
            {
                ans++;
                if ( Left[i] != Right[i] )
                    f[i][ Left[i] ] = '>';
                else
                {
                    if ( Uppest[Left[i]] != i )
                        f[i][ Left[ i ] ] = '^';
                    else
                        f[i][ Left[ i ] ] = 'v';
                }
            }

            if ( f[i][ Right[i] ] == '>' )
            {
                ans++;
                if ( Left[i] != Right[i] )
                    f[ i ][ Right[i] ] == '<';
                else
                {
                    if ( Uppest[Right[i]] != i )
                        f[i][ Right[ i ] ] = '^';
                    else
                        f[i][ Right[ i ] ] = 'v';
                }
            }
            //cout << i << " " << ans << endl;
        }

        for ( int i = 1; i <= C; i++)
        {
            if ( f[ Uppest[i] ][i] == '^' )
            {
                ans++;
                f[ Uppest[i] ][i] = '<';
            }

            if ( f[ Lowest[i] ][ i ] == 'v' ) ans++;
           //cout << i << " " << ans << endl;
        }

        if ( !bad )
            cout << "Case #" << _t << ": " << ans << endl;
        else
            cout << "Case #" << _t << ": " << "IMPOSSIBLE" << endl;
    }

    return 0;
}
