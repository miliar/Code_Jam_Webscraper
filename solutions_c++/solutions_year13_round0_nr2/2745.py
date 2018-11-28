#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[110][110],b[110][110],n,m,t,T,i,j,k,ans;
int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	cin>>T;
	while(T--)
	{
		cin>>n>>m;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++) cin>>a[i][j],b[i][j]=100;
		for(i=1;i<=n;i++)
		{
			k=0;
			for(j=1;j<=m;j++) k=max(k,a[i][j]);
			for(j=1;j<=m;j++) b[i][j]=min(k,b[i][j]);
		}
		for(j=1;j<=m;j++)
		{
			k=0;
			for(i=1;i<=n;i++) k=max(k,a[i][j]);
			for(i=1;i<=n;i++) b[i][j]=min(k,b[i][j]);
		}
		ans=0;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				if(a[i][j]==b[i][j]) ans++;
		cout<<"Case #"<<++t<<": "<<(ans==n*m?"YES":"NO")<<endl;;
	}
}
