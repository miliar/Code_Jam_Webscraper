#include <cstdio>

int getCard(int *a, int *b);
int main()
{
	freopen("TestSets/magicTrick.in","r",stdin);
	freopen("TestSets/magicTrickOut.out","w",stdout);

	int t,cnt = 1,card,ans1,first[4][4],ans2,second[4][4];
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&ans1);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&first[i][j]);
			}
		}

		scanf("%d",&ans2);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&second[i][j]);
			}
		}
		card = getCard(first[ans1-1],second[ans2-1]);
		if(card>0)
			printf("Case #%d: %d\n",cnt,card);
		else if (card==0)
			printf("Case #%d: Bad magician!\n",cnt);
		else
			printf("Case #%d: Volunteer cheated!\n",cnt);
		cnt++;
	}

	fclose (stdin);
	fclose (stdout);
	return 0;
}

int getCard(int *a, int *b)
{
	int count = 0, matched = 0;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(a[i]==b[j])
			{
				count++;
				matched = a[i];
			}
		}
	}
	if(count==1)
		return matched;
	else if(count==0)
		return -1;
	else
		return 0;
}
