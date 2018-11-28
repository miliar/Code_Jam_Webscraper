#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;

typedef int LL;

LL arr1[6][6],arr2[6][6];
int main()
{
	LL cas=0,t,r1,r2,i,j,val;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.in","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&r1);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++) scanf("%d",&arr1[i][j]);
		}
		scanf("%d",&r2);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++) scanf("%d",&arr2[i][j]);
		}
		LL flag=0;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(arr1[r1][i]==arr2[r2][j])
				{
					flag++;
					val=arr1[r1][i];
					break;
				}
			}
		}
		if(flag==1) printf("Case #%d: %d\n",++cas,val);
		else if(flag) printf("Case #%d: Bad magician!\n",++cas);
		else printf("Case #%d: Volunteer cheated!\n",++cas);
	}
	return 0;
}