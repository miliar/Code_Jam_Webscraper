#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>
#include<iostream>
#include<vector>
using namespace std;

int a[11000];
int vis[11000];

int main()
{
	int i,t,n,j,k;

	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	cin>>t;

	int ii=0;
	while(t--)
	{
		int x;
		cin>>n>>x;

		for(i=0;i<n;i++)
			cin>>a[i];

		sort(a,a+n);

		memset(vis,0,sizeof(vis));

		int ans=0;
		for(i=0;i<n;i++)if(!vis[i])
		{
			ans++;
			vis[i]=1;
			for(j=n-1;j>i;j--)if(!vis[j]&&a[j]+a[i]<=x)
			{
				vis[j]=1;
				break;
			}
		}
		cout<<"Case #"<<++ii<<": "<<ans<<endl;
	}
}
