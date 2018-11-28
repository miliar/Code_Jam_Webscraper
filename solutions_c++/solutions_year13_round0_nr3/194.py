/*
    Aleksandar "Al3kSaNdaR" Ivanović

    Problem C. Fair and Square
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
#define all(X) (X).begin(), (X).end ()
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)

using namespace std;

typedef long long int lld;
typedef pair < int, int > pii;

inline bool Palindrome ( lld Number )
{
    lld Reverse = 0LL, __Number = Number;
    while ( __Number )
    {
        Reverse = Reverse * 10LL + __Number % 10LL;
        __Number /= 10LL;
    }

    return Number == Reverse;
}

int T;
lld A, B;
vector < lld > FairSquares;

inline void SolveSmall ( void )
{
    for ( lld i = 1LL; i <= 10000000LL; i++ ) if ( Palindrome ( i ) && ( Palindrome ( i * i ) ) ) FairSquares.pb ( i * i );

    cin >> T;
    for ( int __T = 1; __T <= T; __T++ )
    {
        cin >> A >> B;
        cout << "Case #" << __T << ": " << upper_bound ( all ( FairSquares ), B ) - lower_bound ( all ( FairSquares ), A ) << endl;
    }
}

const int MaxN = 1 << 8;

typedef struct Number
{
    int N, Digits[MaxN];
    Number ( ) { N = 1, memset ( Digits, 0, sizeof ( Digits ) ); }

    Number ( lld __Number )
    {
        memset ( Digits, 0, sizeof ( Digits ) );
        if ( ! __Number ) N = 1;
        else
        {
            N = 0;
            while ( __Number )
            {
                Digits[N++] = __Number % 10LL;
                __Number /= 10LL;
            }
        }
    }

    Number ( string S )
    {
        memset ( Digits, 0, sizeof ( Digits ) );
        N = S.length ( );
        for ( int i = 0; i < N; i++ ) Digits[i] = S[N - i - 1] - '0';
    }

    inline void Print ( void )
    {
        for ( int i = N - 1; i >= 0; i-- ) cout << Digits[i];
    }

    inline bool operator < ( const Number &NewNumber ) const
    {
        if ( N != NewNumber.N ) return N < NewNumber.N;
        else
        {
            for ( int i = N - 1; i >= 0; i-- ) if ( Digits[i] != NewNumber.Digits[i] ) return Digits[i] < NewNumber.Digits[i];
            return false;
        }
    }
};

inline Number Multiply ( const Number &A, const Number &B )
{
    Number Ret;
    Ret.N = A.N + B.N;

    for ( int i = 0; i < A.N; i++ )
    {
        int Carry = 0;
        for ( int j = 0; j < B.N; j++ )
        {
            int Curr = Ret.Digits[i + j] + A.Digits[i] * B.Digits[j] + Carry;
            Ret.Digits[i + j] = Curr % 10;
            Carry = Curr / 10;
        }
        Ret.Digits[i + B.N] = Carry;
    }

    while ( ( Ret.N > 1 ) && ( ! Ret.Digits[Ret.N - 1] ) ) Ret.N--;
    return Ret;
}

set < Number > Numbers;
vector < Number > FairSquaresLARGE;

string StrA, StrB;

bool Palindrome ( Number A )
{
    for ( int i = 0; i < A.N; i++ ) if ( A.Digits[i] != A.Digits[A.N - i -1] ) return false;
    return true;
}

int SQSum;
Number Curr;
void DFS ( int idx )
{
    if ( 2 * idx > Curr.N )
    {
        Number Square = Multiply ( Curr, Curr );
        if ( Palindrome ( Square ) ) Numbers.insert ( Square );
        return;
    }

    for ( int i = 0; i <= 3; i++ ) if ( SQSum + 2 * i * i < 10 )
                                  {
                                      Curr.Digits[idx] = Curr.Digits[Curr.N - idx - 1] = i;
                                      SQSum += 2 * i * i;
                                      DFS ( idx + 1 );
                                      SQSum -= 2 * i * i;
                                      Curr.Digits[idx] = 0;
                                  }

    if ( 2 * idx + 1 == Curr.N )
    {
        for ( int i = 0; i <= 3; i++ ) if ( SQSum + i * i < 10 )
                                      {
                                          Curr.Digits[idx] = Curr.Digits[Curr.N - idx - 1] = i;
                                          SQSum += i * i;
                                          DFS ( idx + 1 );
                                          SQSum -= i * i;
                                          Curr.Digits[idx] = 0;
                                      }
    }
}

inline void SolveLarge ( void )
{
    for ( int i = 1; i <= 51; i++ )
    {
        SQSum = 0;
        Curr.N = i;
        memset ( Curr.Digits, 0, sizeof ( Curr.Digits ) );
        DFS ( 0 );
    }

    for_each ( it, Numbers ) FairSquaresLARGE.pb ( * it );

    cin >> T;
    for ( int __T = 1; __T <= T; __T++ )
    {
        cin >> StrA >> StrB;
        Number A = Number ( StrA ), B = Number ( StrB );
        cout << "Case #" << __T << ": " << upper_bound ( all ( FairSquaresLARGE ), B ) - lower_bound ( all ( FairSquaresLARGE ), A ) << endl;
    }
}

int main ( void )
{
    //freopen ( "C-small-attempt0.in", "r", stdin );
    //freopen ( "C-small-attempt0.out", "w", stdout );
    //freopen ( "C-large-1.in", "r", stdin );
    //freopen ( "C-large-1.out", "w", stdout );
    freopen ( "C-large-2.in", "r", stdin );
    freopen ( "C-large-2.out", "w", stdout );

    cin.sync_with_stdio ( 0 );
    cout.sync_with_stdio ( 0 );

    SolveLarge ( );

    return 0;
}
