/* Have courage and be kind*/
#include<bits/stdc++.h>
#include<stdlib.h>
#include <assert.h>  //assert ( n >= 1 && n < 100005 );
using namespace std;
#define inf 2147383647LL
#define SET(a) memset(a,-1,sizeof(a))
#define all(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define sz(x) ((int)x.size())
#define PB push_back
#define MP make_pair
#define pii pair<int,int>
#define FOR0(i,n) for(int i = 0;i<n;i++)
#define FOR1(i,n) for(int i = 1;i<=n;i++)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define PI acos(-1.0)
#define EPS 1e-9
#define UNIQUE(V) (V).erase(unique((V).begin(),(V).end()),(V).end())//vector must be sorted
#define NUMDIGIT(x,y) (((int)(log10((x))/log10((y))))+1)
#define LCM(x,y) (((x)/gcd((x),(y)))*(y))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define lol long long
#define ulol unsigned long long
#define pf printf
#define sf scanf
#define mod 1000000007 //10^9+7
#define pause system("pause")
#define F first
#define S second
#define phl printf ( "hello\n" )
#define POPCOUNT __builtin_popcountll
#define RIGHTMOST __builtin_ctzll
#define LEFTMOST(x) (63-__builtin_clzll((x)))

lol mod_v(lol num)
{
    if(num>=0)
      return(num%mod);
    else
     return(num%mod+mod)%mod;
}

lol bigmod ( lol b, lol p, lol m ) {  //Repeated Squaring Method for Modular Exponentiation
    lol res = 1 % m, x = b % m;
    while ( p ) {
        if ( p & 1 ) res = ( res * x ) % m;
        x = ( x * x ) % m;
        p >>= 1;
    }
    return res;
}

/********** Solution ***************/
bool arr[10];

int main()
{

    READ("A-large.in");
    WRITE("output.txt");

    int test, cnt;
    lol n, m, ans, r, i;

    sf("%d", &test);
    FOR1(t, test)
    {
        sf("%lld", &n);

        if(n == 0)
            pf("Case #%d: INSOMNIA\n", t);
        else
        {
            CLR(arr);
            i = 0;
            cnt = 0;

            while(1)
            {
                i++;
                m = n*i;
                while(m)
                {
                    r = m%10;
                    m=m/10;

                    if(arr[r] == 0)
                    {
                        arr[r] = 1;
                        cnt++;
                    }
                }

                if(cnt == 10)
                {
                    ans = n*i;
                    break;
                }
            }

            pf("Case #%d: %lld\n", t, ans);
        }
    }

    return 0;
}

