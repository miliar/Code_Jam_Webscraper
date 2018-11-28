#include<iostream>
#include<cstdio>
#include<cstring>
#include<stack>

using namespace std;

int ans1,ans2;
int card1[5][5],card2[5][5];
bool num1[17],num2[17];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-answer.out","w",stdout);

	int kase;

	scanf("%d",&kase);

	for(int x=1;x<=kase;x++)
	{
		memset(num1,false,sizeof(num1));
		scanf("%d",&ans1);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				scanf("%d",&card1[i][j]);
		for(int j=1;j<=4;j++)
			num1[card1[ans1][j]]=true;
		memset(num2,false,sizeof(num2));
		scanf("%d",&ans2);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				scanf("%d",&card2[i][j]);
		for(int j=1;j<=4;j++)
			num2[card2[ans2][j]]=true;

		int y=0;
		for(int i=1;i<=16;i++)
		{
			if(num1[i]&&num2[i])
			{
				if(y==0)
					y=i;
				else
					y=-1;
			}
		}

		if(y==0)
			printf("Case #%d: Volunteer cheated!\n",x);
		else if(y==-1)
			printf("Case #%d: Bad magician!\n",x);
		else
			printf("Case #%d: %d\n",x,y);
	}

	return 0;
}
