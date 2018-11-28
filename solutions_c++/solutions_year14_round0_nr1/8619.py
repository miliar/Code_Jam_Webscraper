#include <stdio.h>

int main()
{
	int times;
	scanf("%d", &times);
	
	for(int tm = 1; tm <= times; tm++)
	{
		int a;
		scanf("%d", &a);
		
		int flag = 0, thatnumber = 0, numbercount = 0;
		
		int array1[5][5];
		
		for(int k = 0; k < 4 ; k++)
		{
			for(int j = 0; j < 4; j++)
			{
				scanf("%d", &array1[k][j]);
			}
		}
		
		int b;
		scanf("%d", &b);
		
		int array2[5][5];
		
		for(int k = 0; k < 4 ; k++)
		{
			for(int j = 0; j < 4; j++)
			{
				scanf("%d", &array2[k][j]);
			}
		}
		
		for(int z = 0; z < 4; z++)
		{
			for (int y = 0; y < 4 ; y++)
			{
				if(array1[a-1][z] == array2[b-1][y])
				{
					flag = 1;
					thatnumber = array1[a-1][z];
					numbercount++;
				}
			}
		}
	
		if((flag == 1) && (numbercount == 1))
		{
			printf("Case #%d: %d\n", tm, thatnumber);
		}
		
		else if((flag == 1)) 
		{
			printf("Case #%d: Bad magician!\n", tm);
		}
		
		else
		{
				printf("Case #%d: Volunteer cheated!\n", tm);
		}
		
		
	}
	return 0;
	
}
