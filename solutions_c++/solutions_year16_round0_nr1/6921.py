#include <stdio.h>
#include <string.h>

int t;
int n;
int arr[10];
char temp[100];

int main(void)
{
	FILE *ou = fopen("output.txt", "w");
	int count = 0;
	scanf("%d", &t);
	for (int k = 1; k <= t; k++)
	{
		memset(arr, 0, sizeof(arr));
		count = 0;
		scanf("%d", &n);
		if (n == 0)
			fprintf(ou,"Case #%d: INSOMNIA\n", k);
		else
		{
			while (1)
			{
				memset(temp, 0, sizeof(temp));
				int sw = 1;
				for (int i = 0; i <= 9; i++)
				{
					if (arr[i] == 0)
					{
						sw = 0;
						break;
					}
				}
				if (sw == 1)
				{
					fprintf(ou,"Case #%d: %d\n", k, n * count);
					break;
				}
				count++;
				sprintf(temp, "%d", n * count);
				for (int i = 0; i < strlen(temp); i++)
					arr[temp[i] - '0']++;
			}
		}
	}
	return 0;
}