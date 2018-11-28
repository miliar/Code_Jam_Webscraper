#include <stdio.h>

int main()
{
	int testCases,firstRow,secondRow;
	scanf("%d",&testCases);
	int array[4][4];
	int sarray[4][4];
	int i,j,count[testCases],element[testCases];
	int t=0;
	while(t!=testCases)
	{
		count[t]=0;
		scanf("%d",&firstRow);
		for(i=0;i<4;i++)
		{
			scanf("%d %d %d %d",&array[i][0],&array[i][1],&array[i][2],&array[i][3]);
		}
		scanf("%d",&secondRow);
		for(i=0;i<4;i++)
		{
			scanf("%d %d %d %d",&sarray[i][0],&sarray[i][1],&sarray[i][2],&sarray[i][3]);
		}

		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(array[firstRow-1][i]==sarray[secondRow-1][j])
				{
					count[t]++;
					element[t]=array[firstRow-1][i];
				}
			}
		}
		t++;
	}
	for(i=0;i<testCases;i++)
	{
		if(count[i]==0)
			printf("Case #%d: Volunteer cheated!\n",i+1);
		else if(count[i]==1)
			printf("Case #%d: %d\n",i+1,element[i]);
		else 
			printf("Case #%d: Bad magician!\n",i+1);
	}
}