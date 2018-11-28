#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;
#define ll long long
#define inf 0x3f3f3f3f

int a[5][5],b[5][5];
int main()
{
	int t;
	scanf("%d",&t);
	int he=0;
	while(t--)
	{
		he++;
		int n,m,i,j,k;
		scanf("%d",&n);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&m);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&b[i][j]);
		int cnt=0,ans;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			{
				if(a[n][i]==b[m][j])
				{
					cnt++;
					ans=a[n][i];
				}
			}
		printf("Case #%d: ",he);
		if(cnt==0)
			printf("Volunteer cheated!\n");
		else if(cnt==1)
			printf("%d\n",ans);
		else
			printf("Bad magician!\n");
	}
}