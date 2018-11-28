#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int t;
	int arr1[5][5];
	int arr2[5][5];
	
	int x,y;
	int v;
	int a1,a2;
	
	scanf("%d",&t);
	int count;
	int num;
	for(v=1;v<=t;v++)
	{
		scanf("%d",&a1);
		for(x=1;x<=4;x++)
		{
			for(y=1;y<=4;y++)
			{
				scanf("%d",&arr1[x][y]);
			}
		}
		
		scanf("%d",&a2);
		
		for(x=1;x<=4;x++)
		{
			for(y=1;y<=4;y++)
			{
				scanf("%d",&arr2[x][y]);
			}
		}
		count=0;
		num=0;
		
		for(x=1;x<=4;x++)
		{
			for(y=1;y<=4;y++)
			{
				if(arr1[a1][x] == arr2[a2][y])
				{
					count++;
					num = arr1[a1][x];
				}
			}
		}
		
		if(count==1)
		{
			printf("Case #%d: %d\n",v,num);
		}
		else if(count==0)
		{
			printf("Case #%d: Volunteer cheated!\n",v);
		}
		else if(count>1)
		{
			printf("Case #%d: Bad magician!\n",v);
		}
	}
	return 0;
}