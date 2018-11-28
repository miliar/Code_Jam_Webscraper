#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <iostream>

using namespace std;

typedef long long big;

int a[5][5],b[5][5];
int vis[20];
int main()
{
	int x,y,cas,cass,i,j;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&cas);
	for(cass=1;cass<=cas;cass++)
	{
		scanf("%d",&x);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&y);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&b[i][j]);
		memset(vis,0,sizeof(vis));
		for(i=1;i<=4;i++)
			vis[a[x][i]]++;
		for(i=1;i<=4;i++)
			vis[b[y][i]]++;
		int cnt=0;
		for(i=1;i<=16;i++)
		{
			if(vis[i]>=2)cnt++;
		}
		printf("Case #%d: ",cass);
		if(cnt>1)puts("Bad magician!");
		else if(cnt<1)puts("Volunteer cheated!");
		else
		{
			for(i=1;i<=16;i++)
				if(vis[i]>=2)break;
			printf("%d\n",i);
		}
	}
}
