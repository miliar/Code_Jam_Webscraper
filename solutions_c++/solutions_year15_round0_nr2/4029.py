#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
#include <limits>
#include <unordered_set>
#include <set>
#include <memory.h>
using namespace std;
const long long MOD=1000000000000000007;
int p[60];
int ha[60];
int deep;
long long Hash(int n)
{
	long long h=0;
	long long base=1;
	for(int i=0;i<n;i++)
	{
		h+=(ha[i]*base)%MOD;
		base=(base*10)%MOD;
	}
	return h;
}
unordered_set<long long> check;
bool dfs(int d,int n)
{
	if(d>deep)return false;
	int i;
	for(i=0;i<n;i++)if(p[i]>0)break;
	if(i==n)return true;
	for(int i=0;i<n;i++)p[i]--;
	if(dfs(d+1,n))return true;
	int newpos=-1;
	for(int i=0;i<n;i++)if(!++p[i])newpos=i;
	int newn=n;
	if(newpos==-1)newpos=newn++;
	for(int i=0;i<n;i++)if(p[i]>3)
	{
		int bak=p[i];
		for(int j=1;j<bak;j++)
		{
			p[i]=j;
			p[newpos]=bak-j;
			memcpy(ha,p,newn*sizeof(int));
			sort(ha,ha+newn);
			if(!check.insert(Hash(newn)).second)continue;
			if(dfs(d+1,newn))return true;
		}
		p[i]=bak;
	}
	if(newn==n)p[newpos]=0;
	return false;
}
int solve()
{
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)scanf("%d",p+i);
	deep=0;
	while(true)
	{
		check.clear();
		if(dfs(0,n))return deep;
		deep++;
	}
}
int main()
{
	freopen("/Users/Erona/Downloads/B-small-attempt6.in","r",stdin);
	freopen("/Users/Erona/Downloads/B-small-attempt6.out","w",stdout);
	int T;
	scanf("%d",&T); for(int Case=1;Case<=T;Case++)printf("Case #%d: %d\n",Case,solve());
	return 0;
}