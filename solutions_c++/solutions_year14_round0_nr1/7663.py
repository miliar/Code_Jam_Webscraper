#include<stdio.h>

int main()
{
	freopen("in.txt","r",stdin);
	freopen("a_out.txt","w",stdout);
	int arr1[5][5];
	int arr2[5][5];

	int cas,cc;
	int ans1,ans2;
	int count,output;
	int i,j;

	scanf("%d",&cas);

	for(cc=1;cc<=cas;cc++)
	{
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

		ans1--;
		ans2--;

		count=0;
		output=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				//printf("%d %d XXX ",arr1[ans1][i],arr2[ans2][j]);
				if(arr1[ans1][i]==arr2[ans2][j])
				{
					count++;
					output=arr1[ans1][i];
				}
			}
		}

		printf("Case #%d: ",cc);

		if(count==0)
		{
			printf("Volunteer cheated!");
		}else if(count==1)
		{
			printf("%d",output);
		}else
		{
			printf("Bad magician!");
		}

		printf("\n");
	}
}
