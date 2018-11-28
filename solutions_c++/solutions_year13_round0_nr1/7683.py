#include<stdio.h>
#include<stdlib.h>

int main()
{
	freopen("A-large.in","r+",stdin);
	freopen("output.out","w+",stdout);
	int n;
	char ch;
	int xCount=0,x1Count=0,oCount=0,o1Count=0,dotCount=0;
	int xdCount=0,odCount=0,xd1Count=0,od1Count=0;
	int solved=0;
	char arr[4][4];
	scanf("%d",&n);
	scanf("%c",&ch);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				scanf("%c",&ch);
				arr[j][k]=ch;
			}
			scanf("%c",&ch);
		}
		scanf("%c",&ch);

		printf("Case #%d: ",i+1);
		solved=0;dotCount=0;xdCount=0;odCount=0;xd1Count=0;od1Count=0;
		for(int j=0;j<4;j++)
		{
			xCount=0;oCount=0;x1Count=0;o1Count=0;		
			for(int k=0;k<4;k++)
			{
				switch(arr[j][k])
				{
					case 'X': xCount++; oCount=0;
					break;
					case 'O': oCount++; xCount=0;
					break;
					case '.': dotCount++;
					break;
					case 'T': xCount++; oCount++;
					break;
				}

				switch(arr[k][j])
				{
					case 'X': x1Count++; o1Count=0;
					break;
					case 'O': o1Count++; x1Count=0;
					break;
					case 'T': x1Count++; o1Count++;
					break;
				}
				
				if(k==j)
				{
					switch(arr[k][j])
					{
						case 'X': xdCount++; odCount=0;
						break;
						case 'O': odCount++; xdCount=0;
						break;
						case 'T': xdCount++; odCount++;
						break;
					}
				}
				if(k+j==3)
				{
					switch(arr[k][j])
					{
						case 'X': xd1Count++; od1Count=0;
						break;
						case 'O': od1Count++; xd1Count=0;
						break;
						case 'T': xd1Count++; od1Count++;
						break;
					}
				}							
			}
			
			if(xCount==4)
			{
				printf("X won\n");
				solved=1;
				break;	
			}
			else if(oCount==4)
			{
				printf("O won\n");
				solved=1;
				break;
			}
			else if(x1Count==4)
			{
				printf("X won\n");
				solved=1;
				break;
			}
			else if(o1Count==4)
			{
				printf("O won\n");
				solved=1;
				break;
			}
			
		}
		if(!solved)
		{
			if(xdCount==4)
				printf("X won\n");
			else if(odCount==4)
				printf("O won\n");
			else if(xd1Count==4)
				printf("X won\n");
			else if(od1Count==4)
				printf("O won\n");	
			else if(dotCount==0)
				printf("Draw\n");	
			else
				printf("Game has not completed\n");
		}
		
	}
}
	
