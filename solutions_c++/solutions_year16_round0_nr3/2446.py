#include <bits/stdc++.h>
#define ll long long int
#define ull unsigned long long int
#define s(a) scanf("%lld",&a)
#define pb push_back
#define mp make_pair
#define f first
#define sc second
#define inf 10e16

using namespace std;

vector<ll> prm;
void sieve()
{
    bitset<1000001>b;
    ll i,j;
    for(i=2;i<=1000000;i++) {
        if(b[i]==1) continue;
        prm.pb(i);
        for(j=i+i;j<=1000000;j+=i) b[j]=1;
    }
}

int arr[12] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};

ll mulmod(ll a, ll b, ll mod)
{
    ll x = 0,y = a % mod;
    while (b > 0) {
        if (b&1)
            x = (x + y) % mod;

        y = (y * 2) % mod;
        b /= 2;
    }
    return x;
}

ll bin(ll a, ll b, ll M)
{
    ll x = 1;
    ll y = a;

    while(b > 0) {
        if(b&1)
            x = mulmod(x, y, M);
        y = mulmod(y, y, M);

        b/= 2;
    }

    return x;
}

bool isprime(ll p)
{
    if (p < 2)
        return false;
    if (p != 2 && p % 2==0)
        return false;

    ll s = p - 1;
    while (s % 2 == 0)
        s /= 2;
    int i;
    for(i=0;i<12;i++) {
        ll a = arr[i] % (p - 1) + 1, temp = s;
        ll mod = bin(a, temp, p);

        while ((temp != p-1) && (mod != 1) && (mod != p-1)) {
            mod = mulmod(mod, mod, p);
            temp *= 2;
        }

        if (mod != p-1 && temp%2 == 0)
            return false;
    }
    return true;
}

ll factor(ll a)
{
    ll i;
    for(i=0;i<prm.size();i++) {
        if(a%prm[i]==0) return prm[i];
    }
    return 1;
}

ll valid(ll a)
{
    ll n=a;
    ll w,i,j;
    vector<ll>v,vv;
    while(a>0) {
        w=a%2;
        v.pb(w);
        a/=2;
    }
    for(i=2;i<=10;i++) {
        w = 0;
        ll mul = 1;
        for(j=0;j<v.size();j++) {
            w = w + mul * v[j];
            mul = mul * i;
        }
        if(isprime(w)) return 0;
        vv.pb(w);
    }
    for(i=v.size()-1;i>=0;i--) cout<<v[i];
    cout<<" ";
    for(i=0;i<vv.size();i++) cout<<factor(vv[i])<<" ";
    cout<<endl;
    return 1;
}

int main()
{
    sieve();
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,tt,n,i,j,k,l,w,ww,x,y,z;

    s(t);
    for(tt=1;tt<=t;tt++) {
        ll cnt=0;
        s(n);s(k);
        cout<<"Case #"<<tt<<":\n";
        w = pow(2,n-1)+1;
        ww = pow(2,n)-1;
        for(i=w;i<=ww;i+=2) {
            if(valid(i)) cnt++;
            if(cnt==k) break;
        }
    }
    return 0;
}
