#include <bits/stdc++.h>

using namespace std ;

typedef long long ll ;
typedef unsigned long long llu ;
typedef unsigned int ui ;

//#define eps 1e-9
//#define pi acos(-1.0)
//#define INF 100000001
//#define MAX 10100
//int rr[]= {-1,-1,0,0,1,1};
//int cc[]= {-1,0,-1,1,0,1};
//int rr[]= {0,0,1,-1};/*4 side move*/
//int cc[]= {-1,1,0,0};/*4 side move*/
//int rr[]= {1,1,0,-1,-1,-1,0,1};/*8 side move*/
//int cc[]= {0,1,1,1,0,-1,-1,-1};/*8 side move*/
//int rr[]={1,1,2,2,-1,-1,-2,-2};/*night move*/
//int cc[]={2,-2,1,-1,2,-2,1,-1};/*night move*/

template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T sq(T x) { return x * x; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template < class T > T power(T N , T P) { return (P == 0) ?  1 : N * power(N , P - 1); }


int main()
{
//    freopen("in.txt", "r", stdin) ;
//    freopen("out.txt", "w", stdout) ;
    ll i, tst, n, cas = 0, ans, l, j, memo[10] ;
    scanf("%lld", &tst) ;
    while(tst--)
    {
        scanf("%lld", &n) ;
        if( n == 0 )
            printf("Case #1: INSOMNIA\n", ++cas) ;
        else
        {
            int fl = 0 ;
            memset(memo, 0, sizeof memo) ;
            for( i = 1; !fl ; i++ )
            {
                j = n * i ;
                while( j )
                {
                    memo[j % 10]++ ;
                    j /= 10 ;
                }
                for( j = 0; j <= 9; j++ )
                    if( !memo[j] )
                    {
                        fl = 1 ;
                        break ;
                    }
                if( fl )
                    fl = 0 ;
                else
                {
                    ans = n * i ;
                    break ;
                }
            }
            printf("Case #%lld: %lld\n", ++cas, ans) ;
        }
    }

    return 0;
}
