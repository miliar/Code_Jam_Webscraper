#include<iostream>
#include<fstream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<iomanip>
#include<ctime>
#include<cstring>
#include<climits>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<algorithm>
#include<stack>
#include<deque>
#include<list>
#include<vector>
#define LL long long
using namespace std;
int cnt,snt,n,L,m,times;
LL oo=1000000007;
int a[1010],b[1010],c[1010],sum[1010],ans;
struct pp
{
	int x,pos;
}p[1010];
bool cmp(pp x,pp y)
{
	return x.x<y.x;
}
int lowbit(int x)
{
	return x&-x;
}
int get(int x)
{
	int ans=0;
	while (x>0)
	{
		ans+=sum[x];
		x-=lowbit(x);
	}
	return ans;
}
void updata(int x,int y)
{
	while (x<=n)
	{
		sum[x]+=y;
		x+=lowbit(x);
	}
}
void work(int lab)
{
	scanf("%d",&n);
	for (int i=1;i<=n;i++) scanf("%d",&a[i]),p[i].x=a[i],p[i].pos=i;
	sort(p+1,p+n+1,cmp);
	int maxn=-oo,pos=-1;
	for (int i=1;i<=n;i++) 
	if (a[i]>maxn)
	{
		maxn=a[i];
		pos=i;
	}
	ans=0;
	int hb=0,hc=n+1;
	for (int i=1;i<=n;i++)
	{
		int minn=oo,tpos=-1;
		for (int j=hb+1;j<=hc-1;j++)
		if (a[j]<minn)
		{
			tpos=j;
			minn=a[j];
		}
		if (tpos-(hb+1)<hc-1-tpos)
		{
			while (tpos!=hb+1) swap(a[tpos],a[tpos-1]),tpos--,ans++;
			hb++;
		}
		else 
		{
			while (tpos!=hc-1) swap(a[tpos],a[tpos+1]),tpos++,ans++;
			hc--;
		}
	}
	printf("Case #%d: %d\n",lab,ans);
}
int main()
{
	freopen("data1.in","r",stdin);
	freopen("data.out","w",stdout);
	scanf("%d",&times);
	for (int i=1;i<=times;i++)
	work(i);
	return 0;
}

