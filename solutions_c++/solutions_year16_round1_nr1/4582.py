#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TEST_CASE_MAX		2048
#define DATA_SET_MAX		2048
#define MAX_BUF_SIZE        2048
#define INPUT_FILENAME  	"A-small-attempt3.in"
#define OUTPUT_FILENAME  	"A-small-attempt3.out"

char* putToHead(char target, char *data, int length)
{
	int i = 0;
	char result[MAX_BUF_SIZE];
	char *final = NULL;
	memset(result, 0, sizeof(result));
	result[0] = target;
	for (i = 0; i < length; i++)
	{
		result[i+1] = data[i];
	}
	final = result;
	//printf("%s\n", result);

	return final;
}

char* putToEnd(char target, char *data, int length)
{
	int i = 0;
	char result[MAX_BUF_SIZE];
	char *final = NULL;
	memset(result, 0, sizeof(result));
	for (i = 0; i < length; i++)
	{
		result[i] = data[i];
	}
	result[i] = target;
	final = result;
	//printf("%s\n", result);

	return final;
}

char* algo(char *data)
{
	int i = 0, j = 0, k = 0;
	char tmpBuf[MAX_BUF_SIZE];
	char *result = NULL;
	char *final = NULL;
	char head = 'A';
	memset(tmpBuf, '\0', sizeof(tmpBuf));	
	
	for (i = 0; i < strlen(data)-1; i++)
	{
		if (0 == i)
		{
			memset(tmpBuf, '\0', sizeof(tmpBuf));
			tmpBuf[i] = data[i];
			head = data[i];
			//printf("%d tmpBuf = %s\n", i, tmpBuf);
		}
		else
		{
			if (data[i] >= head)
			{
				result = NULL;
				result = putToHead(data[i], tmpBuf, i);
				head = data[i];
			}
			else
			{
				result = NULL;
				result = putToEnd(data[i], tmpBuf, i);
			}
			memcpy(tmpBuf, result, strlen(result));
			//printf("%d tmpBuf = %s\n", i, tmpBuf);
		}
	}
	final = tmpBuf;

	return final;
}

int main()
{
	FILE *fp = fopen(INPUT_FILENAME, "r");
	FILE *output = fopen(OUTPUT_FILENAME, "w");
	int testCase = 0;
	int i = 0;
	char *result = NULL;
	int tmp_len = 0;
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
		memset(buffer, '\0', sizeof(buffer));
		if (NULL != fgets(buffer, sizeof(buffer), fp))
		{
			tmp_len = strlen(buffer);
			buffer[tmp_len-1]= '\n';
			memset(data[i], '\0', sizeof(data[i]));
			memcpy((char *)data[i], buffer, strlen(buffer));
			//printf("%d: %s", i, data[i]);
		}
	}	
	fclose(fp);
	
	for (i = 0; i < testCase; i++)
	{
		result = algo(data[i]);
		tmp_len = strlen(result);
		//printf("len = %d\n", tmp_len-1);
		buffer[tmp_len-1]= '\n';		
		//printf("Case #%d = %s\n", i+1, result);
		fprintf(output, "Case #%d: %s\n", i+1, result);	
	}
	fclose(output);

	return 0;
}
