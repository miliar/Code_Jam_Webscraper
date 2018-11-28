#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int T;
int m1[10][10];
int m2[10][10];
int main()
{
	//freopen("5.in","r",stdin);
	//freopen("1.out","w",stdout);
	scanf("%d",&T);
	int t=0;
	int r1,r2;
	while(T--)
	{
		t++;
		scanf("%d",&r1);
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
				scanf("%d",&m1[i][j]);
		}
		scanf("%d",&r2);
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
				scanf("%d",&m2[i][j]);
		}
		int cnt=0;
		int temp;
		int ans;
		for(int i=1;i<=4;i++)
		{
			temp = m1[r1][i]; 
			for(int j=1;j<=4;j++)
			{
				if(temp==m2[r2][j])
				{
					ans = temp;
					cnt++;
				}
			}
		}
		printf("Case #%d: ",t);
		if(cnt==1)
			printf("%d\n",ans);
		else if(cnt>1)
			printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
	return 0;
}
