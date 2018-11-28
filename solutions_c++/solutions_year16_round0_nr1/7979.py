#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
//	freopen("E:A-large.in","r",stdin);

//	freopen("E:A-small-attempt0.txt","w",stdout);

	int T;
	int n,k,vis[10];
	
	scanf("%d",&T);
	for(int fuck=1;fuck<=T;fuck++)
	{
		memset(vis,0,sizeof(vis));
		printf("Case #%d: ",fuck);
		scanf("%d",&n);
		if(n==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		int tmp=1;
		
		while(1)
		{
			int flag=0;
			k=n*tmp;
			tmp++;
			while(k)
			{
				vis[k%10]=1;
				k=k/10;
			}
			for(int i=0;i<=9;i++)
			{
				if(vis[i]==0)
				{
					flag=1;
				}
			}
			if(!flag)
			{
				break;
			}
		}
		printf("%d\n",(tmp-1)*n);
	}

}
