#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
	//freopen("B-small-attempt1.in","r",stdin);
	//freopen("output1.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		int n,m;
		int a[100][100];
		bool valid[100][100];
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)for(int j=0;j<m;j++)
		{
			scanf("%d",&a[i][j]);
			if(a[i][j]==1)valid[i][j]=false;
			else valid[i][j]=true;
		}
		bool flag;
		for(int i=0;i<n;i++)
		{
			flag=true;
			for(int j=0;j<m;j++)if(a[i][j]==2){flag = false;}
			if(flag)for(int j=0;j<m;j++)if(a[i][j]==1){valid[i][j]=true;}
		}
		for(int j=0;j<m;j++)
		{
			flag=true;
			for(int i=0;i<n;i++)if(a[i][j]==2){flag = false;}
			if(flag)for(int i=0;i<n;i++)if(a[i][j]==1){valid[i][j]=true;}
		}
		flag=true;
		for(int i=0;i<n;i++)for(int j=0;j<m;j++)if(valid[i][j]==false){flag=false;break;}
		printf("Case #%d: ",k);
		if(flag)printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}