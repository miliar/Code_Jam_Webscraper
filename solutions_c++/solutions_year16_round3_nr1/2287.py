#include <bits/stdc++.h>

using namespace std;


#define Set(a, s) memset(a, s, sizeof (a))
#define rep(i, x, y) for(int i = x; i < y; i++)
#define Rep(i, x, y) for(int i = x; i <= y; i++)
#define vi vector<int>
#define vvi vector<vector<int> >
#define vp vector< pair< int, int > >
#define point pair<double, double >
#define pb push_back
#define mp make_pair
#define eps pow(10.0,-9.0)
#define MOD 1000000007
#define oo 1e18
#define Maxi 250000
#define PI  3.14159265358979323846
#define prim 31
typedef unsigned long long ull;
typedef long long ll;

bool prime[10000002];
vector<ll> primes;

void sieve(ll num)
{
    Set( prime, true );
    prime[ 0 ] = prime[ 1 ] = 0;
    ll i=4;
    primes.pb(2);
    while ( i <= num )
    {
        prime[i]=false;
        i+=2;
    }
    for ( i=3 ; i<=num ; i+=2 )
    {
        if ( prime[i] )
        {
            primes.pb(i);
            for ( ll  j=i*i ; j<=num ; j+=i )
                prime[j]=false;
        }
    }

}

ll solve(ll n)
{
    rep( i, 0, (int)primes.size())
    {
        if( primes[i]*primes[i] > n)
            break;
        ll a = primes[i]*primes[i];
        n -= n/a;
    }
    return n;
}

double len(int a, int b, int x, int y)
{
    return sqrt(((a-x)*(a-x))+((b-y)*(b-y)));
}
double lenFromLine(int a, int b, int c, int d, int x, int y)
{
    return fabsl( x*(d-b) -(c-a)*y - a*d + b*c )/len(a, b, c, d);
}
double cirArea( double r)
{

    return r*r*PI;
}

int a[30];
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("input.in","r", stdin);
    freopen("output.out","w", stdout);
    int t;
    cin>>t;
    rep( T, 1, t+1)
    {
        int n, cnt =0;
        cin>>n;
        priority_queue< pair<int,int> > Q;
        rep(i, 0, n)
        {
            pair<int,int> p;
            cin>>p.first;
            cnt += p.first;
            p.second = i;
            Q.push(p);
        }
        cout<<"Case #"<<T<<":";
        pair<int,int> k = Q.top();
        while( k.first > 0 )
        {
            string s="";
            if(cnt%2)
            {
                pair<int,int> p = Q.top();
                Q.pop();
                p.first--;
                s += char('A' +p.second);
                Q.push(p);
                cnt--;
                cout<<" "<<s;
                continue;
            }

            rep(j,0,2)
            {
                pair<int,int> p = Q.top();
                Q.pop();
                p.first--;
                s += char('A' +p.second);
                Q.push(p);
            }
            cout<<" "<<s;
            k = Q.top();
        }
        cout<<endl;
    }

    return 0;
}
