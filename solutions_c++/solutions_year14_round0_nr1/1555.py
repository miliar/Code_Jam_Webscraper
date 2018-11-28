#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int kase = 1, t;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",kase);
		kase++;
		int first,second,firstArr[4][4],secondArr[4][4],i,j,k;
		scanf("%d",&first);
		first = first - 1;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			scanf("%d",&firstArr[i][j]);
		}
		scanf("%d",&second);
		second = second - 1;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			scanf("%d",&secondArr[i][j]);
		}
		int match=0,cardNo=-1;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			if(firstArr[first][i] == secondArr[second][j])
			{
				match++;
				cardNo = firstArr[first][i];
			}
		}
		if(match == 1)
		{
			printf("%d\n",cardNo);
		} else if (match == 0)
		{
			printf("Volunteer cheated!\n");
		} else
		{
			printf("Bad magician!\n");
		}
	}
	return 0;
}
