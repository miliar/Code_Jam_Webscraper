#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;
double ay[(1<<16)+10] , an[(1<<16)+10];
int id[(1<<16)];
double yy[(1<<16)] , nn[(1<<16)];
double v[20];
int ck( int now )
{
    int rt = 0;
    while( now > 0 )
    {
        rt++;
        now -= ( now & (-now) );
    }
    return rt;
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int T , n , k;
    scanf( "%d" , &T );
    for( int cas = 1 ; cas <= T ; cas++ )
    {
        scanf( "%d %d" , &n , &k );
        for( int i=0 ; i<n ; i++ ) scanf( "%lf" , &v[i] );
        memset( ay , -1 , sizeof(ay) );
        ay[0] = 1.0; an[0] = 1.0;
        int p = 0;
        for( int i=0 ; i<(1<<n) ; i++ )
            if( ay[i] > -1e-8 )
            {
                int num = ck( i );
                //cout << i << " " << num << endl;
                if( num >= k / 2 )
                {
                    if( num == k / 2 )
                    {
                        id[p] = i;
                        yy[p] = ay[i];
                        nn[p++] = an[i];
                    }
                    continue;
                }
                for( int j=0 ; j<n ; j++ )
                    if( ( i & (1<<j) ) == 0 )
                    {
                        ay[(i+(1<<j))] = ay[i] * v[j];
                        an[(i+(1<<j))] = an[i] * ( 1.0 - v[j] );
                        //cout<< (i|(1<<j)) << " " << ay[(i|(1<<j))] << "+" << an[(i|(1<<j))] << endl;
                    }
            }
        double ans = 0.0;
        memset( ay , 0 , sizeof(ay) );
        for( int i=0 ; i<p ; i++ )
            for( int j=0 ; j<p ; j++ )
                if( ( id[i] & id[j] ) == 0 ) ay[ ( id[i] + id[j] ) ] += yy[i] * nn[j];
        for( int i=0 ; i<(1<<n) ; i++ ) ans = max( ay[i] , ans );
        printf( "Case #%d: %lf\n" , cas , ans );
        //printf( "Case #%d: %d\n" , cas , max( sum , mx ) );
    }
    return 0;
}
