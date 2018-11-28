#include <stdio.h>
#include <string.h>

int t;
char arr[1001];

int main(void)
{
	FILE *ou = fopen("output.txt", "w");
	int i;
	int count = 0;
	scanf("%d", &t);
	for (int k = 1; k <= t; k++)
	{
		count = 0;
		memset(arr, 0, sizeof(arr));
		scanf("%s", arr);
		while (1)
		{
			int sw = 1;
			char temp = 0;
			for (i = 0; i < strlen(arr); i++)
			{
				if (arr[i] == '-')
				{
					sw = 0;
					break;
				}
			}
			if (sw == 1)
				break;
			count++;
			for (i = strlen(arr) - 1; i >= 0; i--)
			{
				if (arr[i] == '-' && sw == 0)
					sw = 1;
				if (sw == 1)
				{
					if (arr[i] == '-') arr[i] = '+';
					else arr[i] = '-';
				}
			}
		}
		fprintf(ou,"Case #%d: %d\n", k, count);
	}
	return 0;
}