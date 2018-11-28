#include <iostream>
#include <cstdio>
using namespace std;
const int MAXN = 20;

int a[MAXN][MAXN];

void setGrid( int R , int C )
{
    for ( int i = 0; i < R; i++ )
    {
        for ( int j = 0; j < C; j++ )
            a[i][j] = 0;
    }
}

bool isTaken( int x , int y , int R , int C )
{
    if ( x < 0 || x >= R || y < 0 || y >= C )  return false;
    return a[x][y] == 1;
}

int checkGrid( int R , int C )
{
    int res = 0;
    for ( int i = 0; i < R; i++ )
    {
        for ( int j = 0; j < C; j++ )
        {
            //cout << a[i][j];
            if ( isTaken( i , j , R , C ) && isTaken( i , j + 1 , R , C ) ) res++;
            if ( isTaken( i , j , R , C ) && isTaken( i + 1 , j , R , C ) ) res++;
        }
        //cout << endl;
    }
    //cout << "/////////////" << endl;
    return res;
}

int bits( int x )
{
    int res = 0;
    while ( x > 0 )
    {
        res += (x % 2);
        x /= 2;
    }
    return res;
}

int main()
{
    freopen("inputB.in" , "r" , stdin );
    freopen("output.out" , "w" , stdout );

    int T;
    cin >> T;

    for ( int _t = 1; _t <= T; _t++ )
    {
        int R, C, N;
        cin >> R >> C >> N;

        int RC = R * C;
        int ans = 100 * RC;

        for (int i = 0; i < (1 << RC) ; i++)
        {
            if ( bits( i ) != N ) continue;
            setGrid( R , C );

            for ( int j = 0; j < RC; j++ )
            {
                int pow = (1 << j);
                if ( (pow & i) == 0 ) continue;
                a[ j % R ][ j / R ] = 1;
            }

            ans = min( ans , checkGrid( R , C ) );
        }

        cout << "Case #" << _t << ": " << ans << endl;
    }

    return 0;
}
