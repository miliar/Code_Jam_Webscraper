#include <bits/stdc++.h>

using namespace std;


#define Set(a, s) memset(a, s, sizeof (a))
#define rep(i, x, y) for(int i = x; i < y; i++)
#define Rep(i, x, y) for(int i = x; i <= y; i++)
#define vi vector<int>
#define vvi vector<vector<int> >
#define vp vector< pair< int, int > >
#define point pair<double, double >
#define pp push_back
#define mp make_pair
#define eps pow(10.0,-9.0)
#define MOD 1000000007
#define oo 1e18
#define Maxi 250000

#define prim 31
typedef unsigned long long ull;
typedef long long ll;

int n;

ull h[2002], pw[2002];
string s, st, en;

int k = (1<<10)-1;

int main()
{
    ios_base::sync_with_stdio(0);
    freopen("input.in","r", stdin);
    freopen("output.out","w", stdout);
    int t;
    scanf("%d", &t);
    rep(i,0,t)
    {
        ll n;
        scanf("%lld", &n);
        if(!n)
        {
            printf("Case #%d: INSOMNIA\n", i+1);
            continue;
        }
        int m = 0;
        ll p = 0;
        while( m != k )
        {
            p++;
            ll a = p*n;
            while(a)
            {
                int s = a%10;
                a /= 10;
                m |= (1<<s);
            }
        }
        n *= p;
        printf("Case #%d: %lld\n", i+1, n);
    }
    return 0;
}
