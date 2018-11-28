#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
double f[300][300],b[300],a[300],ans;
int n,k,T;
bool used[300];
double cal()
{
	int m=0;
	for(int i=1;i<=n;i++)
		if (used[i])
		{
			m++;
			b[m]=a[i];
		}
	memset(f,0,sizeof(f));
	f[0][0]=1;
	for(int i=1;i<=m;i++)
	{
		for(int j=0;j<=i;j++)
			f[i][j]=f[i-1][j]*(1-b[i])+f[i-1][j-1]*b[i];
	}
	return f[m][m/2];
}
/*void dfs(int i,int j)
{
	if (i>n)
	{
		if (j==k)
		{
			//cout<<"sb"<<endl;
			ans=max(ans,cal());
		}
		return;
	}
	used[i]=true;
	dfs(i+1,j+1);
	used[i]=false;
	dfs(i+1,j);
	return;
}*/
int main()
{
	freopen("t.in","r",stdin);
	freopen("t.out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d %d",&n,&k);
		memset(used,false,sizeof(used));
		for(int i=1;i<=n;i++)
			scanf("%lf",&a[i]);
		ans=0;
		sort(a+1,a+n+1);
		memset(used,false,sizeof(used));
		for(int i=1;i<=k;i++)
			used[i]=true;
		ans=max(ans,cal());
		memset(used,false,sizeof(used));
		for(int i=1;i<=k;i++)
			used[n-i+1]=true;
		ans=max(ans,cal());
		for(int i=1;i<=k;i++)
		{
			memset(used,false,sizeof(used));
			for(int j=1;j<=i;j++)
				used[j]=true;
			for(int j=1;j<=(k-i);j++)
				used[n-j+1]=true;
			ans=max(ans,cal());
		}
		//dfs(1,0);
		printf("Case #%d: %.6f\n",tt,ans);
	}
}