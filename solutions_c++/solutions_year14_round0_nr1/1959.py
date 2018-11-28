#include<stdio.h>

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,a,b,arr1[4][4],arr2[4][4];
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		scanf("%d",&a);
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				scanf("%d",&arr1[j][k]);
			}
		}
		scanf("%d",&b);
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				scanf("%d",&arr2[j][k]);
			}
		}

		int count=0;

		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(arr1[a-1][j]==arr2[b-1][k])
				{
					count++;
				}
			}
		}
		if(count==0)
		{
			printf("Case #%d: Volunteer cheated!\n",i+1);
		}
		else if(count==1)
		{
			int cari;
			for(int j=0;j<4;j++)
			{
				for(int k=0;k<4;k++)
				{
					if(arr1[a-1][j]==arr2[b-1][k])
					{
						cari=arr1[a-1][j];
					}
				}
			}
			printf("Case #%d: %d\n",i+1,cari);
		}
		else
		{
			printf("Case #%d: Bad magician!\n",i+1);
		}
	}
	return 0;
}