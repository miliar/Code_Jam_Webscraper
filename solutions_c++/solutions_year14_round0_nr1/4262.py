#include<iostream>
#include<cstdio>
using namespace std;
int a[5][5],b[5][5],i,j,n,coun,ans,count,temp[5],k,n1,n2;
int main()
{
	int t;count=0;coun=0;
	scanf("%d",&t);
	while(t--)
	{coun++;count=0;
		scanf("%d",&n1);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			scanf("%d",&a[i][j]);
		}
		scanf("%d",&n2);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				scanf("%d",&b[i][j]);
			}
		}
		k=0;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
		//	printf("kk\n");
				if(a[n1][i]==b[n2][j])
				{
					count++;
					temp[k]=a[n1][i];
					//printf("%dhh\n",a[n1][i]);
				}
			}
		}
		if(count==0)
		{
			
			printf("case #%d: Volunteer cheated!\n",coun);
		}
		else if(count==1)
		{
			printf("Case #%d: %d\n",coun,temp[0]);
		}
		else
		{
			printf("Case #%d: Bad magician!\n",coun);
		}
	}
	return 0;
}
