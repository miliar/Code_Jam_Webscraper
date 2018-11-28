#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

void Init(void)
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
}

int data1[8][8];
int data2[8][8];

int main(void)
{
	Init();
	int i,j,k,n,m;
	int cases,tt;
	scanf("%d",&cases);
	for(tt=1; tt<=cases; ++tt)
	{
		scanf("%d",&n);
		for(i=1; i<=4; ++i)
		{
			for(j=1; j<=4; ++j)
			{
				scanf("%d",&data1[i][j]);
			}
		}
		scanf("%d",&m);
		for(i=1; i<=4; ++i)
		{
			for(j=1; j<=4; ++j)
			{
				scanf("%d",&data2[i][j]);
			}
		}

		int count = 0;
		int ans = 0;
		for(i=1; i<=4; ++i)
		{
			for(j=1; j<=4; ++j)
			{
				if(data1[n][i]==data2[m][j])
				{
					count++;
					ans = data1[n][i];
					break;
				}
			}
		}
		if(count==1)
			printf("Case #%d: %d\n", tt,ans);
		else if(count > 1)
			printf("Case #%d: Bad magician!\n", tt);
		else
			printf("Case #%d: Volunteer cheated!\n", tt);
	}
	return 0;
}