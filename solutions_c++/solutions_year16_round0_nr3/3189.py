#include <bits/stdc++.h>

using namespace std;

int t ;
long long n , J, x ;
long long is_p()
{
    for ( long long i = 2 ; i*i <= x ; i++ )
        if ( x%i == 0 )
            return i ;
    return 0 ;
}
int main()
{
    //freopen("A-large.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    scanf("%d",&t) ;
    long long a ;
    for ( int c = 1 ; c <= t ; c++ )
    {
        long long ans[11] ;
        scanf("%d%d",&n,&J) ;
        printf("Case #%d:\n",c) ;
        int lol = 0 ;
        bool kk ;
        for ( int i = 0 ; i < ( 1<< n ) ; i++ )
        {
            kk = 1 ;
            if ( !(i&1) || !(i&(1<<(n-1)) ))continue ;
            if ( lol == J ) break;
            string s ;
            for ( int k = 0 ; k < n ; k++ )
                s += bool((1<<k)&i) + '0' ;
            for ( int j = 2 ; j <= 10 ; j++ )
            {
                x = 0 , a = 1 ;
                for ( int k = 0 ; k < n ; k++ )
                    x += a*bool(i&(1<<k)) , a *= j ;
                ans[j] = is_p() ;
            }
            for (int j = 2 ; j <= 10 ; j++ )
                if ( !ans[j] )
                    kk = 0 ;
            if ( !kk ) continue ;
            reverse(s.begin(),s.end()) ;
            cout << s << " " ;
            for ( int j = 2 ; j <= 10 ; j++ )
                printf("%d ",ans[j]) ;
            puts("") ;
            lol++ ;
        }
    }
    return 0;
}
