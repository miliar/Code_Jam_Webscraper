#include <stdio.h>
#include <string.h>

int hash[20];

int main()
{
	int ans, card[10], tmp, counter = 0, resp, casos;
	
	scanf("%d", &casos);
	for(int w = 0; w < casos; w++)
	{
		scanf("%d", &ans);
		for(int i = 0; i < 4; i++)
		{
			scanf("%d %d %d %d", &card[0], &card[1], &card[2], &card[3]);
			if(i == (ans - 1))
				for(int j = 0; j < 4; j++)
					hash[card[j]] = 1;
			
		}
	
		scanf("%d", &ans);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
			{
				scanf("%d", &tmp);
				if(i == (ans - 1) && hash[tmp] == 1)
				{
					counter++;
					if(counter == 1)
						resp = tmp;
				}
			 
			}
			
		
		
		
		printf("Case #%d: ", w + 1);
		if(counter > 1)
			printf("Bad magician!");
		else if(counter < 1)
			printf("Volunteer cheated!");
		else
			printf("%d", resp);
		printf("\n");
		
		memset(hash, 0, sizeof(hash));
		counter = 0;	
	}
			
		return 0; 

}
