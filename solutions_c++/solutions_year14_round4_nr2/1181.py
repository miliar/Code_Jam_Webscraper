#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <sstream>

using namespace std;
int n,a[1111];
int bf()
{
	int ma=0;for(int i=1;i<=n;i++)ma=max(ma,a[i]);
	int ans=n*n;
	for(int i=0;i<(1<<n);i++)
	{
		int t=0;
		for(int j=1;j<=n;j++)
			for(int k=j+1;k<=n;k++)
			{
				int x=a[j];
				if(i&(1<<(j-1)))x=2*ma-a[j];
				int y=a[k];
				if(i&(1<<(k-1)))y=2*ma-a[k];
				if(x>y)t++;
			}
		ans=min(ans,t);
	}
	return ans;
}
int L[1111],R[1111];
void solve()
{
	scanf("%d",&n);
	for(int i=1;i<=n;i++)scanf("%d",&a[i]);
//	int pos=1;
//	for(int i=1;i<=n;i++)if(a[i]>a[pos])pos=i;
//	for(int i=pos+1;i<=n;i++)a[i-1]=a[i];
//	for(int i=1;i<n;i++)
//	{
//		int cnt=0;
//		for(int j=1;j<i;j++)if(a[j]>a[i])cnt++;
//		L[i]=L[i-1]+cnt;
//	}
//	R[n]=0;
//	for(int i=n-1;i>=1;i--)
//	{
//		int cnt=0;
//		for(int j=i+1;j<n;j++)if(a[j]>a[i])cnt++;
//		R[i]=R[i+1]+cnt;
//	}
//	int ans=n*n;
//	for(int i=0;i<n;i++)
//	{
//		int t=L[i]+R[i+1]+abs(pos-(i+1));
//		ans=min(ans,t);
//	}
//	if(bf()!=ans)
//	{
//		printf("%d\n",n);
//		for(int i=1;i<=n;i++)printf("%d ",a[i]);
//		puts("");
//	}
	printf("%d\n",bf());
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		solve();
	}
}
