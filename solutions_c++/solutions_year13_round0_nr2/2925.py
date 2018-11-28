#include<stdio.h>
#include<string.h>
int map[102][102];
int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j;
	int T,step;
	int m,n;
	int flag;
	int x,y;
	scanf("%d",&T);
	for(step=1;step<=T;step++)
	{
		printf("Case #%d: ",step);
		memset(map,-1,sizeof(map));
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				scanf("%d",&map[i][j]);
	/*	for(i=1;i<=n;i++,putchar(10))
			for(j=1;j<=m;j++)
				printf("%d  ",map[i][j]);*/
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				flag=0;
				for(x=i,y=1;y<=m&&map[x][y]<=map[i][j];y++);
			//	printf("i==%d,j==%d,x==%d,y==%d\n",i,j,x,y);
				if(y>m)flag=1;
				for(x=1,y=j;x<=n&&map[x][y]<=map[i][j];x++);
			//	printf("**i==%d,j==%d,x==%d,y==%d**\n",i,j,x,y);
				if(x>n)flag=1;
				if(flag==0)break;
			}
			if(flag==0)break;
		}
		if(flag==0)printf("NO\n");
		else printf("YES\n");
	}
	return(0);
}