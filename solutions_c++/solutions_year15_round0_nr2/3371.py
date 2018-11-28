/*
    Aleksandar "Al3kSaNdaR" Ivanović

    Problem B. Infinite House of Pancakes
*/
#include <bits/stdc++.h>

using namespace std;

int main ( void )
{
    freopen ( "B-large.in", "r", stdin );
    freopen ( "B-large.out", "w", stdout );

    int TestCases;
    scanf ( "%d", &TestCases );

    for ( int TestCase = 1; TestCase <= TestCases; TestCase++ )
    {
        int D, P[1 << 10];
        scanf ( "%d", &D );
        for ( int i = 0; i < D; i++ ) scanf ( "%d", &P[i] );

        int Solution = 1 << 30, k = * max_element ( P, P + D );
        while ( k > 0 )
        {
            int Current = k;
            for ( int i = 0; i < D; i++ ) Current += ( P[i] + k - 1 ) / k - 1;
            Solution = min ( Solution, Current );
            k--;
        }
        printf ( "Case #%d: %d\n", TestCase, Solution );
    }

    return 0;
}
