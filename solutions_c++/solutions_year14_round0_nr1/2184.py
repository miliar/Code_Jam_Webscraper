#include<cstdio>
#include<cstring>

using namespace std;

bool v[19];
int n[5][5];

int main(void)
{
	int cases,cas;
	int i,j;
	scanf("%d",&cases);
	for(cas=1;cas<=cases;cas++)
	{
		int r;
		scanf("%d",&r);
		for(i=1;i<=4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&n[i][j]);
		memset(v,0,sizeof(v));
		for(i=0;i<4;i++)
			v[n[r][i]]=1;
		scanf("%d",&r);

		for(i=1;i<=4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&n[i][j]);
		int cnt=0;
		int ans=0;

		for(i=0;i<4;i++)
		{
			if(v[n[r][i]])
			{
				cnt++;
				ans=n[r][i];
			}
		}

		printf("Case #%d: ",cas);
		if(cnt==1)
			printf("%d\n",ans);
		else if(cnt)
			printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
	return 0;
}
