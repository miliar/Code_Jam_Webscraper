/*
    Aleksandar "Al3kSaNdaR" Ivanović

    Problem B. Lawnmower
*/
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <bitset>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <numeric>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <utility>
#include <functional>

#define pb push_back
#define sz size
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)

using namespace std;

typedef long long int lld;
typedef pair < int, int > pii;

const int MaxN = 1 << 8;
const int MaxM = 1 << 8;

int T, N, M, A[MaxN][MaxM];

inline string SolveSmall ( void )
{
    for ( int i = 0; i < N; i++ )
        for ( int j = 0; j < M; j++ ) if ( A[i][j] == 1 )
                                      {
                                          bool Ok1 = true, Ok2 = true;
                                          for ( int k = 0; k < M; k++ ) Ok1 &= A[i][k] == 1;
                                          for ( int k = 0; k < N; k++ ) Ok2 &= A[k][j] == 1;

                                          if ( ! Ok1 && ! Ok2 ) return "NO";
                                      }
    return "YES";
}

inline string SolveLarge ( void )
{
    for ( int i = 0; i < N; i++ )
        for ( int j = 0; j < M; j++ )
        {
            bool Ok1 = true, Ok2 = true;
            for ( int k = 0; k < M; k++ ) Ok1 &= A[i][k] <= A[i][j];
            for ( int k = 0; k < N; k++ ) Ok2 &= A[k][j] <= A[i][j];

            if ( ! Ok1 && ! Ok2 ) return "NO";
        }

    return "YES";
}

int main ( void )
{
    //freopen ( "B-small-attempt1.in", "r", stdin );
    //freopen ( "B-small-attempt1.out", "w", stdout );
    freopen ( "B-large.in", "r", stdin );
    freopen ( "B-large.out", "w", stdout );

    cin.sync_with_stdio ( 0 );
    cout.sync_with_stdio ( 0 );

    cin >> T;
    for ( int __T = 1; __T <= T; __T++ )
    {
        cin >> N >> M;
        for ( int i = 0; i < N; i++ )
            for ( int j = 0; j < M; j++ ) cin >> A[i][j];

        cout << "Case #" << __T << ": " << SolveLarge ( ) << endl;
    }

    return 0;
}
