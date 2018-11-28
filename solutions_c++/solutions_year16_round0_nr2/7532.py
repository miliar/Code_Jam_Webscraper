#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int res(char *input)
{
	int max = strlen(input);
	int stack[max];
	int count = 0;
	int result = 0;

	for(int i = 0 ; i < max ; i++)
	{
		if(input[i] == '-')	stack[i] = 0;
		else stack[i] = 1;
	}

	while(1)
	{
		count = 0;
		for(int i = 0 ; i <= max ; i++)
		{
			if(stack[i] == 1) count++;
		}
		if(count == max)
		{
			return result;
		}
		//////////////////////////////
		count = 0;
		if(stack[0] == 0)
		{
			for(int j = 0; j < max ; j++)
			{
				if(stack[j] == 1)
				{
					break;
				}
				stack[j] = 1;
			}
			result++;
		}
		////////////////////////////////
		for(int i = 0 ; i < max ; i++)
		{
			if(stack[i] == 1)
			{
				count++;
			}
		}
		if(count == max)
		{
			return result;
		}
		//////////////////////////////////
		if(stack[0] == 1)
		{
			for(int j = 0; j < max ; j++)
			{
				if(stack[j] == 0)
				{
					break;
				}
				stack[j] = 0;
			}
			result++;
		}
	}
}

int main()
{
/*	char in[100];
	while(1){
		scanf("%s",in);
		printf("%d\n",res(in));
	}
*/	
	FILE *fp1;
	FILE *fp2;

	int i;
	int cnt = 1;
	char buffer[256];

	fp1 = fopen("B-large.in","r");
	fp2 = fopen("B-large.out","w");

	while(1)
	{
		fgets(buffer,255,fp1);
		if(feof(fp1))
		{
			break;
		}

		for(i = 0; i < strlen(buffer); i++)
		{
			if(buffer[i] =='\n')
				buffer[i] = '\0';
		}

		fprintf(fp2,"Case #%d: %d\n",cnt++,res(buffer));
	}
	fclose(fp1);
	fclose(fp2);
}
