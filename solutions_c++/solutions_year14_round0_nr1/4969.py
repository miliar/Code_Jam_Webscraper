#include<stdio.h>
#include<string.h>
int main()
{
	int t;
	scanf("%d",&t);
	int x=1;
	while(t--)
	{
		int n;
		scanf("%d",&n);
		int arr[4][4];
		int i,j;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			scanf("%d",&arr[i][j]);
			}
		   int m;
		   scanf("%d",&m);
		   int arr1[4][4];
		   for(i=0;i<4;i++)
		   {
				for(j=0;j<4;j++)
				scanf("%d",&arr1[i][j]);
				}
				int arr2[4];
				arr2[0]=arr[n-1][0];
				arr2[1]=arr[n-1][1];
				arr2[2]=arr[n-1][2];
				arr2[3]=arr[n-1][3];
				
				int arr3[4];
					arr3[0]=arr1[m-1][0];
				arr3[1]=arr1[m-1][1];
				arr3[2]=arr1[m-1][2];
				arr3[3]=arr1[m-1][3];
				int count=0;
				for(i=0;i<4;i++)
				{for(j=0;j<4;j++)
				{
					if(arr2[i]==arr3[j])
					count++;}
					}
					if(count>1)
					printf("Case #%d: Bad magician!\n",x);
					else if(count==0)
					printf("Case #%d: Volunteer cheated!\n",x);
					else {int flag=0;
					for(i=0;i<4;i++)
				{for(j=0;j<4;j++)
				{if(arr2[i]==arr3[j])
				flag=1;
				if(flag)
				break;
				}if(flag)
				break;}	
					printf("Case #%d: %d\n",x,arr2[i]);}
			x++;}
			
			return 0;
}
