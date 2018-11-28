#include <cstdio>
#include <cstring>
#include <algorithm>
#define M 105
int m[M][M];
bool is[M][M];
bool get(int x,int y,int n1,int m1)
{
	int i,mark=0,mark1=0;
	for(i=1;i<=m1;i++)
	{
		if(m[x][i]>m[x][y])
		{
			mark=1;
			break;
		}
	}
	for(i=1;i<=n1;i++)
	{
		if(m[i][y]>m[x][y])
		{
			mark1=1;
			break;
		}
	}
	if(mark==0||mark1==0)
		return true;
	return false;
}
bool judge(int n,int m1)
{
	int i,j;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m1;j++)
		{
			if(get(i,j,n,m1)==false)
			{
				return false;
			}
		}
	}
	return true;
}
int main()
{
	int t1,d=1,i,j,n,m1,t;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d",&n,&m1);
		t1=0;
		for(i=1;i<=n;i++)
			for(j=1;j<=m1;j++)
				scanf("%d",&m[i][j]);
		printf("Case #%d: ",d++);
		if(judge(n,m1))
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}

