#include <bits/stdc++.h>

#define rep(i,n) for(i=1;i<=n;i++)
#define Rep(i,n) for(i=0;i<n;i++)
#define For(i,a,b) for(i=a;i<=b;i++)

#define pb(x) push_back(x)
#define sz(x) x.size()

#define mem(ara,val) memset(ara,val,sizeof(ara))
#define eps 1e-3

#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define siii(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define slll(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)
#define ss(ch) scanf("%s",ch)
#define pi(x) printf("%d",x)
#define pii(x,y) printf("%d %d",x,y)
#define piii(x,y,z) printf("%d %d %d",x,y,z)
#define pl(x) printf("%lld",x)
#define pll(x,y) printf("%lld %lld",x,y)
#define plll(x,y,z) printf("%lld %lld %lld",x,y,z)
#define ps(ch) printf("%s",ch)
#define Afridi 0
#define NL printf("\n")
#define debug(x) printf("wow  %d !!\n",x)
#define Max 100005
#define INF INT_MAX
#define PI 3.141592653589793
#define FI freopen("in.txt","r",stdin)
#define FO freopen("out.txt","w",stdout)
#define mod 1000000007
#define FO freopen("out.txt","w",stdout)

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

LL bigmod(LL b,LL p,LL m)
{
    if(p == 0)return 1;
    LL my = bigmod(b,p/2,m);
    my*=my;
    my%=m;
    if(p & 1)my*=b,my%=m;
    return my;
}
int setb(int n,int pos)
{
    return n=n | (1 << pos);
}
int resb(int n,int pos)
{
    return n=n & ~(1 << pos);
}
bool checkb(int n,int pos)
{
    return (bool)(n & (1 << pos));
}

bool taken[10];

bool oka()
{
	LL i;
	Rep(i,10)if(taken[i] == 0)return 0;
	return 1;
}

void fuck(LL x)
{
	while(x)
	{
		LL my = x % 10;
		x /= 10;
		taken[my] = 1;
	}
}

LL fun(LL x)
{
	mem(taken,0);
	LL cur = x;
	while(1)
	{
		fuck(cur);
		if( oka() )return cur;
		cur += x;
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outAlarge.txt","w",stdout);

	LL t,T,n;
	sl(T);
	rep(t,T)
	{
		sl(n);
		printf("Case #%lld: ",t);
		if(n == 0)puts("INSOMNIA");
		else printf("%lld\n",fun(n));
	}

	return 0;
}
