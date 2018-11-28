#include <stdio.h>

int main()
{
	int check[10] = {0,};
	int arr[20] = {-1,};
	int temp[20] = {-1,};
	int tmp;
	int i;
	int j;
	char value[20] = {0,};
	int c;
	FILE *fp = fopen("text.txt","r");
	int count;
	int check_count;
	
	
	for(i=0;i<=100;i++)
	{
		fscanf(fp,"%s\n",value);
		
		c = 1;
		
		for(j=0;j<10;j++)
		{
			check[j] = 0;		
		}
		while(1)
		{
			if(i==0)
				break;
			if(value[0] == '0')
			{
				printf("Case #%d: INSOMNIA\n",i);			
				break;
			}
		
			for(j=0;j<20;j++)
			{
				arr[j] = -1;
				temp[j] = -1;
				
			}
		
			count = 0;
			for(j=0;j<20;j++)
			{
				if(value[j]>='0' && value[j]<='9')
					count++;
				else
					break;
			}
			
			for(j=0;j<20;j++)
			{
				if(value[j]>='0' && value[j]<='9')
					arr[count-1] = value[j] - '0';
					
				count--;  
			}
			
			for(j=0;j<20;j++)
			{
				if(arr[j] != -1)
					temp[j] = arr[j]*c;
			}
			
			for(j=0;j<20;j++)
			{
				if(temp[j]>9)
				{
					tmp = temp[j];
					temp[j] = tmp%10;
					if(temp[j+1] != -1)
						temp[j+1] += tmp/10;
					else
						temp[j+1] = tmp/10;
				}
			}
			
			for(j=19;j>=0;j--)
			{
				check[temp[j]] = 1;
			}
			check_count = 0;
			for(j=0;j<10;j++)
			{
				if(check[j] == 1)
					check_count++;
					
			}
			
			if(check_count == 10)
			{
				
				printf("Case #%d: ",i);
				for(j=19;j>=0;j--)
				{
					if(temp[j] != -1)
					printf("%d",temp[j]);
				}
				printf("\n");
				break;
			}
			c++;
		}
		
	}
	
	
	
}
