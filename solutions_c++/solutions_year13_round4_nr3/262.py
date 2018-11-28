#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <sstream>
#include <cmath>

using namespace std;
int casenum,T;
int a[30],b[30];
int f[30];
bool h[30];
bool ok;
int n;
void dfs(int dep)
{
	if (dep==n+1)
	{
		for (int i=n-1;i>=1;i--)
		{
			int m=0;
			for (int j=n;j>i;j--)
				if (f[i]>f[j]) m=max(m,b[j]);
			if (b[i]!=m+1) return;
		}
		ok=true;
		for (int i=1;i<=n;i++)
		{
			if (i<n) cout<<f[i]<<" ";
			else cout<<f[i]<<endl;
		}
		return;
	}
	for (int i=1;i<=n;i++)
	{
		if (h[i]) continue;
		f[dep]=i;
		int m=0;
		for (int j=1;j<dep;j++)
			if (f[j]<f[dep]) m=max(m,a[j]);
		if (a[dep]!=m+1) continue;
		bool flag=true;
		for (int j=1;j<dep;j++)
			if (b[j]<=b[dep]&&f[j]>f[dep])
			{
				flag=false;
				break;
			}
		if (!flag) continue;
		h[i]=true;
		dfs(dep+1);
		if (ok) return;
		h[i]=false;
	}
}
void dfs2(int dep)
{
	if (dep==n+1)
	{
		for (int i=n-1;i>=1;i--)
		{
			int m=0;
			for (int j=n;j>i;j--)
				if (f[i]>f[j]) m=max(m,b[j]);
			if (b[i]!=m+1) return;
		}
		ok=true;
		for (int i=n;i>=1;i--)
		{
			if (i>1) cout<<f[i]<<" ";
			else cout<<f[i]<<endl;
		}
		return;
	}
	for (int i=n;i>=1;i--)
	{
		if (h[i]) continue;
		f[dep]=i;
		int m=0;
		for (int j=1;j<dep;j++)
			if (f[j]<f[dep]) m=max(m,a[j]);
		if (a[dep]!=m+1) continue;
		bool flag=true;
		for (int j=1;j<dep;j++)
			if (b[j]<=b[dep]&&f[j]>f[dep])
			{
				flag=false;
				break;
			}
		if (!flag) continue;
		h[i]=true;
		dfs2(dep+1);
		if (ok) return;
		h[i]=false;
	}
}
int main()
{
	freopen("gcj.in","r",stdin);
	//freopen("gcj.out","w",stdout);

	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		if (casenum<=13)
		{
			cin>>n;
			for (int i=1;i<=n;i++)
				cin>>a[i];
			for (int i=1;i<=n;i++)
				cin>>b[i];
			cout<<endl;
			continue;
		}


		cin>>n;
		for (int i=1;i<=n;i++)
			cin>>a[i];
		for (int i=1;i<=n;i++)
			cin>>b[i];
		memset(h,0,sizeof(h));
		ok=false;
		dfs(1);


		/*cin>>n;
		for (int i=n;i>=1;i--)
			cin>>b[i];
		for (int i=n;i>=1;i--)
			cin>>a[i];
		memset(h,0,sizeof(h));
		ok=false;
		dfs2(1);*/
	}
	return 0;
}
