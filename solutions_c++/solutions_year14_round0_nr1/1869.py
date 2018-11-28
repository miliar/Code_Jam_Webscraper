#include<stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main() 
{ 

#ifdef FILEIO
	freopen("in.txt","r",stdin); 
	freopen("out.txt","w",stdout); 
#endif

#define SIZE 17
	int T;
	int guessNumberOne;
	int guessNumberTwo;
	int card[4][4];
	int chooseCard[SIZE];

	int resultNumber;
	int result[4];

	int i,j,k;//for loop

	scanf("%d",&T);

	for(i=0;i<T;i++)
	{
		memset(chooseCard,0,SIZE*sizeof(int));
		memset(card,0,sizeof(int)*16);
		memset(result,0,sizeof(int)*4);
		resultNumber = 0;
		scanf("%d",&guessNumberOne);

		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
			{
				scanf("%d",&card[j][k]);
			}
		
		for(k=0;k<4;k++)
		{
			chooseCard[card[guessNumberOne-1][k]] = 1;
		}

		memset(card,0,sizeof(int)*16);
		scanf("%d",&guessNumberTwo);

		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
			{
				scanf("%d",&card[j][k]);
			}
		
		for(k=0;k<4;k++)
		{
			if(chooseCard[card[guessNumberTwo-1][k]] == 1)
			{
				resultNumber++;
				result[resultNumber-1] = card[guessNumberTwo-1][k];
			}
		}

		if(resultNumber == 1)
		{
			//Case #1: 7
			printf("Case #%d: %d\n",(i+1),result[resultNumber-1]);
		}
		else if(resultNumber > 1)
		{
			//Case #2: Bad magician!
			printf("Case #%d: Bad magician!\n",(i+1));
		}
		else if (resultNumber == 0)
		{
			//Case #3: Volunteer cheated!
			printf("Case #%d: Volunteer cheated!\n",(i+1));
		}
	}
	

#ifdef FILEIO
	fclose(stdin);
	fclose(stdout);
#endif  

	return 0; 
}
