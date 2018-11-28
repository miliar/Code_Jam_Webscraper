#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <vector>
using namespace std;
char c[110][110] , x[110];
int num[110][110];
bool check( int a , int p )
{
    int ln = strlen( c[a] ) , q = 0 , t = 0;
    if( ln > 0 ) t = 1;
    for( int i=1 ; i<ln ; i++ )
        if( c[a][i] != c[a][i-1] ) t++;
    if( t != p ) return 0;
    for( int i=0 ; i<ln ; i++ )
        if( c[a][i] == x[q] ) q++;
    if( q >= p ) return 1;
    else return 0;
}
int main()
{
    freopen("A-small-attempt1.in" , "r", stdin);
    freopen("out.txt", "w", stdout);
    int T , N;
    scanf( "%d" , &T );
    for( int cas=1 ; cas<=T ; cas++ )
    {
        scanf( "%d" , &N );
        for( int i=0 ; i<N ; i++ ) scanf( "%s" , c[i] );
        int ln = strlen( c[0] ) , p = 1;
        x[0] = c[0][0];
        for( int i=1 ; i<ln ; i++ )
        {
            if( c[0][i-1] != c[0][i] ) x[p++] = c[0][i];
        }
        bool q = 1;
        for( int i=1 ; i<N ; i++ )
        {
            if( !check( i , p ) )
            {
                q = 0; break;
            }
        }
        int ans = 0;
        if( q )
        {
            memset( num , 0 , sizeof(num) );
            for( int i=0 ; i<N ; i++ )
            {
                int k = 0 , lnn = strlen( c[i] );
                for( int j=0 ; j<lnn ; j++ )
                {
                    if( c[i][j] == x[k] ) num[i][k]++;
                    else
                    {
                        k++; j--;
                    }
                }
            }
            for( int i=0 ; i<p ; i++ )
            {
                int l = 100;
                for( int j=1 ; j<=100 ; j++ )
                {
                    int s = 0;
                    for( int k=0 ; k<N ; k++ ) s += abs( num[k][i] - j );
                    l = min( s , l );
                }
                ans += l;
            }
        }
        if( q ) printf( "Case #%d: %d\n" , cas , ans );
        else printf( "Case #%d: Fegla Won\n" , cas );
    }
    return 0;
}
