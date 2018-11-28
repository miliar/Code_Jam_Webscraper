#include <cstdio>

int main()
{
	freopen("in1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	
	int magician[4][4];
	int volunteer[4][4];
	
	
	int testCase,rowNumberBefore,rowNumberAfter,answer = 0, totalAnswer = 0;;
	
	scanf("%d",&testCase);
	for(int test = 1; test <= testCase; test++)
	{
		scanf("%d",&rowNumberBefore);
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				scanf("%d",&magician[i][j]);
			}
			
		}
		
		scanf("%d",&rowNumberAfter);
		
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				scanf("%d",&volunteer[i][j]);
			}
			
		}
		
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(magician[rowNumberBefore-1][i] == volunteer[rowNumberAfter-1][j]){
					
					if(totalAnswer==0)
					{
						answer = magician[rowNumberBefore-1][i];
					}
					totalAnswer++;
				}
			}
			
		}
		
		if(totalAnswer==1){
			printf("Case #%d: %d",test,answer);
		}
		else if(totalAnswer == 0){
			printf("Case #%d: Volunteer cheated!",test);
		}
		else{
			printf("Case #%d: Bad magician!",test);
		}
		printf("\n");
		totalAnswer = 0;
		answer = 0;
	}
	
}
