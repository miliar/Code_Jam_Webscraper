#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstring>
#include<algorithm>
#include<cstdlib>
using namespace std;

int T;
int N;
int vis[10];

void solve()
{
	int ca=0;
	scanf("%d",&T);
	while(T--)
	{
		memset(vis,0,sizeof(vis));
		ca++;
		scanf("%d",&N);
		printf("Case #%d: ",ca);
		if(N==0)printf("INSOMNIA\n");
		else
		{
			for(int i=1;;i++)
			{
				int now=i*N;
				
				while(now>0)
				{
					int x=now%10;
					vis[x]=1;
					now/=10;
				}
				
				int no=0;
				for(int j=0;j<10;j++)no+=vis[j];
				
				if(no==10)
				{
				   printf("%d\n",i*N);
				   break;
				}
			}
		}
		
	}
}

int main()
{
	//freopen("Counting Sheep.in","r",stdin);
	//freopen("Counting Sheep.out","w",stdout);
	
	solve();
	
	return 0;
}
