#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<iostream>
using namespace std;
const int maxn=200010;

int a[2100],b[2100];
int ans[2100];

int vis[2100];
int dpa[2100],dpb[2100];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C1.out","w",stdout);

	int T,n,i,j,k;
	cin>>T;

	for(int ii=1;ii<=T;ii++)
	{
		cin>>n;
		for(i=1;i<=n;i++)
			cin>>a[i];
		for(i=1;i<=n;i++)
			cin>>b[i];

		memset(vis,0,sizeof(vis));
		memset(dpa,0,sizeof(dpa));
		memset(dpb,0,sizeof(dpb));
		memset(ans,0,sizeof(ans));

		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)if(!vis[j]&&b[j]==dpb[j]+1&&a[j]==dpa[j]+1)
			{

				int is=0;
				for(k=1;k<j;k++)if(!vis[k]&&b[k]<=b[j])
				{
					is=1;
					break;
				}
				for(k=j+1;k<=n;k++)if(!vis[k]&&a[k]<=a[j])
				{
					is=1;
					break;
				}
				if(is)
					continue;
				ans[j]=i;
				vis[j]=1;
				for(k=1;k<=j;k++)
					dpb[k]=max(dpb[k],b[j]);
				for(k=j;k<=n;k++)
					dpa[k]=max(dpa[k],a[j]);
				break;
			}
		}
		printf("Case #%d:",ii);
		for(i=1;i<=n;i++)
		{
			if(!ans[i])
				puts("wori!!!!!!!");
			printf(" %d",ans[i]);
		}
		puts("");
	}
}