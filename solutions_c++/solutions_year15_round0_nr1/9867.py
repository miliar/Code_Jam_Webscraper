#include<bits/stdc++.h>
#define sl(n) scanf("%lld",&n);
#define sc(n) scanf(" %c",&n);
#define pl(n) printf("%lld",n);
#define pc(n) printf("%c",n);
#define pn printf("\n");
#define pt printf(" ");
#define forall(i,a,b) for(ll i=a;i<b;i++)
#define all(c) c.begin(), c.end()
#define tr(container, it) for(auto it = container.begin(); it != container.end(); it++)
#define bsearch(arr,ind) (int)(lower_bound(all(arr),ind)-arr.begin())
#define toDigit(c) (c-'0')
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define MOD 1000003
using namespace std;
typedef long long int ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;
ll power(ll a, ll p, ll mod)
{ll ret = 1;while(p){if(p&1)ret = (ret*a)%mod;a=(a*a)%mod;p/=2;}return ret;}
//modPow(ll a,ll b) {ll res=1;a%=MOD;for(;b;b>>=1){if(b&1)res=res*a%MOD;a=a*a%MOD;}return res;}
ll modInverse(ll a){return power(a,MOD-2,MOD);}
ll gcd (ll a, ll b){if (b == 0) {return a;}return gcd(b, a % b);}
ll nCk(ll n, ll k){if(k<0)return 0;
ll numerator = 1,il;
forall(il,0,k)numerator =(numerator*(n-il))%MOD;
ll denominator = 1;forall(il,1,k+1)denominator=(denominator*il)%MOD;
return (numerator*modInverse(denominator))%MOD;}


int main()
{   freopen("i1.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ll t,n,k,x,y,c;
    string s;
    sl(t);
    for(x=1;x<=t;x++)
    {c=0;
    k=0;
      sl(n);
      cin>>s;
        for(y=0;y<=n;y++)
        {
            if(c>=y && toDigit(s[y])!=0)
                c+=toDigit(s[y]);
            else
             {  if(toDigit(s[y])!=0)
                 {k+=y-c;
                 c+=(k+toDigit(s[y]));
                 }
             }
             //cout<<"Y="<<y<<" C= "<<c<<" k="<<k<<endl;
        }
        cout<<"Case #"<<x<<": "<<k;
        pn;
    }




    return 0;
}

