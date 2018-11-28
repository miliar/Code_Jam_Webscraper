#include<stdio.h>
#include<string.h>

#define N 4

int ans[2],card[2][N][N],cnt[20];

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out_a1.txt","w",stdout);
	int t,i,j,k,num,m,sol;
	scanf("%d",&t);
	for(m=1;m<=t;++m)
	{
		num=-1;
		memset(cnt,0,sizeof(cnt));
		for(i=0;i<2;++i)
		{
			scanf("%d",&ans[i]);
			for(j=0;j<4;++j)
			{
				for(k=0;k<4;++k)
				{
					scanf("%d",&card[i][j][k]);
					if(j==ans[i]-1)
					{
						++cnt[card[i][j][k]];
					}
				}
			}
		}
		sol=0;
		for(i=1;i<=16;++i)
		{
			if(cnt[i]==2)
			{
				num=i;
				++sol;
			}
		}
		if(sol==0)
		{
			printf("Case #%d: Volunteer cheated!\n",m);
		}
		else if(sol==1)
		{
			printf("Case #%d: %d\n",m,num);
		}
		else
		{
			printf("Case #%d: Bad magician!\n",m);
		}
	}
	return 0;
}