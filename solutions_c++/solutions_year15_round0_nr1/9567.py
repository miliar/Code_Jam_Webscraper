#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_COLS 1200
#define MAX_ROWS 100

int Friend_cal(char Shyness_input[MAX_COLS]);

int main()
{
		FILE *in;
		FILE *out;
		char s[MAX_COLS];
		int Invited_Friend[MAX_ROWS];
		int row;
		
		if((in = fopen("example.txt", "rt")) == NULL){
			fputs("Cannot open input file...\n", stderr);
		}
		
		out = fopen("result_A.txt", "w");
		
		while(fgets(s, MAX_COLS+1, in)!= NULL){
		
		if(row==0)
		{
		}
		else
		{
			Invited_Friend[row] = Friend_cal(s);
			fprintf(out, "Case #%d: %d\n", row, Invited_Friend[row]);
			printf("%d\r\n",row);
		}
			
		printf(s);
		printf("\n");				
		
		row++;
		
		}
		
		fclose(in);
		return 0;
}

int Friend_cal(char Shyness_input[MAX_COLS])
{
	int Shyness_max=0;
	int max_cal[4]={0,0,0,0};
	int Shyness_sum=0;
	int temp_sum=0;
	int Need_People=0;
	int temp_need=0;
	
	int index=0;
	int s_index=0;
	int m_index=0;
	
	int i=0;
	int flag=1;
		
	if(Shyness_input[0]=='0')
	{
	//	printf("End of function\n");
		return Need_People;	
	}
	
	/* Extract the max Shyness*/
	
	while(Shyness_input[index]!=' ')
	{
		max_cal[index]=Shyness_input[index]-'0';
		index++;
	}
	
	switch(index)
	{
		case 1:
			Shyness_max = max_cal[0];
			break;
		case 2:
			Shyness_max = max_cal[0] * 10 + max_cal[1];
			break;
		case 3:
			Shyness_max = max_cal[0] * 100 + max_cal[1] * 10 + max_cal[2];
			break;
		case 4:
			Shyness_max = max_cal[0] * 1000 + max_cal[1] * 100 + max_cal[2] * 10 + max_cal[3];
			break;
	}
	
	/* Start function */
	//printf("Shyness_max = %d\n", Shyness_max);
	index++;
	s_index = index;
	
//	printf("index : %d\n", index);
	/*
	while(1)
	{
		if(flag==1)
		{
			Shyness_sum = Shyness_input[index]-'0';
			flag=0;
		}
		else
		{
			if((Shyness_sum - i + 1) >= 0)
			{
				index = index + Shyness_sum;
				if(index > (s_index + Shyness_max))
				{
					index = s_index + Shyness_max;
				}
				printf("index: %d\n", index);
			}
			else
			{
				Need_People += (i - Shyness_sum - 1);
				Shyness_sum += Need_People;
				printf("Need_people : %d\n", Need_People);
			}
		}
		
		if(Shyness_max <= Shyness_sum)				
		{
			break;
		}
		
		temp_sum = Shyness_sum;
		m_index=Shyness_sum+index;
		
		if(m_index >(s_index + Shyness_max))
		{
			m_index = s_index + Shyness_max;
		}
		
		for(i=index;i<m_index;i++)
		{
			temp_sum += (Shyness_input[i]-'0');
			printf("Sum : %d, Index : %d, Input : %d\n", temp_sum, i, (Shyness_input[i]-'0'));
		}
		i = i - 1;
		Shyness_sum = temp_sum;
		
		if(Shyness_sum==0)
		{
			Need_People=1;
			Shyness_sum=1;
		}
		
		printf("Cal : %d\n", Shyness_sum - i + 1);
				
		if(Shyness_max <= Shyness_sum)				
		{
			break;
		}

	}*/
		Shyness_sum = (Shyness_input[index]-'0');
		i=index++;
		while(Shyness_input[i]!='\n')
		{
			i++;
			if(Shyness_input[i]!='0')
			{
			if(Shyness_sum < i-s_index)
			{
				temp_need = ((i-s_index)-Shyness_sum);
				Need_People+=temp_need;
				Shyness_sum+=temp_need;
				//printf("Need People = %d\n", Need_People);
			}
			}
			if((Shyness_sum > Shyness_max))// || (i==Shyness_max+1))
			{
				break;
			}
			
			Shyness_sum += (Shyness_input[i]-'0');
			
			//printf("Sum : %d, Index : %d, Input : %d\n", Shyness_sum, i-s_index, (Shyness_input[i]-'0'));
		}
		
	return Need_People;
}
