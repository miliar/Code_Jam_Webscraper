#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>
using namespace std;
#define LL long long
ifstream fin("ai.txt");
ofstream fout("ap.txt");
int g[110][110],mr[110],mc[110];
int n,m;
int solve()	
{
	int i,j,k;
	memset(mr,0,sizeof(mr));
	memset(mc,0,sizeof(mc));
	for(i=0;i<n;i++)
	{
		int s=0;
		for(j=0;j<m;j++)
		{
			s=max(g[i][j],s);
		}
		mr[i]=s;
	}
	for(i=0;i<m;i++)
	{
		int s=0;
		for(j=0;j<n;j++)
		{
			s=max(g[j][i],s);
		}
		mc[i]=s;
	}
	
	for(i=0;i<n;i++)
		for(j=0;j<m;j++)
		{
			//if(g[i][j]==1)
			if(mr[i]>g[i][j]&&mc[j]>g[i][j])
				return 0;

		}
	return 1;
}
int main()
{
	freopen("ai.txt","r",stdin);
	freopen("bp.txt","w",stdout);
	int i,j,k;
	int t,cas;
	cin>>t;
	//fin>>t;
	for(cas=1;cas<=t;cas++)
	{
		cin>>n>>m;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				cin>>g[i][j];
		int res=solve();				
		printf("Case #%d: ",cas);	
		if(res)
			printf("YES\n");
		else
			printf("NO\n");
	}
	
	return 0;	
}
