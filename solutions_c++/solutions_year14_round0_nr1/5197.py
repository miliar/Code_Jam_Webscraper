#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	int test,row1,i,num,flag,ind,j;
	scanf("%d",&test);
	for(j=0;j<test;j++)
	{
		flag=0;
		int* arrayMain = new int[17] ();
		scanf("%d",&row1);
		for(i=0;i<16;i++)
		{
			if(row1==((i/4)+1))
			{
				scanf("%d",&num);
				arrayMain[num]++;
			}
			else
				scanf("%d",&num);
		}
		scanf("%d",&row1);
		for(i=0;i<16;i++)
		{
			if(row1==((i/4)+1))
			{
				scanf("%d",&num);
				if(arrayMain[num]==1)
				{
					flag++;
					ind=num;
				}
			}
			else
				scanf("%d",&num);
		}
		switch(flag)
		{
			case 0:printf("Case #%d: Volunteer cheated!\n",j+1);
				break;
			case 1:printf("Case #%d: %d\n",j+1,ind);
				break;
			default:printf("Case #%d: Bad magician!\n",j+1);
		}
		delete arrayMain;
	}
	return 0;
}