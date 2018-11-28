#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <vector>
using namespace std;
int main()
{
    freopen("B-small-attempt0.in" , "r", stdin);
    freopen("out.txt", "w", stdout);
    int T , a , b , k;
    scanf( "%d" , &T );
    for( int cas=1 ; cas<=T ; cas++ )
    {
        scanf( "%d %d %d" , &a , &b , &k );
        int ans = 0;
        for( int i=0 ; i<a ; i++ )
        {
            for( int j=0 ; j<b ; j++ )
                if( ( i & j ) < k ) ans++;
        }
        printf( "Case #%d: %d\n" , cas , ans );
    }
    return 0;
}
