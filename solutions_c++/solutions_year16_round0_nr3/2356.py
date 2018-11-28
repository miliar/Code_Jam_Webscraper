#include<bits/stdc++.h>
using namespace std;
#define rep(i,x,y) for(i=x;i<=y;i++)
#define _rep(i,x,y) for(i=x;i>=y;i--)
#define CL(S,x) memset(S,x,sizeof(S))
#define CP(S1,S2) memcpy(S1,S2,sizeof(S2))
#define ALL(x,S) for(x=S.begin();x!=S.end();x++)
#define sqr(x) ((x)*(x))
#define mp make_pair
#define fi first
#define se second
#define upmin(x,y) x=min(x,y)
#define upmax(x,y) x=max(x,y)

typedef long long ll;
typedef long double ld;
int T,n,m,i,j,k,l,p;
int z[1111];

map<ll,int> S;map<ll,int>::iterator pos;
const int MAXP=1000000,mod=int(1e9)+7;bool pd[MAXP+1];
ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}
ll mul(ll a,ll b,ll mod){return (a*b-ll(a/ld(mod)*b+1e-3)*mod+mod)%mod;}
ll pow(ll a,ll b,ll mod){ll ans=1;a%=mod;for(;b;b>>=1,a=mul(a,a,mod))if(b&1)ans=mul(ans,a,mod);return ans;}
ll pow(ll a,ll b){ll ans=1;a%=mod;for(;b;b>>=1,a=a*a%mod)if(b&1)ans=ans*a%mod;return ans;}
bool MR(ll n,int k)
{
    ll s=n-1;int w=0;
    for(;!(s&1);s>>=1)w++;
    ll y=pow(k,s,n);
    if(y==1||y==n-1)return 1;
    while(w--){y=mul(y,y,n);if(y==n-1)return 1;}
    return 0;
}
bool pdp(ll n)
{
    if(n<=MAXP)return !pd[n];
    return MR(n,2)&&MR(n,3)&&MR(n,5)&&MR(n,7)&&MR(n,11)&&MR(n,13)&&MR(n,17)&&MR(n,19)&&MR(n,23);
}
void rho(ll n,ll&z)
{
    ll x,y,d,p;
    while(1)
    {
        x=2;y=2;d=1;p=mul(rand(),rand(),10000000);
        while(d==1)
        {
            x=(mul(x,x,n)+p)%n;
            y=(mul(y,y,n)+p)%n;
            y=(mul(y,y,n)+p)%n;
            d=gcd(abs(x-y),n);
        }
        if(d==n||d==0)continue;
        z=d;break;
    }
}


void pre()
{
    int i,j;
    pd[1]=1;
    rep(i,2,MAXP)if(!pd[i])
    rep(j,2,MAXP/i)pd[i*j]=1;
}

ll ans[11];
set<string> s;string ss;

int main()
{
	//freopen("1.in","r",stdin);
		freopen("1.out","w",stdout);
	
	printf("Case #1:\n");
	
	pre();
	
	n=16;
	for(int gg=50;gg;gg--)	
	{
		while(1)
		{
			z[1]=1;for(int i=2;i<=n-1;i++)z[i]=rand()&1;z[n]=1;
			ss="";for(int i=1;i<=n;i++)ss=ss+char(z[i]);
			if(s.find(ss)!=s.end())continue;s.insert(ss);
			bool ok=1;
			for(int bb=2;bb<=10;bb++)
			{	
				ll v=0;for(int i=1;i<=n;i++)v=v*bb+z[i];
				if(pdp(v)){
					ok=0;break;
				}
				else rho(v,ans[bb]);
			}
			if(ok)
			{
				for(int i=1;i<=n;i++)cout<<z[i];
				for(int i=2;i<=10;i++)cout<<" "<<ans[i];cout<<endl;
				break;
			}
		}
	}
	
	return 0;
}
