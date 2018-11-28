#if 1
#include<stdio.h>
#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>

using namespace std;
int main()
{
	freopen("text.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int p=0;p<t;p++)
	{
	int a[110][110]={},b[110][110]={};
		int n,m;
		cin>>n>>m;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				cin>>a[i][j];
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				b[i][j]=100;
			}
		}
		for(int i=0;i<n;i++)
		{
			int p=1;
			for(int j=0;j<m;j++)
			{
				p=max(p,a[i][j]);
			}
			for(int j=0;j<m;j++)
			{
				b[i][j]=min(b[i][j],p);
			}
		}
		for(int i=0;i<m;i++)
		{
			int p=1;
			for(int j=0;j<n;j++)
			{
				p=max(p,a[j][i]);
			}
			for(int j=0;j<n;j++)
			{
				b[j][i]=min(b[j][i],p);
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(a[i][j]!=b[i][j])
				{
					cout<<"Case #"<<p+1<<": NO"<<endl;
					goto m;
				}
			}
		}
			cout<<"Case #"<<p+1<<": YES"<<endl;
m:;
	}
}













#endif