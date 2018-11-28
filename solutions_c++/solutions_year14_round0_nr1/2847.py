#include<iostream>
#include<cstdio>

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int t, row1, row2, i, j, counter = 1;
	int board1[4][4], board2[4][4];
	
	scanf("%d", &t);
	
	while(t--)
	{
		printf("Case #%d: ", counter++);
		
		scanf("%d", &row1);	
		for(i=0; i<4; i++)
			for(j=0; j<4; j++)
				scanf("%d",&board1[i][j]);
			
		scanf("%d", &row2);	
		for(i=0; i<4; i++)
			for(j=0; j<4; j++)
				scanf("%d",&board2[i][j]);
		
		int res, flag = 0;
		
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				if( board1[row1-1][i] == board2[row2-1][j])
				{
					res = board1[row1-1][i];
					flag++;
				}
			}
		}
		
		if(flag == 0)
			printf("Volunteer cheated!\n");
		else if(flag == 1)
			printf("%d\n", res);
		else
			printf("Bad magician!\n");				
	}
	
	
	return 0;
}
