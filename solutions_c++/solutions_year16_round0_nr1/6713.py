#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen( "A-large.in","r",stdin );
    freopen( "output.in","w",stdout );
    int t, T;
    long long n, total, p, num, z, c;
    bool checker[11];
    cin >> t;
    for( int T=1;T<=t;T++ ){
        p = 1;
        memset( checker,false,sizeof(checker) );
        cin >> n;
        if( n==0 ){
            printf( "Case #%d: INSOMNIA\n",T );
        }else{

            while( 1 ){
                c = 0;
                long long mod, div;
                num = n * p;
                z = num;
                while( z ){
                    mod = z % 10;
                    checker[mod] = true;
                    z = z / 10;
                }
                for( int i=0;i<10;i++ ){
                    if( checker[i] )c++;
                }
                if( c== 10 )break;
                p++;
            }
            printf( "Case #%d: %lld\n",T,num );
        }
    }
}
