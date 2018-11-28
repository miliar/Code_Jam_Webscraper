#include<iostream>
#include<fstream>

int first[4][4],second[4][4];

int main()
{
int t,ans1,ans2,count,num;
scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
	
		num=count=0;
		
		scanf("%d",&ans1);
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		scanf("%d",&first[i][j]);
		scanf("%d",&ans2);
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		scanf("%d",&second[i][j]);
		
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		//printf("%d %d\n",first[ans1-1][q],second[ans2-1][z]);
		if(first[ans1-1][i] == second[ans2-1][j])
		{
		num=first[ans1-1][i];
		count++;
		}
		
		if(count == 1)
		printf("Case #%d: %d\n",tc,num);
		else if(count > 1)
		printf("Case #%d: Bad magician!\n",tc);
		else
		printf("Case #%d: Volunteer cheated!\n",tc);
		
		
	}


return 0;
}