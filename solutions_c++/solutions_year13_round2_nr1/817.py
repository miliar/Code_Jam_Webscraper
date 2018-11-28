/*
    Aleksandar "Al3kSaNdaR" Ivanović

    Problem A. Osmos
*/
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int MaxN = 1 << 8;

int T, A, N, Motes[MaxN];

int main ( void )
{
    //freopen ( "A-small-attempt0.in", "r", stdin );
    //freopen ( "A-small-attempt0.out", "w", stdout );
    freopen ( "A-large.in", "r", stdin );
    freopen ( "A-large.out", "w", stdout );

    cin.sync_with_stdio ( 0 );
    cout.sync_with_stdio ( 0 );

    cin >> T;
    for ( int __T = 1; __T <= T; __T++ )
    {
        cin >> A >> N;
        for ( int i = 0; i < N; i++ ) cin >> Motes[i];
        sort ( Motes, Motes + N );

        int L = 0, R = N, Sol = N;
        while ( L <= R )
        {
            int M = ( L + R ) >> 1;
            bool Can = false;

            for ( int Cnt1 = 0; Cnt1 <= M; Cnt1++ )
            {
                int Cnt2 = M - Cnt1, Size = N - Cnt2;
                int CurrA = A, CntTaken = 0;
                bool CurrCan = true;

                for ( int i = 0; i < Size; i++ )
                {
                    if ( Motes[i] < CurrA ) CurrA += Motes[i];
                    else
                    {
                        CurrA += CurrA - 1;
                        CntTaken++;
                        if ( CntTaken > Cnt1 )
                        {
                            CurrCan = false;
                            break;
                        }
                        i--;
                    }
                }

                if ( CurrCan )
                {
                    Can = true;
                    break;
                }
            }

            if ( Can )
            {
                Sol = M;
                R = M - 1;
            }
            else L = M + 1;
        }

        cout << "Case #" << __T << ": " << Sol << endl;
    }

    return 0;
}
