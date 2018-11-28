#include <bits/stdc++.h>

#define Max      40000
#define Max2     100010
//#define mod      1000000007
#define Maxp     78499
#define pf       printf
#define sf       scanf
#define CLR(a)   memset(a,0,sizeof(a))
#define SET(a)   memset(a,-1,sizeof(a))
#define pb       push_back
#define fs       first
#define sc       second
#define TCASE    int T,t=1;scanf("%d",&T);while(T--)
#define loop(n)  for(int i=0;i<n;i++)
#define lop2(n)  for(int i=1;i<=n;i++)
#define lup(a)   for(int i=0;i<strlen(a);i++)
#define NL       pf("\n")
#define uplo     0b00100000
#define _        ios_base::sync_with_stdio(false); cin.tie(false);
#define check(a,b) a & (1 << b)

using namespace std;

typedef long long ll;
typedef unsigned long lu;
const double eps = 1e-9;
const double PI  = 3.1415926535897932384626433832795;
const int    inf = 0x7f7f7f7f;

int limit,pri;

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

bool miller_rabin(ll p, int it){
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

ll power(ll n,int p)
{
    ll ans = 1ll;
    for(int i=0;i<p;i++) ans*=n;
    return ans;
}

ll make_base(int mask,int base)
{
    ll num = 1ll + power(base,limit+1);
    for(int i=20;i>=0;i--)
    {
        if(check(mask,i)) num+=power(base,i+1);
    }
    return num;
}

map <int,vector<ll>> res;
map <int,vector<ll>>::iterator it2;

void chk(int mask)
{
    vector <ll> vct,vct2;
    for(int b=2;b<=10;b++)
    {
        ll num = make_base(mask,b);
        if(miller_rabin(num,30))  return;
        vct.pb(num);
    }
    int f = 0;
    for(int i=0;i<9;i++)
    {
        ll n = vct[i];
        for(ll j=2;j<=9999;j++)
        {
            if(j==n)  return;
            ll n1 = n,div=1ll;
            while(n1%j==0)
            {
                div*=j;
                n1/=j;
            }
            if(n1!=1ll && n!=n1)
            {
                vct2.pb(div);
                f++;
                break;
            }
        }
    }
    if(f==9)
    {
        for(int i=0;i<9;i++)
        {
            res[mask].pb(vct2[i]);
        }
        pri--;
    }
}

void prnt(int mask)
{
    pf("1");
    for(int i=limit-1;i>=0;i--)
    {
        if(check(mask,i)) pf("1");
        else              pf("0");
    }
    pf("1");
}

int main()
{
    freopen("C-small-attempt4.in","r",stdin);
    freopen("out.txt","w",stdout);
    TCASE
    {
        sf("%d %d",&limit,&pri);
        limit-=2;
        int lim = (1 << (limit)) - 1;
        for(int i=1;i<=lim;i++)
        {
            chk(i);
            if(!pri) break;
        }
        pf("Case #%d:\n",t++);
        if(!pri)
        {
            for(it2=res.begin();it2!=res.end();it2++)
            {
                int cur = it2->first;
                prnt(cur);
                for(int i=0;i<9;i++)  pf(" %lld",it2->second[i]);
                pf("\n");
            }
        }
    }
    return 0;
}
