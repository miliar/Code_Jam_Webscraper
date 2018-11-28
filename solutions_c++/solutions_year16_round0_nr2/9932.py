#include <stdio.h>

int main()
{
	FILE *fp;
	char str[101] = {0,};
	char tmp;
	int i;
	int j;
	int count;
	int check;
	int num;
	int c_count;
	
	fp = fopen("text.txt","r");
	
	for(i=0;i<=100;i++)
	{
		fscanf(fp,"%s\n",str);
		
		
		c_count = 0;
		while(1)
		{
			if(i==0)
				break;
			num = 0;
			count = 0;

			for(j=0;j<100;j++)
			{
				if(str[j] == '-')
					count++;
					
				if(str[j] != '-' && str[j] != '+')
					break;
				num++;
			}
			
			if(count == 0)
			{

				printf("Case #%d: %d\n",i, c_count);			
				break;
			}
			
			if(num == 1)
			{
				if(str[0] == '-')
					str[0] = '+';
			}
			else if(num == count)
			{ 
				for(j=0;j<100;j++)
				{
					if(str[j]=='-')
						str[j] = '+';
				}
			}
			else 
			{
			
				check = 1;
				for(j=0;j<100;j++)
				{
					if(str[j] == '-' && str[j+1] =='+' ||str[j] == '+' && str[j+1] =='-')
					{
						break;
					}
					check++;
				}
			
				if(str[check] == '-')
				{
					for(j=0;j<check;j++)
							str[j] = '-';
						
				}
				else if(str[check] == '+')
				{
					for(j=0;j<check;j++)
						str[j] = '+';	
				}
			
			}
			c_count++;
		}

		
	}
	
	
	
}
