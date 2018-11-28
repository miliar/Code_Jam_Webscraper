#include <cstring>
#include <cstdlib>
#include <cstdio>

int t,id;
int n,m;
int map[110][110],max1[110],max2[110];
int i,j,flag;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);id=0;
	while(t--)
	{
		memset(max1,0,sizeof(max1));
		memset(max2,0,sizeof(max2));
		id++;
		printf("Case #%d: ",id);
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
			{
				scanf("%d",&map[i][j]);
				if (max1[i]<map[i][j])max1[i]=map[i][j];
				if (max2[j]<map[i][j])max2[j]=map[i][j];
			}

		flag=1;
		for (i=0;i<n && flag;i++)
			for (j=0;j<m && flag;j++)
			{
				if (max1[i]>map[i][j] && max2[j]>map[i][j])flag=0;
			}
		if (flag==1)printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}