#include <cstdio>
#include <cstring>
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int T,cse,ra,rb,i,j,a[5][5],b[5][5],c[20],ans,key;
	scanf("%d",&T);
	for(cse = 1;cse <= T;++cse)
	{
		scanf("%d",&ra);
		for(i = 1;i <= 4;++i)for(j = 1;j <= 4;++j)scanf("%d",&a[i][j]);
		scanf("%d",&rb);
		for(i = 1;i <= 4;++i)for(j = 1;j <= 4;++j)scanf("%d",&b[i][j]);
		memset(c,0,sizeof c);
		for(j = 1;j <= 4;++j)++c[a[ra][j]],++c[b[rb][j]];
		ans = 0;
		for(i = 1;i < 20;++i)if(c[i] > 1)++ans,key = i;
		if(ans == 0)printf("Case #%d: Volunteer cheated!\n",cse);
		else
		if(ans == 1)printf("Case #%d: %d\n",cse,key);
		else		printf("Case #%d: Bad magician!\n",cse);
	}
	return 0;
}
