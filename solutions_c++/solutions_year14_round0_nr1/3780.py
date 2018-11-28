#include<iostream>
#include<cstdio>
#include<cstdlib>

#define ll long long

using namespace std;

int main()
{
	int t;
	ll ans1,ans2,grid1[4][4],grid2[4][4],num;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		//printf("Case #%d:",i);
		scanf("%lld",&ans1);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%lld",&grid1[j][k]);
		scanf("%lld",&ans2);
		for(int j=0;j<4;j++)
                       for(int k=0;k<4;k++)
                               scanf("%lld",&grid2[j][k]);
		ans1=ans1-1;
		ans2=ans2-1;
		int finds=0;
		for(int j=0;j<4;j++)
		{
			ll tmp=grid1[ans1][j];
			for(int k=0;k<4;k++)
			{
				if(grid2[ans2][k]==tmp)
				{
					finds++;
					num=tmp;
					break;
				}
			}	
		}
		printf("Case #%d:",i);
		if(finds==1)
			printf(" %lld\n",num);
		else if(finds==0)
			printf(" Volunteer cheated!\n");
		else
			printf(" Bad magician!\n");
	}
	return 0;
}
