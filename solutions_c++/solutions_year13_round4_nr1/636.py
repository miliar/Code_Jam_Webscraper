#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
#include<cstdlib>
#include<functional>
#include<iostream>
#include<map>
#include<bitset>
#define fo(i,a,b) for(i=a;i<=b;i++)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define MP(a,b) make_pair(a,b)
#define clr(x,y) memset(x,y,sizeof x)
#define fi first
#define se second
#define LL long long
#define sqr(z) ((z)*(z))
using namespace std;
typedef pair<int,int> PII;
const LL oo=1047483647,maxn=2010;
const LL Mod=1000002013LL;
LL n,i,j,k,m,q,ge[maxn],ans,cost,T,tot;
struct node
{
	LL x,y,s;
}a[maxn];
PII P[maxn];
LL Read()
{
	char ch;while (ch = getchar(), (ch < '0' || ch > '9') && (ch != '-')); 
	bool neg= (ch == '-');
	if (ch=='-') ch=getchar();
	LL v=0;
	while (ch>='0' && ch<='9') v=v*10+ch-'0',ch=getchar();
	if (neg) v=-v;
	return v;
}
int main()
{
	freopen("1.in","r",stdin);
  freopen("1.out","w",stdout);
	T=Read();
	int ca=0;
	for(;T;T--)
	{
		++ca;
		n=Read();
		m=Read();
		cost=0;ans=0;
		memset(ge,0,sizeof ge);
		tot=0;
		fo(i,1,m)
		{
			a[i].x=Read();
			a[i].y=Read();
			a[i].s=Read();
			P[++tot]=MP(a[i].x,-i);
			P[++tot]=MP(a[i].y,i);
			LL w=a[i].y-a[i].x;
			cost=(cost+(w*(n+1)-w*(w+1)/2)%Mod*a[i].s%Mod)%Mod;
		}
		sort(P+1,P+tot+1);
		P[0]=MP(-oo,0);
		LL now=0;
		fo(i,1,tot)
		{
			if (P[i].fi!=P[i-1].fi) P[++now]=P[i];
			if (P[i].se<0)
			{
				LL t=-P[i].se;
				ge[now]+=a[t].s;
			} else
			{
				LL t=P[i].se;
				LL d=a[t].s;
				fd(j,now,1)
				{
					if (ge[j])
					{
						LL w=min(ge[j],d);
						d-=w;
						ge[j]-=w;
						LL dis=P[i].fi-P[j].fi;
						ans=(ans+((n+1)*dis-dis*(dis+1)/2)%Mod*w%Mod)%Mod;
					}
					if (!d) break;
				}
			}
		}
		cost=(cost-ans)%Mod;
		cost=(cost+Mod)%Mod;
		printf("Case #%d: ",ca);
		cout<<cost<<endl;
	}
	return 0;
}
