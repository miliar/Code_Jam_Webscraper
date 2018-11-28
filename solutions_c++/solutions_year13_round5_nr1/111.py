#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

long long a[100];
long long b;
bool check(int N,long long mid)
{
	long long need=0;
	for(int i=1;i<=N;i++)
		need+=mid-a[i];
	for(int i=N+1;i<=37;i++)
		if(a[i]<=mid)
			need+=mid+1-a[i];
	return need<=b;
}
void solve()
{
	int n;
	scanf("%lld %d",&b,&n);
	for(int i=1;i<=n;i++)
		scanf("%lld",&a[i]);
	for(int i=n+1;i<=37;i++)a[i]=0;
	sort(a+1,a+38);
	double ans=0;
	for(int N=1;N<=37;N++)
	{
		long long l=a[N],r=a[N]+b;
		while(l<r)
		{
			long long mid=(l+r)/2+1;
			if(check(N,mid))
				l=mid;
			else r=mid-1;
		}
		if(check(N,l))
		{
			long long s1=0;
			for(int i=1;i<=N;i++)
				s1+=l-a[i];
			long long s2=0;
			for(int i=N+1;i<=37;i++)
				if(a[i]<=l)
					s2+=l+1-a[i];
			ans=max(ans,(36.0/N-1)*s1-s2);
		}
	}
	printf("%.10f\n",ans);
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++cas);
		solve();
	}
}
