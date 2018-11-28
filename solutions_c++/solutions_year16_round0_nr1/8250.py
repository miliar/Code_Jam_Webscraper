#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TEST_CASE_MAX		100
#define DATA_SET_MAX		102
#define MAX_BUF_SIZE        1024
#define MAx_ATTEMP			100
#define INPUT_FILENAME  	"A-large.in"
#define OUTPUT_FILENAME  	"A-large.out"

int getAsleep(int *data, int num)
{
	int i = 0;
	int result = 0;
	for (i = 0; i < 10; i++)
	{
		//printf("data[%d] = %d num = %d result = %d\n", i, data[i], num, result);
		
		if (0 == data[i])
		{
			result = 0;
			break;
		}
		result = 1;	
	}

	return result;
}

int algo(char *data)
{
	int i = 0, j = 0, k = 0;
	int number = atoi(data);
	int num = number;
	int index = 0;
	char tmpNum[MAX_BUF_SIZE];
	int result = 0;
	int checkList[10];
	memset(checkList, 0, sizeof(checkList));
	memset(tmpNum, 0, sizeof(tmpNum));
	
	if (0 == num)
		return result;
	for (i = 1; i <= MAx_ATTEMP; i++)
	{
		num = number * i;
		sprintf(tmpNum, "%d", num);
		for (j = 0; j < strlen(tmpNum); j++)
		{		
			index = tmpNum[j] - '0';
			//printf("index = %d\n", index);
			checkList[index] = 1;
			//printf("=====> %c", tmpNum[j]);
			//printf("-----> %d", checkList[j]);
		}
		result = getAsleep(checkList, num) * num;
		if (result > 0) break;
		//printf("\n");
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
	char buffer[MAX_BUF_SIZE];
	memset(buffer, '\0', sizeof(buffer));		
	
	if (NULL == fp)
	{
		perror("NULL");
		return -1;
	}
	
	if (NULL != fgets(buffer, sizeof(buffer), fp))
		testCase = atoi(buffer);	
		
	//printf("testCase=%d\n", testCase);
	
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
		if (result <= 0)
		{
			printf("Case #%d: INSOMNIA\n", i+1);
			fprintf(output, "Case #%d: INSOMNIA\n", i+1);
		}
		else
		{
			printf("Case #%d: %d\n", i+1, result);
			fprintf(output, "Case #%d: %d\n", i+1, result);	
		}
	}
	fclose(output);

	return 0;
}
