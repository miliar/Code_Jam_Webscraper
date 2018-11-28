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


vector < ll > all, ans ;

ll mulmod(ll a, ll b, ll c){
	ll x = 0,y = a%c;

	while(b>0){
		if(b&1) x = (x+y)%c;
		y = (y<<1)%c;
		b >>= 1;
	}

	return x;
}

ll pow(ll a, ll b, ll c){
	ll x = 1, y = a;

	while(b>0){
		if(b&1) x = mulmod(x,y,c);
		y = mulmod(y,y,c);
		b >>= 1;
	}

	return x;
}

bool miller_rabin(ll p, ll it)
{
	if(p<2) return false;
	if(p==2) return true;
	if((p&1)==0) return false;

	ll s = p-1;
	while(s%2==0) s >>= 1;

	while(it--){
		ll a = rand()%(p-1)+1,temp = s;
		ll mod = pow(a,temp,p);

		if(mod==-1 || mod==1) continue;

		while(temp!=p-1 && mod!=p-1){
			mod = mulmod(mod,mod,p);
			temp <<= 1;
		}

		if(mod!=p-1) return false;
	}

	return true;
}


void pre_generate(ll prnt)
{
    ll i, fl, num, j = 32769 * 2, chk, a[16], l, k, m, cnt = 0 ;
    for(i = 32769; i <= j; i += 2 )
    {
        chk = i, k = 0 ;
        while( chk )
        {
            a[k++] = chk % 2 ;
            chk /= 2 ;
        }
        reverse(a, a + k) ;
        if( a[0] == 1 && a[k - 1] == 1 )
        {
            chk = k ;
            fl = 0, l = chk - 1 ;
            num = 0 ;
            all.clear() ;
            for( m = 2; m <= 10; m++ )
            {
                num = 0 ;
                l = chk - 1 ;
                for( k = 0; k < chk; k++ )
                {
                    num = num + ( a[k] * power(m, l) ) ;
                    l-- ;
                }
                all.push_back(num) ;
                if( miller_rabin(num, 30) )
                {
                    fl = 1 ;
                    all.clear() ;
                    break ;
                }
            }
            if( !fl )
            {
                cnt++ ;
                ans.clear() ;
                for( k = 0; k < 10; k++ )
                {
                    chk = sqrt(all[k]) ;
                    for( m = 2; m <= chk; m++ )
                    {
                        if( all[k] % m == 0 )
                        {
                            ans.push_back(m) ;
                            break ;
                        }
                    }
                }
                for( k = 0; k < 16; k++ )
                    printf("%lld", a[k]) ;
                for( k = 0; k < 9; k++ )
                    printf(" %lld", ans[k]) ;
                puts("") ;
            }
        }
        if( cnt >= prnt )
            break ;
    }
}

int main()
{
//    freopen("in.txt", "r", stdin) ;
//    freopen("out.txt", "w", stdout) ;
//    pre_generate() ;
    ll i, tst, n, cas = 0, cnt, l, j, k;
    scanf("%lld", &tst) ;
    getchar() ;
    while(tst--)
    {
        scanf("%lld %lld", &n, &j) ;
        printf("Case #%lld:\n", ++cas) ;
        if( n == 16 )
        {
            pre_generate(j) ;
        }
        else
        {

        }
    }
    return 0;
}
