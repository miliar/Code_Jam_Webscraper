#include<iostream>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<cstdio>
#include<cmath>
using namespace std;
int ans,T,n,a[30][30],b[30],c[30];
char str[30];
bool pd()
{
	memset(b,0,sizeof(b));
	memset(c,0,sizeof(c));
	int sum=0;
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=n;j++)
		{
			b[i]=b[i]*2+a[i][j];
			c[i]=c[i]+a[i][j];
		}
		//sum+=c[i];
	}
	//cout<<sum<<endl;
	int num=0;
	for(int i=1;i<=n;i++)
	{
		num=0;
		for(int j=1;j<=n;j++)
			if (b[i]==b[j])
				num++;
			else
				if ((b[i]&b[j])!=0)
					return false;
		if (num!=c[i])
			return false;
	}
	return true;
}
void dfs(int i,int j,int k)
{
	if (i>n)
	{
		//cout<<k<<endl;
		if (k<ans)
		{
			if (pd())
				ans=min(ans,k);
		}
		return;
	}
	if (j>n)
		dfs(i+1,1,k);
	else
	{
		if (a[i][j]==1)
			dfs(i,j+1,k);
		else
		{
			a[i][j]=1;
			dfs(i,j+1,k+1);
			a[i][j]=0;
			dfs(i,j+1,k);
		}
	}
	return;
}
int main()
{
	freopen("t.in","r",stdin);
	freopen("t.out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%s",str);
			for(int j=1;j<=n;j++)
				if (str[j-1]=='0')
					a[i][j]=0;
			else
				a[i][j]=1;
		}
		ans=10000000;
		dfs(1,1,0);
		printf("Case #%d: %d\n",tt,ans);	
	}
}