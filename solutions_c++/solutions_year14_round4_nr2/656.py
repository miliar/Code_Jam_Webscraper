#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
const int oo=1073741819;
using namespace std;
int u[2000000],a[2000000],b[2000000],st[2000000],p[2000000];
int c[2000000];
int f[2005][2005];
int t,n;
bool cmp(int i,int j)
{
	return a[i]<a[j];
}
void change(int x)
{
	for (;x<=n;x+=(x & -x)) b[x]++;
}
int query(int x)
{
	int ans=0;
	for (;x;x-=(x & -x)) ans+=b[x];
	return ans;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int test=1;t;t--,test++) {
		printf("Case #%d: ",test);
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
			scanf("%d",&a[i]);
		for (int i=1;i<=n;i++) u[i]=i;
		sort(u+1,u+n+1,cmp);
		for (int i=1;i<=n;i++) p[u[i]]=i;
		for (int i=1;i<=n;i++) b[i]=c[i]=0;
		for (int i=1;i<=n;i++)
			for (int j=i+1;j<=n;j++)
				if (a[i]>a[j]) b[i]++,c[j]++;
		int ans=0;
		for (int i=1;i<=n;i++) {
			int sum=oo;
			int tot=0;
			for (int j=i+1;j<=n;j++)
				if (u[j]<u[i]) tot++;
			sum=min(sum,tot);
			tot=0;
			for (int j=i+1;j<=n;j++)
				if (u[j]>u[i]) tot++;
			sum=min(sum,tot);
			ans+=sum;
		}
		//for (int i=0;i<=n;i++) ans=min(ans,f[n][i]);
		printf("%d\n",ans);
	}
	return 0;
}
