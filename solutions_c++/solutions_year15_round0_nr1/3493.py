/*
    Aleksandar "Al3kSaNdaR" Ivanović

    Problem A. Standing Ovation
*/
#include <bits/stdc++.h>

using namespace std;

int main ( void )
{
    freopen ( "A-large.in", "r", stdin );
    freopen ( "A-large.in.out", "w", stdout );

    int TestCases;
    scanf ( "%d", &TestCases );

    for ( int TestCase = 1; TestCase <= TestCases; TestCase++ )
    {
        int N;
        char Buffer[1 << 10];

        scanf ( "%d %s", &N, Buffer );

        int Solution = 0, Total = 0;
        for ( int i = 0; i < N + 1; i++ )
        {
            if ( Buffer[i] != '0' && Total < i )
            {
                Solution += i - Total;
                Total += i - Total;
            }
            Total += Buffer[i] - '0';
        }

        printf ( "Case #%d: %d\n", TestCase, Solution );
    }

    return 0;
}
