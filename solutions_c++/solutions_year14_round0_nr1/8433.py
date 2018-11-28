#include<stdio.h>

int main()
{
	int cases;
	int k=0;
	
	scanf("%d",&cases);
	
	while(cases--)
	{
		int ans,ans1,ans2;
	    int arr1[4][4] = {0};
	    int arr2[4][4] = {0};
	    int i = 0;
		int j = 0;
		int check = 0;
		
		scanf("%d",&ans1);
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&arr1[i][j]);
			}
		}
		
		scanf("%d",&ans2);
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&arr2[i][j]);
			}
		}
		
		for(i=0;i<4;i++)
		{
			
			for(j=0;j<4;j++)
			{
				if(arr1[ans1 - 1][i] == arr2[ans2 - 1][j])
				{
					check++;
					if(check == 1)
					{
						ans = arr1[ans1 - 1][i];
					}
					
				    else if(check > 1)
				    {
					    break;
				    }
				}
				
			}
			if(check > 1)
			{
				k++;
				printf("Case #%d: Bad magician!",k);
				break;
			}
			
		}
		
		if(check == 1)
		{
			k++;
			printf("case #%d: %d",k,ans);
		}
		
		else if(check == 0)
		{
			k++;
			printf("case #%d: Volunteer cheated!",k);
		}
		
		printf("\n");
	}
	
	return 0;
}
