//Author:Hena Firdaus
#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
typedef pair<int,int> ii;
#define fr(i,a,b) for(i=a;i<b;i++)
int vis[10];
int allVis()
{
	for(int i=0;i<10;i++)
	{
		if(!vis[i])
			return 0;
	}
	return 1;
}
int main()
{
	long long m,tt;
	int n,t,f;
	
	
	freopen("in2.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		memset(vis,0,sizeof(vis));
		f=0;
		cin>>n;
		if(n==0)
			{cout<<"Case #"<<i<<": INSOMNIA\n";
		    continue;}
		for(long long j=1;;j++)
		{
			 m=n*j;
			 tt=m;
			while(m)
			{
				int x=m%10;
				m/=10;
				vis[x]=1;
				if(allVis())
				{
					f=1;
					break;
				}
			}
			if(f)
			{
				cout<<"Case #"<<i<<": "<<tt<<endl;
				break;
			}
		}
	}
	return 0;
}
