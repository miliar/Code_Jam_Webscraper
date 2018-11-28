#include<cstdio>
#include<cstring>
const int maxn=5;
int map[maxn][maxn];
int hash[20];

int main()
{
	int T,t;
	freopen("1.in","r",stdin);
	freopen("1.txt","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		int x=2;
		memset(hash,0,sizeof(hash));
		while(x--)
		{
			int n;
			scanf("%d",&n);
			for(int i=1;i<=4;i++)
				for(int j=1;j<=4;j++)
					scanf("%d",&map[i][j]);
			for(int j=1;j<=4;j++)
			{
				//printf("%d\n",map[n][j]);
				hash[map[n][j]]++;	
			}
		}
		int tow=0,ans=0;
		for(int i=1;i<=16;i++)
			if(hash[i]==2)
			{
				tow++;
				ans=i;
			}
		printf("Case #%d: ",t);
		switch(tow)
		{
			case 0:printf("Volunteer cheated!\n");break;
			case 1:printf("%d\n",ans);break;
			default:printf("Bad magician!\n");
		}
	}	
	return 0;
}