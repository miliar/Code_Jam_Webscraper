#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int test;
	FILE *fp = fopen("C:/Users/Mycom/Documents/Visual Studio 2013/Projects/pro/Debug/A-large.in", "r");
	FILE *fp2 = fopen("C:/Users/Mycom/Documents/Visual Studio 2013/Projects/pro/Debug/A-large.out", "w");
	if (fp == NULL)
		return 0;

	fscanf(fp, "%d", &test);

	for (int t = 1; t <= test; t++)
	{
		int num;
		fscanf(fp, "%d", &num);
		if (num == 0)
		{
			fprintf(fp2, "Case #%d: INSOMNIA\r\n", t);
			continue;
		}
		char s[20] = { 0, };
		
		int n = num;
		int idx[10] = { 0, };
		while (1)
		{
			sprintf(s, "%d", num);
			int len = strlen(s);
			int flag = 0;
			for (int i = 0; i < len; i++)
				idx[s[i] - '0'] = 1;
			
			for (int i = 0; i < 10; i++)
				if (!idx[i])
				{
					flag = 1;
					break;
				}
			if (flag)
			{
				num += n;
				continue;
			}
			else break;
		}
		fprintf(fp2, "Case #%d: %d\r\n", t, num);
	}
}