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

LL bigmod(LL b,LL p)
{
    if(p == 0)return 1;
    LL my = bigmod(b,p/2);
    my*=my;
    if(p & 1)my*=b;
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

LL lol[100],ara[100],tot,n,K;
LL wut[] = {2,3,11};
bool fuck(LL b)
{
	LL x = 0,i;
	rep(i,n)
	{
		x *= b;
		x += ara[i];
	}
	for(i=0;i<3;i++)
	{
		if(x % wut[i] == 0)
		{
			lol[b] = wut[i];
			return 1;
		}
	}
	//puts("no");
	return 0;
}

void go()
{
	LL i;
	for(i=2;i<=10;i++)
	{
		bool my = fuck(i);
		if(my == 0)return;
	}
	rep(i,n)printf("%lld",ara[i]);
	for(i=2;i<=10;i++)printf(" %lld",lol[i]);
	NL;
	tot++;
}

void fun(LL pos,LL sum)
{
	if(tot == K)return;
	if(pos == n)
	{
		ara[pos] = 1;
		sum++;
		if(sum % 2 == 0)go();
		return;
	}
	ara[pos] = 0;
	fun(pos+1,sum);
	ara[pos] = 1;
	fun(pos+1,sum+1);
}

void dick(LL pos,LL sum,LL t11,LL t12,LL t21,LL t22,LL t31,LL t32,LL t41,LL t42,LL t51,LL t52)
{
	if(tot == K)return;
	if(pos > n)
	{
		if(sum & 1)return;

		LL boobs[12];
		mem(boobs,-1);

		if(t11 == 0)boobs[2] = 3;
		if(t12 == 0)boobs[2] = 11;

		if(t21 == 0)boobs[4] = 3;
		if(t22 == 0)boobs[4] = 11;

		if(t31 == 0)boobs[6] = 3;
		if(t32 == 0)boobs[6] = 11;

		if(t41 == 0)boobs[8] = 3;
		if(t42 == 0)boobs[8] = 11;

		if(t51 == 0)boobs[10] = 3;
		if(t52 == 0)boobs[10] = 11;

		LL i;
		for(i=2;i<=10;i+=2)
		{
			if(boobs[i] == -1)return;
		}
		rep(i,n)printf("%lld",ara[i]);
		for(i=2;i<=10;i++)
		{
			if(i & 1)printf(" 2");
			else printf(" %lld",boobs[i]);
		}
		NL;
		tot++;
		return;
	}

	if(pos < n)
	{
		ara[pos] = 0;
		dick(pos+1,sum, (t11*2)%3,(t12*2)%11, (t21*4)%3,(t22*4)%11, (t31*6)%3,(t32*6)%11, (t41*8)%3,(t42*8)%11, (t51*10)%3,(t52*10)%11);
	}
	ara[pos] = 1;
	dick(pos+1,sum+1, (t11*2+1)%3,(t12*2+1)%11, (t21*4+1)%3,(t22*4+1)%11, (t31*6+1)%3,(t32*6+1)%11, (t41*8+1)%3,(t42*8+1)%11, (t51*10+1)%3,(t52*10+1)%11);
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("outClarge.txt","w",stdout);
	LL t,T;
	sl(T);
	rep(t,T)
	{
		ara[1] = 1;
		sll(n,K);
		tot = 0;
		printf("Case #%lld:\n",t);
		//fun(2,1);
		dick(2,1,1,1,1,1,1,1,1,1,1,1);
	}
	return 0;
}
