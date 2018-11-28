#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<queue>
#include<map>
#include<set>
using namespace std;
#define INF 1000000000
int t,a1,a2,num1[6][6],num2[6][6];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int time=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&a1);
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&num1[i][j]);
			}
		}
		scanf("%d",&a2);
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&num2[i][j]);
			}
		}
		int cou=0,mark;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				if(num1[a1][i]==num2[a2][j])
				{
					cou++; mark=num1[a1][i];
				}
			}
		}
		printf("Case #%d: ",++time);
		if(cou==0) printf("Volunteer cheated!\n");
		else if(cou>1) printf("Bad magician!\n");
		else printf("%d\n",mark);
	}


    return 0;
}
