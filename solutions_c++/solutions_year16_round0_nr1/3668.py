#include <bits/stdc++.h>

using namespace std;

int t ;
long long n , tmp , tmp2 ;

int main()
{
    freopen("A-large.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    scanf("%d",&t) ;
    for ( int c = 1 ; c <= t ; c++ )
    {
        scanf("%lld",&n) ;
        if ( n == 0 )
        {
            printf("Case #%d: INSOMNIA\n",c) ;
            continue ;
        }
        bool vis[10] = {} , k ;
        int ctr = 0 ;
        tmp2 = n ;
        while ( true )
        {
            ctr++ ;
            tmp = n ;
            k = 1 ;
            while ( tmp )
            {
                vis[tmp%10] = 1 ;
                tmp /= 10 ;
            }
            for ( int i = 0 ; i < 10 ; i++ )
                if ( !vis[i] ) k = 0 ;
            if ( k )
            {
                printf("Case #%d: %lld\n",c,n) ;
                break;
            }
            if ( ctr > 10000 )
            {
                printf("Case #%d: INSOMNIA\n",c) ;
                break;
            }
            n += tmp2 ;
        }
    }
    return 0;
}
