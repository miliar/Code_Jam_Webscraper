#include <stdio.h>
#include <string.h>

#define MAX 12

int isDone(int len, char pancakes[]);

int main(void)
{
	int testcase, index;
	FILE *in, *out;
	in = fopen("B-small-attempt0.in", "r");
	out = fopen("result_pancakes_small.out", "w");

	fscanf(in, "%d", &testcase);
	for(index = 0; index<testcase; index++)
	{
		int i, j;
		char pancakes[MAX];
		int len;
		int result = 0;

		fscanf(in, "%s", pancakes);
		len = strlen(pancakes);

		while(isDone(len, pancakes) == 0)
		{
			for(i=len-1; i>=0; i--)
			{
				if(pancakes[i] == '-')
					break;
			}
			for(j=i; j>=0; j--)
			{
				if(pancakes[j] == '+')
					pancakes[j] = '-';
				else
					pancakes[j] = '+';
			}
			result++;
		}

		fprintf(out, "Case #%d: %d\n", index+1, result);
	}
	return 0;
}

int isDone(int len, char pancakes[])
{
	int i;
	int flag = 1;

	for(i=0; i<len; i++)
	{
		if(pancakes[i] == '-')
			flag = 0;
	}

	return flag;
}