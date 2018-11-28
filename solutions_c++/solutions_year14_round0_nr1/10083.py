#include <bits/stdc++.h>
int main()
{
	int t,n1,n2,i,j,k,temp,count,ans;
	int arr1[4], arr2[4];
	scanf("%d",&t);
	for (i = 0; i < t; i++)
	{
		scanf("%d",&n1);
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&temp);
				if (j == n1 -1)
				{
					arr1[k] = temp;
				}
			}
		}
		scanf("%d",&n2);
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&temp);
				if (j == n2 -1)
				{
					arr2[k] = temp;
				}
			}
		}
		count = 0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if (arr1[j] == arr2[k])
				{
					count++;
					ans = arr1[j];
				}
			}
		}
		if(count == 0)
		{
			printf("Case #%d: Volunteer cheated!\n",i+1);
		}
		else if(count == 1)
		{
			printf("Case #%d: %d\n",i+1,ans);
		}
		else
		{
			printf("Case #%d: Bad magician!\n",i+1);
		}
	}
	return 0;
}