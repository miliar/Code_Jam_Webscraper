#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<stdio.h> 
#include<stdlib.h>
using namespace std;
int num=0;

void Gao()
{
	int n,k;
	cin>>n>>k;
	vector<double> a;
	printf("Case #%d: ",++num);
	for(int i=0;i<n;i++){
		double x;
		cin>>x;a.push_back(x);
	}
	
	sort(a.begin(),a.end());
	double f[210][210],g[210][210];
	for (int i=0;i<n;i++)
		for (int j=0;j<n;j++)
			f[i][j]=0.0;
	
	f[0][0]=1.0-a[0];
	f[0][1]=a[0];
	for (int i=1;i<n;i++)
	{
		for (int j=0;j<=i;j++)
		{
			if (j>0)
				f[i][j]+=f[i-1][j-1]*a[i]+f[i-1][j]*(1-a[i]);
			if(j==0)
				f[i][j]=f[i-1][j]*(1-a[i]);
		}
	}
	
	vector<double>b;
	for(int i=n-1;i>=0;i--)
		b.push_back(a[i]);
		
	g[0][0]=1.0-b[0];
	g[0][1]=b[0];
	for (int i=1;i<n;i++)
	{
		for (int j=0;j<=i;j++)
		{
			if (j>0)
				g[i][j]+=g[i-1][j-1]*b[i]+g[i-1][j]*(1-b[i]);
			if(j==0)
				g[i][j]+=g[i-1][j]*(1-b[i]);
		}
	}
	double maxx=0;
	for (int i=0;i<=k;i++){
		int remain=k-i;
		double temp=0;
		for(int j=0;j<=i;j++)
		{
			if(j>k/2)
				continue;
			int needs=(k/2)-j;
			double tem=f[i][j]*g[remain-2][needs];
			if(tem>maxx)
				maxx=tem;
		}
	}
	cout<<maxx<<endl;
}

int main()
{
	freopen("b.in","r",stdin);
	int T;
	cin>>T;
	while(T--)
		Gao();
}
