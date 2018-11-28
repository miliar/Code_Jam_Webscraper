#include <cmath>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;
typedef pair<int,int> PII;

#define maxn 101010
#define maxe 202020
int a[maxn],n;
int cal1(int l,int r)
{
	for(int i=l;i<r;i++)if(a[i]>a[i+1])
		return 0;
	return 1;
}
int cal2(int l,int r)
{
	for(int i=l;i<r;i++)if(a[i]<a[i+1])
		return 0;
	return 1;
}
int dfs(int x,int y)
{
	int tmp=0,i,j,p=-1;
	for(i=x;i<=y;i++)
	{
		if(tmp<a[i])
			tmp=a[i],p=i;
	}
	int ls=cal1(x,p);
	int rs=cal2(p,y);
	if(ls&&rs) return 0;
	for(i=x;i<=y;i++)
	{
		if(tmp>a[i])
			tmp=a[i],p=i;
	}
	int ans=0;
	if(p-x<y-p)
	{
		ans=p-x;
		while(p>x)
			swap(a[p],a[p-1]),p--;
		return ans+dfs(x+1,y);
	}
	else
	{
		ans=y-p;
		while(p<y)
			swap(a[p],a[p+1]),p++;
		return ans+dfs(x,y-1);
	}
}
int main()
{
	int i,j,ncase,tt=0;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&ncase);
	while(ncase--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%d",&a[i]);
		printf("Case #%d: %d\n",++tt,dfs(0,n-1));
	}
	return 0;
}