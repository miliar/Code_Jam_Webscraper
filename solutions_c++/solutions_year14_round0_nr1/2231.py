#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int cases,test,i,j,k,arr[10],count,flag,ans1,ans2,temp,temp2,ans;
	scanf("%d",&cases);
	test = cases;
	while(cases)
	{
		scanf("%d",&ans1);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(i!=ans1)
					scanf("%d",&temp);
				else
					scanf("%d",&arr[j-1]);
			}
		}
		scanf("%d",&ans2);
		count = 0;
		flag = 0;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(i!=ans2)
					scanf("%d",&temp);
				else
				{
					scanf("%d",&temp2);	
					for(k=0;k<=3;k++)
					{
						if(arr[k]==temp2)
						{
							flag = 1;
							ans = temp2;
							count++;	
						}	
					}
				}		
				
			}
		}
		if(flag == 0)
			printf("Case #%d: Volunteer cheated!\n",test-cases+1);	
		else
		{
			if(count == 1)
				printf("Case #%d: %d\n",test-cases+1, ans);
			else
				printf("Case #2: Bad magician!\n");	
		}
		cases--;	
	}

return 0;
}
