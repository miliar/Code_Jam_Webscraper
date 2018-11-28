#include<cstdio>
#include<cstring>

int T,ans1,ans2;
bool cnt[2][20];

int main()
{
	freopen("trick.in","r",stdin);
	freopen("trick.out","w",stdout);
	scanf("%d",&T);
	for (int cas = 1;cas <= T;cas ++)
	{
		memset(cnt,0,sizeof cnt);
		scanf("%d",&ans1);
		for (int i = 1;i <= 4;i ++)
			for (int j = 1;j <= 4;j ++)
			{
				int x;
				scanf("%d",&x);
				if (i == ans1) cnt[0][x] = 1;
			}
		scanf("%d",&ans2);
		for (int i = 1;i <= 4;i ++)
			for (int j = 1;j <= 4;j ++)
			{
				int x;
				scanf("%d",&x);
				if (i == ans2) cnt[1][x] = 1;
			}
		int c = 0,x;
		for (int i = 1;i <= 16;i ++)
			if (cnt[1][i] && cnt[0][i])
			{
				c ++;
				x = i;
			}
		printf("Case #%d: ",cas);
		if (c == 1) printf("%d\n",x);
		if (c > 1) puts("Bad magician!");
		if (!c) puts("Volunteer cheated!");
	}
	return 0;
}
