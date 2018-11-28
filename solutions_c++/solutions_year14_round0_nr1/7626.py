#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define maxn 5
int key1[maxn][maxn];
int key2[maxn][maxn];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas = 0;
	scanf("%d",&t);
	while(t--)
	{
		int a,b;
		scanf("%d",&a);
		for(int i = 1;i <= 4;i++)
			for(int j = 1;j <= 4;j++)
				scanf("%d",&key1[i][j]);
		scanf("%d",&b);
		for(int i = 1;i <= 4;i++)
			for(int j = 1;j <= 4;j++)
				scanf("%d",&key2[i][j]);
		int ok = 0,ans;
		for(int i = 1;i <= 4;i++)
		{
			for(int j = 1;j <= 4;j++)
			{
				if(key1[a][i] == key2[b][j])
				{
					ans = key1[a][i];
					ok++;
					break;
				}
			}
		}
		printf("Case #%d: ",++cas);
		if(ok == 0)	puts("Volunteer cheated!");
		else if(ok == 1)	printf("%d\n",ans);
		else puts("Bad magician!");
	}
	return 0;
}