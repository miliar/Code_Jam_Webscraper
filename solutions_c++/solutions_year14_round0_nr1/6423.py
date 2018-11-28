//the queen problem
#include<cstdio>
#include<cstring>
using namespace std;
int flag[20];
int a[5][5];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small_attempt0.out","w",stdout);
	int o=0;
	int t,ans,out;
	int i,j;
	scanf("%d",&t);
	while(t--)
	{
		memset(flag,0,sizeof(flag));
		scanf("%d",&ans);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		for(i=1;i<=4;i++)flag[a[ans][i]]++;
		scanf("%d",&ans);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		int count=0;
		for(i=1;i<=4;i++)
		{
			if(flag[a[ans][i]])
			{
				out=a[ans][i];
				count++;
			}
		}
		if(count==0)
			printf("Case #%d: Volunteer cheated!\n",++o);
		if(count==1)
			printf("Case #%d: %d\n",++o,out);
		if(count>1)
			printf("Case #%d: Bad magician!\n",++o);

	}
	return 0;
}