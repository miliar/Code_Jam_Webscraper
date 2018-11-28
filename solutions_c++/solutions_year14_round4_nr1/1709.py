#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
const int MAXN = 10005;

int N , X , S[MAXN] , a[MAXN] ;

bool posible( int K )
{
    if ( 2 * K < N ) return false;

    for ( int i = 1 ; i <= K ; i++ )
        a[i] = S[i];

    int j = K;
    for ( int i = K + 1 ; i <= N ; i++ )
    {
        a[j] += S[i];
        j--;
    }

    for ( int i = 1 ; i <= K ; i++ )
        if ( a[i] > X ) return false;

    return true;

}

int main()
{
    freopen( "input.in" , "r" ,   stdin );
    freopen( "output.out", "w" , stdout );

    int T;
    cin >> T;
    for ( int t = 1 ; t <= T ; t++ )
    {
        cin >> N;
        cin >> X;

        for ( int i = 1 ; i <= N ; i++ )
            cin >> S[i];

        sort( S + 1 , S + N + 1 );

        for ( int i = 1 ; 2*i <= N ; i++ )
            swap( S[i] , S[N+1-i] );


        int l = 1 , r = N;

        while( r - l > 1 )
        {
            int mid = ( l + r ) / 2 ;
            if ( posible( mid ) ) r = mid ;
            else l = mid;
        }

        cout << "Case #" << t << ": " << r << endl;

    }

    return 0;
}
