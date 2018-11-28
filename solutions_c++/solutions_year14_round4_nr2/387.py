#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <queue>

#define mp make_pair
#define pb push_back

using namespace std;

typedef long long big;

const int N=10020;
const int inf=0x3f3f3f3f;
int n,a[N],b[N],id;
vector<int>slx;
int tr[N];
struct A
{
	int x,id;
	bool operator<(const A &t)const
	{
		return x<t.x;
	}
}c[N];
int get(int x)
{
	int s=0;
	for(;x;x-=x&-x)
		s+=tr[x];
	return s;
}
void add(int x)
{
	for(;x<=n;x+=x&-x)
		tr[x]++;
}

int cal1(int l,int r)
{
	if(l>r)return 0;
	int i,res=0;
	memset(tr,0,sizeof(tr));
	for(i=r;i>=l;i--)
	{
		res+=get(a[i]-1);
		add(a[i]);
	}
	return res;
}
int cal2(int l,int r)
{
	if(l>r)return 0;
	int i,res=0;
	memset(tr,0,sizeof(tr));
	for(i=l;i<=r;i++)
	{
		res+=get(a[i]-1);
		add(a[i]);
	}
	return res;
}
int sol(int x)
{
	int res=0,i;
	for(i=1;i<=n;i++)
		a[i]=b[i];
	if(id<x)
	{
		for(i=id+1;i<=x;i++)
			swap(a[i-1],a[i]),res++;
	}
	else
	{
		for(i=id;i>x;i--)
			swap(a[i],a[i-1]),res++;
	}
//	for(i=1;i<=n;i++)
//		printf("%d ",a[i]);
//	puts("");
	res+=cal1(1,x-1);
	res+=cal2(x+1,n);
	return res;
}
int d(int x,int y)
{
	return abs(x-y);
}
int solve()
{
	int i,j,l,r,res=0;
	for(i=1;i<=n;i++)
		a[i]=b[i];
	for(i=1;i<=n;i++)
		c[i].x=b[i],c[i].id=i;
	sort(c+1,c+1+n);
	l=0;r=0;
	for(i=1;i<=n;i++)
	{
		int x=l+1;
		for(j=l+1;j<=n-r;j++)
			if(a[j]<a[x])x=j;
		if(x-l-1<n-r-x)
		{
			for(j=x;j>l+1;j--)
				swap(a[j],a[j-1]),res++;
			l++;
		}
		else
		{
			for(j=x;j<n-r;j++)
				swap(a[j],a[j+1]),res++;
			r++;
		}
	}
	return res;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int i,cas,cass,j,mx,ans=inf;
	scanf("%d",&cas);
	for(cass=1;cass<=cas;cass++)
	{
		slx.clear();
		scanf("%d",&n);
		for(i=1;i<=n;i++)
			scanf("%d",&b[i]),slx.pb(b[i]);
		sort(slx.begin(),slx.end());
		for(i=1;i<=n;i++)
			b[i]=lower_bound(slx.begin(),slx.end(),b[i])-slx.begin()+1;
		mx=b[1];
		for(i=1;i<=n;i++)
			mx=max(mx,b[i]);
		for(i=1;i<=n;i++)
			if(mx==b[i])
				break;
		id=i;
		ans=inf;
		ans=solve();
		printf("Case #%d: ",cass);
		printf("%d\n",ans);
	}
}
