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
typedef unsigned long long ull;
typedef long long ll;

int gcd( int a, int b )
{
    return ( b == 0 ? a : gcd( b, a%b ));
}

ll poW( ll base, ll p )
{
    if( !p )
        return 1;

    ll ans = poW(base,p/2);
    ans = (ans*ans)%MOD;

    if(p%2)
        ans = (ans*base)%MOD;
    return ans;
}

ll a[100002];

int main()
{
    ios_base::sync_with_stdio(0);
    //freopen("input.in","r", stdin);
    //freopen("output.out","w", stdout);
    int t;
    cin>>t;
    rep(j, 1, t+1)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int cnt = 0, ans = 0;
        rep( i, 0, (int)s.size() )
        {
            if( i > cnt  )
            {
                ans += i - cnt;
                cnt = i;
            }

            cnt += s[i] - '0';
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }
    return 0;
}
