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
    ll i, tst, n, cas = 0, cnt, l, j, k;
    string a, b ;
    scanf("%lld", &tst) ;
    getchar() ;
    while(tst--)
    {
        cnt = 0 ;
        getline(cin, a) ;
        l = a.size() ;
        for( i = l - 1; i >= 0; i-- )
        {
            if( a[i] == '-' )
            {
                b = "" ;
                k = 0 ;
                cnt++ ;
                if( a[k] == '+' )
                    cnt++ ;
                while( a[k] == '+' )
                    a[k] = '-', k++ ;
                for( j = i; j >= 0; j-- )
                {
                    if( a[j] == '+' )
                        a[j] = '-' ;
                    else
                        a[j] = '+' ;
                    b += a[j] ;
                }
                for( j = 0; j <= i; j++ )
                    a[j] = b[j] ;
//                cout << b << endl ;
            }
        }
        printf("Case #%lld: %lld\n", ++cas, cnt) ;
        b.clear() ;
    }
    return 0;
}
