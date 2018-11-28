#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define FILL(a,x) memset(a,x,sizeof(a))
#define foreach( gg,ii ) for( typeof(gg.begin()) ii=gg.begin();ii!=gg.end();ii++)
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define sz(a) int((a).size())
#define N 1000010
#define MAX 30
#define mod 1000000007
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define all(a) a.begin(),a.end()
const ll INF = 1e18+1;

inline ll input(void)
{
	char t;
	ll x=0;
	int neg=0;
	t=getchar();
	while((t<48 || t>57) && t!='-')
		t=getchar();
	if(t=='-')
		{neg=1; t=getchar();}
	while(t>=48 && t<=57)
	{
		x=(x<<3)+(x<<1)+t-48;
		t=getchar();
	}
	if (neg) x=-x;
	return x;
}

inline void output(ll x)
{
	char a[20];
	int i=0,j;
	a[0]='0';
	if (x<0) {putchar('-'); x=-x;}
	if (x==0) putchar('0');
	while(x)
	{
		a[i++]=x%10+48;
		x/=10;
	}
	for(j=i-1;j>=0;j--)
	{
		putchar(a[j]);
	}
	putchar(' ');
}

ll isprime(ll n)
{
	for(ll i=2;i*i<=n;i++)
		if (n%i==0) return i;
	return 1;
}

bool poss(ll n, ll size)
{
	int s[20];
	ll curr,x;
	vector <ll> v;
	REP(i,size)
	{
		s[size-i-1]=n%2;
		n/=2;
	}
	REPP(base,2,11)
	{
		curr=0;
		REP(i,size)
			curr=base*curr+s[i];
		v.pb(isprime(curr));
	}
	REP(i,sz(v)) if (v[i]==1) return 0;
	REP(i,size) putchar(s[i]+'0');
	putchar(' ');
	REP(i,sz(v)) output(v[i]);
	putchar('\n');
}

int main()
{
	ll t,n,j,curr,mask,offset,ans;
	t=input();
	char s[101];
	REP(kase,t)
	{
		n=input();
		j=input();
		ans=0;
		mask=1<<(n-2);
		offset=2*mask+1;
		printf("Case #%d:\n",kase+1);
		REP(i,mask)
		{
			curr=offset+2*i;
			if (poss(curr,n))
				ans++;
			if (ans==j) break;
		}
	}
return 0;
}
