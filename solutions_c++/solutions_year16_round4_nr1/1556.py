#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;
int win[4100*4];
int wn( int a , int b )
{
    if( a + 1 == b ) return a;
    if( b + 1 == a ) return b;
    if( a + 2 == b ) return b;
    if( b + 2 == a ) return a;
}
int lef[4] , lt;
bool update( int rt )
{
    if( rt == 1 ) return true;
    if( rt / 2 * 2 != rt )
    {
        //cout << rt << " " << (rt-1) << endl;
        if( win[rt] == win[(rt-1)] ) return false;
        //cout << "++" << endl;
        win[rt/2] = wn( win[rt] , win[(rt-1)] );
        return update( rt / 2 );
    }
    else return true;
}
bool searchs( int now )
{
    if( now >= 2 * lt ) return true;
    for( int i=1 ; i<=3 ; i++ )
    {
        if( now % 2 == 0 && lef[i] > 0 )
        {
            win[now] = i;
            lef[i]--;
            if( searchs( now+1 ) ) return true;
            lef[i]++;
        }
        else if( now % 2 == 1 && lef[i] > 0 && win[now-1] != i )
        {
            win[now] = i;
            lef[i]--;
            if( update( now ) )
            {
                if( searchs( now+1 ) ) return true;
            }
            lef[i]++;
        }
    }
    return false;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T , n , R , P , S;
    scanf( "%d" , &T );
    for( int cas = 1 ; cas <= T ; cas++ )
    {
        scanf( "%d %d %d %d" , &n , &R , &P , &S );
        lt = ( 1 << n );
        lef[1] = P; lef[2] = R; lef[3] = S;
        printf( "Case #%d: " , cas );
        if( searchs( lt ) )
        {
            for( int i=lt ; i<lt*2 ; i++ )
            {
                if( win[i] == 1 ) printf( "P" );
                else if( win[i] == 2 ) printf( "R" );
                else if( win[i] == 3 ) printf( "S" );
            }
            puts( "" );
        }
        else puts( "IMPOSSIBLE" );
        //printf( "Case #%d: %d\n" , cas , max( sum , mx ) );
    }
    return 0;
}
