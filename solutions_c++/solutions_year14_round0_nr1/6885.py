#include<stdio.h>
#include<string.h>

int main()
{
	int T,cards[4][4],is_card[17],row,i,j,num,test,count;
	scanf("%d",&T);
	for(test=1;test<=T;test++)
	{
		count=0;
		memset(is_card,0,17*sizeof(int));
		scanf("%d",&row);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&cards[i][j]);
		for(i=0;i<4;i++)
			is_card[cards[row-1][i]]=1;
			
		scanf("%d",&row);
		
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&cards[i][j]);
				
		for(i=0;i<4;i++)
			if(is_card[cards[row-1][i]])
			{
				count++;
				num=cards[row-1][i];
			}
			
		switch(count)
		{
			case 0:
					printf("Case #%d: Volunteer cheated!\n",test);
					break;
			case 1:
					printf("Case #%d: %d\n",test,num);
					break;
			case 2:
			case 3:
			case 4: 
					printf("Case #%d: Bad magician!\n",test);
		}
	}
 return 0;
}
			
