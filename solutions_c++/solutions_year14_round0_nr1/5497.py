#include <stdio.h>
#include <string.h>
int main()
{
	int t, ans, count, test=0;
	int a[4][4], b[4][4], i, j, r1, r2, flag[20];
	freopen("A-small-attempt1.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		memset(flag,0,sizeof(flag));
		count = 0;
		scanf("%d",&r1);
		r1--;
		for( i = 0; i < 4; i ++ )
			for( j = 0; j < 4; j ++ )
				scanf("%d",&a[i][j]);
		for( i = 0; i < 4; i ++ )
			flag[a[r1][i]] = 1;
		scanf("%d",&r2);
		r2--;
		for( i = 0; i < 4; i ++ )
			for( j = 0; j < 4; j ++ )
				scanf("%d",&b[i][j]);
		for( i = 0; i < 4; i ++ )
		{
			if(flag[b[r2][i]] == 1 )
			{
				count++;
				ans = b[r2][i];
			}
		}
		printf("Case #%d: ",++test);
		if( count == 1 )
			printf("%d\n",ans);
		else if(count > 1)
			printf("Bad magician!\n");
		else
			puts("Volunteer cheated!");
	}

	return 0;
}