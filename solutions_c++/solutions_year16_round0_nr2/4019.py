#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int test;
	FILE *fp = fopen("C:/Users/Mycom/Documents/Visual Studio 2013/Projects/pro/Debug/B-large.in", "r");
	FILE *fp2 = fopen("C:/Users/Mycom/Documents/Visual Studio 2013/Projects/pro/Debug/B-large.out", "w");
	fscanf(fp, "%d", &test);

	for (int t = 1; t <= test; t++)
	{
		char cake[105] = { 0, };
		fscanf(fp, "%s", cake);
		int eIdx = 0;
		int cnt = 0;
		
		int len = strlen(cake);
		if (len == 1)
		{
			if (cake[0] == '-')
				fprintf(fp2, "Case #%d: %d\n", t, 1);
			else
				fprintf(fp2, "Case #%d: %d\n", t, 0);

			continue;
		}
		while (1)
		{
			int flag = 0;
			for (int i = 0; i < len; i++)
			{
				if ((cake[i] == '-' && cake[i + 1] == '+') ||
					(cake[i] == '-' && cake[i+1] == '\0'))
				{
					flag = 1;
					eIdx = i;
					break;
				}
			}
			if (flag)
			{
				for (int i = 0; i <= eIdx; i++)
				{
					if (cake[i] == '-')
						cake[i] = '+';
					else if (cake[i] == '+')
						cake[i] = '-';
				}
			}
			else
			{
				fprintf(fp2, "Case #%d: %d\n", t, cnt);
				break;
			}
			cnt++;
		}
	}
}