#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

using namespace std;

const int N = 110;

int val[N][N];
int rmax[N],cmax[N];

int main()
{
	int csnum;
//	freopen("in","r",stdin);
//	freopen("out","w",stdout);
	scanf("%d",&csnum);
	for(int cs=1;cs<=csnum;cs++)
	{
		int n,m;
		scanf("%d %d",&n,&m);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				scanf("%d",&val[i][j]);
		for(int i=1;i<=n;i++)
		{
			rmax[i]=val[i][1];
			for(int j=1;j<=m;j++)
				rmax[i]=max(rmax[i],val[i][j]);
		}
		for(int i=1;i<=m;i++)
		{
			cmax[i]=val[1][i];
			for(int j=1;j<=n;j++)
				cmax[i]=max(cmax[i],val[j][i]);
		}
		int flag=true;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				if(val[i][j]!=rmax[i]&&val[i][j]!=cmax[j])
					flag=false;
		printf("Case #%d: %s\n",cs,flag?"YES":"NO");
	}
	return 0;
}