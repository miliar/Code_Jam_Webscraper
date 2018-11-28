#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define SWAP(a,b) ((a)^=(b)^=(a)^=(b));

int main(void)
{
	FILE *input, *output;
	int size,flag=0;
	unsigned long long int top;
	unsigned long long int bot;
	unsigned long long int rooted;
	unsigned long long int low=1;
	unsigned long long int high=10000001;
	unsigned long long int sq;
	int temp1, temp2;
	char strtemp[1000];
	unsigned long long int *can;
	int count = 0;
	int len;
	unsigned long long int bot1, top1;

	can = (unsigned long long int *)malloc(sizeof(unsigned long long int)*high);


	if((input = fopen("C-large-1.in", "rt")) == NULL)
	{
		printf("input fopen err\n");
		return 0;
	}

	if((output = fopen("C-large-1.out", "wt")) == NULL)
	{
		printf("output fopen err\n");
		return 0;
	}

	fscanf(input,"%d",&size);

	int i = 0;

	for(unsigned long long int i = 1 ; i <= high ; i++ )
	{
		flag = 0;
		memset(strtemp, 0 , sizeof(char)*1000);
		itoa(i, strtemp, 10);
		len = strlen(strtemp);

		for( unsigned long long int k = 0 ; k < (int)len/2 ; k++ )
		{
			if(strtemp[k] != strtemp[len-k-1])
			{
				flag = -1;
				break;
			}
		}

		if(flag == -1) continue;
		memset(strtemp, 0 , sizeof(char)*1000);

		sq = i*i;
		sprintf(strtemp, "%llu",sq);

		len = strlen(strtemp);

		for( unsigned long long int k = 0 ; k < (int)len/2 ; k++ )
		{
			if(strtemp[k] != strtemp[len-k-1])
			{
				flag = -1;
				break;
			}
		}

		if(flag != -1)
			can[count++] = sq;
	}

	for(int i=0 ; i < size ; i++) 
	{
		int flagg = 0;
		int max, min;
		fscanf(input,"%llu %llu",&bot, &top);
		for(max = 0 ; can[max] < bot ; max++);
		for(min = 0 ; can[min] <= top ; min++);
		count = min - max;
		fprintf(output, "Case #%d: %d\n", i+1, count);
	}
	return 0;
}