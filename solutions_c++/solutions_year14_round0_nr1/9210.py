#include<iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int vis[17];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int i,T;
	cin>>T;
	for (int ca=1;ca<=T;ca++)
	{
		memset(vis,0,sizeof(vis));
		int f1;
		scanf("%d",&f1);
		for( i=1;i<=4;i++)
		{
			for (int j=1;j<=4;j++)
			{
				int a;
				scanf("%d",&a);
				if (i==f1) vis[a]=1;
			}
		}
		int num=0,ans=0;
		scanf("%d",&f1);
		for( i=1;i<=4;i++)
		{
			for (int j=1;j<=4;j++)
			{
				int a;
				scanf("%d",&a);
				if (i==f1) vis[a]++;
			}
		}
		for ( i=1;i<=16;i++)
			if (vis[i]==2){num++;ans=i;}
		if (num==1)
		{
			printf("Case #%d: %d\n",ca,ans);
			continue;
		}
		if (num==0)
		{
			printf("Case #%d: Volunteer cheated!\n",ca);
			continue;
		}

			printf("Case #%d: Bad magician!\n",ca);
	}
	return 0;
}