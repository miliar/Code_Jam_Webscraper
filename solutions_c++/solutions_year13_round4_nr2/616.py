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
const int oo=1047483647,maxn=310;
LL n,i,j,k,m,q,ans1,ans2,N,T,P,ca;
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
LL check(LL l,LL r,LL s)
{
	if (!l) return 1;
	LL ans=0;
	ans+=s/2;
	l--;
	l=l/2;
	ans+=check(l,s/2-l-1,s/2);
	return ans;
}
LL ok(LL l,LL r,LL s)
{
	if (!r) return l+1;
	LL ans=0;
	l=(l+1)/2;
	ans+=ok(l,s/2-l-1,s/2);
	return ans;
}
int main()
{
	freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
	T=Read();
	ca=0;
	for(;T;T--)
	{
		ca++;
		n=Read();
		P=Read();
		N=(1<<n)-1;
		LL l=0,r=(1<<n)-1;
		while (l<r)
		{
			LL mid=(l+r+1)/2;
			if (check(mid,N-mid,N+1)<=P) l=mid;
			else r=mid-1;
		}
		ans2=l;
		l=0,r=(1<<n)-1;
		while (l<r)
		{
			LL mid=(l+r+1)/2;
			if (ok(mid,N-mid,N+1)<=P) l=mid;
			else r=mid-1;
		}
		ans1=l;
        printf("Case #%d: ",ca);
		cout<<ans2<<' '<<ans1<<endl;
	}
	return 0;
}
