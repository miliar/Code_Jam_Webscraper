#include <stdio.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
	int t;int ans1,ans2;bool arr[16];
	for(int v=0;v<16;v++)
		arr[v]=false;
	scanf("%d",&t);int neg=0;
	for(int jk=0;jk<t;jk++)
	{
		
		for(int v=0;v<16;v++)
		arr[v]=false;
		scanf("%d",&ans1);
		for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
					{
						scanf("%d",&neg);
						if(i+1==ans1)
							arr[neg-1]=true;
					}
			}
		int g=0;
		scanf("%d",&ans2);int b[4];
		for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
					{
						scanf("%d",&g);
						if(i+1==ans2)
						{
							b[j]=g;
						}
					}
			}
		int count=0;int cv;
		for(int o=0;o<4;o++)
		{
			if(arr[b[o]-1]==true)
				{count++;cv=b[o];}

		}
		if(count>1)
				{printf("Case #%d",(jk+1));
					printf(": Bad magician!\n");
			}
		else if(count==1)
			{printf("Case #%d",(jk+1));
				printf(": %d\n",cv);}
		else if(count==0)
			{printf("Case #%d",(jk+1));
					printf(": Volunteer Cheated!\n");
			}
	}
	return 0;
}
