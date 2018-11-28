#include <stdio.h>
#include <string.h>

int t,r1,r2,a[4][4],b[4][4],cnt[17];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for(int ncase=1;ncase<=t;++ncase)
	{
		memset(cnt,0,sizeof(cnt));
		scanf("%d",&r1);
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				scanf("%d",&a[i][j]);
		for(int i=0;i<4;++i)
			++cnt[a[r1-1][i]];
		scanf("%d",&r2);
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				scanf("%d",&b[i][j]);
		for(int i=0;i<4;++i)
			++cnt[b[r2-1][i]];
		int ans = -1;
		bool ok=1;
		for(int i=1;i<=16;++i)
			if(cnt[i]==2)
			{
				if(ans==-1)
					ans=i;
				else
					ok=0;
			}
		if(!ok)
			printf("Case #%d: Bad magician!\n",ncase);
		else if(ans==-1)
			printf("Case #%d: Volunteer cheated!\n",ncase);
		else
			printf("Case #%d: %d\n",ncase,ans);
	}
	return 0;
}