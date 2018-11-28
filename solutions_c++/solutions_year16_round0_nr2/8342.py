#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TEST_CASE_MAX		100
#define DATA_SET_MAX		102
#define INPUT_FILENAME  	"B-large.in"
#define OUTPUT_FILENAME  	"B-large.out"

int algo(char *data)
{
	int i = 0;
	char target[1] = {'-'};	
	int result = 0;
	
	for (i = strlen(data); i >=0; i--)
	{			
		if (data[i] == target[0])
		{
			if ('-' == target[0])
				target[0] = '+';
			else
				target[0] = '-';
			result++;
		}
	}	
	return result;
}

int main()
{
	FILE *fp = fopen(INPUT_FILENAME, "r");
	FILE *output = fopen(OUTPUT_FILENAME, "w");
	int testCase = 0;
	int i = 0;
	int result = 0;
	char *data[TEST_CASE_MAX];
	char buffer[DATA_SET_MAX];
	memset(buffer, '\0', sizeof(buffer));		
	
	if (NULL == fp)
	{
		perror("NULL");
		return -1;
	}
	
	if (NULL != fgets(buffer, sizeof(buffer), fp))
		testCase = atoi(buffer);	
	
	for (i = 0; i < TEST_CASE_MAX; i++)
	{
		data[i] = (char *) malloc(DATA_SET_MAX);
		memset(data[i], '\0', sizeof(data[i]));
	}	
	
	for (i = 0; i < testCase; i++)
	{
		if (NULL != fgets(buffer, sizeof(buffer), fp))
		{
			memcpy((char *)data[i], buffer, strlen(buffer));
			//printf("%s\n", data[i]);
		}
	}	
	fclose(fp);
	
	for (i = 0; i < testCase; i++)
	{
		result = algo(data[i]);		
		printf("Case #%d: %d\n", i+1, result);
		fprintf(output, "Case #%d: %d\n", i+1, result);
	}
	fclose(output);
			
	return 0;
}
