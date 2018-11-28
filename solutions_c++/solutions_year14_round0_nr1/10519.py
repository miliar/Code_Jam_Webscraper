#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i,j,k,t;
	scanf("%d",&t);
	for(i=1;i<=t;++i)
	{
		int m;
		int arr[4][4];
		scanf("%d",&m);
		for(j=0;j<4;++j)
		{
			for(k=0;k<4;++k)
			scanf("%d",&arr[j][k]);
		}
		
		int set1[4];
		for(j=0;j<4;++j)
		set1[j] = arr[m-1][j];
		
		scanf("%d",&m);
		for(j=0;j<4;++j)
		{
			for(k=0;k<4;++k)
			scanf("%d",&arr[j][k]);
		}
		
		int set2[4];
		for(j=0;j<4;++j)
		set2[j] = arr[m-1][j];
		
		int count = 0, card;
		for(j=0;j<4;++j)
		{
			for(k=0;k<4;++k)
			{
				if(set1[j] == set2[k])
				{
					count++;
					card = set1[j];
				}
			}
		}
		
		
		if(count == 1)
			printf("Case #%d: %d\n", i, card);
		else if(count > 1)
			printf("Case #%d: Bad magician!\n", i);
		else
			printf("Case #%d: Volunteer cheated!\n", i);
	}
	return 0;
}
