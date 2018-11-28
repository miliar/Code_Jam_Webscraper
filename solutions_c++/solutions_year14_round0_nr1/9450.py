#include <stdio.h>

int main() {
	int t,grid1[4][4],grid2[4][4],choosen,ans1,ans2,i,j,count,k;
	scanf("%d",&t);
	for(k=1; k<=t; k++)
	{
		count = 0;
		scanf("%d",&ans1);
		for(i=0; i<4; i++)
			for(j=0; j<4; j++)
				scanf("%d",&grid1[i][j]);
		scanf("%d",&ans2);
		for(i=0; i<4; i++)
			for(j=0; j<4; j++)
				scanf("%d",&grid2[i][j]);
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				if(grid1[ans1-1][i] == grid2[ans2-1][j])
				{
					count++;
					if(count == 1)
						choosen = grid1[ans1-1][i];
					else if(count >1)
						break;
				}
			}
		}
		if(count == 1)
			printf("Case #%d: %d\n",k,choosen);
		else if(count > 1)
			printf("Case #%d: Bad magician!\n",k);
		else if(count == 0)
			printf("Case #%d: Volunteer cheated!\n",k);
	}
	return 0;
}