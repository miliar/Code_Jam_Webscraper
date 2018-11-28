#include<cstdio>
using namespace std;
int main()
{
	int ans,cnt,x,ar[5][5],t,tc;
	for(scanf("%d",&tc),t=1;t<=tc;t++)
	{
		int hash1[17]={},hash2[17]={};
		cnt=0;
		scanf("%d",&x);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&ar[i][j]);
				if(i==x)
					hash1[ar[i][j]]++;
			}
		scanf("%d",&x);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&ar[i][j]);
				if(i==x)
					hash2[ar[i][j]]++;
			}
		for(int i=1;i<=16;i++)
			if(hash1[i] && hash2[i])
			{
				cnt++;
				ans=i;
			}
		if(cnt==0)
			printf("Case #%d: Volunteer cheated!\n",t);
		else if(cnt>1)
			printf("Case #%d: Bad magician!\n",t);
		else
			printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}