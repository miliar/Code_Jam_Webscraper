#include <stdio.h>
#include <string.h>

int t;
int n;
int arr[27];
int temp[27];

int main(void)
{
	FILE *out = fopen("output.txt", "w");
	int i;
	int j;
	int k;
	scanf("%d", &t);
	for (k = 1; k <= t; k++)
	{
		memset(arr, 0, sizeof(arr));
		memset(temp, 0, sizeof(temp));
		scanf("%d", &n);
		for (i = 1; i <= n; i++)
			scanf("%d", &arr[i]);
		fprintf(out, "Case #%d: ", k);
		while (1)
		{
			int sw = 0;
			int l;
			
			for (i = 1; i <= n; i++)
			{
				if (arr[i] > 0)
				{
					sw = 1;
					break;
				}
			}
			if (sw == 0)
				break;
			sw = 0;
			for (i = 1; i <= n; i++)
			{
				for (j = 1; j <= n; j++)
				{
					int max = -1000;
					int maxcount = 0;
					for (l = 1; l <= n; l++)
						temp[l] = arr[l];
					if (temp[i] > 0 || temp[j] > 0)
					{
						temp[i]--;
						temp[j]--;
						for (l = 1; l <= n; l++)
						{
							if (temp[l] > max)
							{
								max = temp[l];
								maxcount = 1;
							}
							else if (temp[l] == max)
								maxcount++;
						}
						if (maxcount >= 2)
						{
							sw = 1;
							for (l = 1; l <= n; l++)
								arr[l] = temp[l];
							if (arr[i] >= 0)
								fprintf(out, "%c", 'A' + i - 1);
							if (arr[j] >= 0)
								fprintf(out, "%c", 'A' + j - 1);
							if(arr[i] == arr[j] && arr[i] == -1)
								fprintf(out, "%c", 'A' + j - 1);
							fprintf(out, " ");
							break;
						}
					}
				}

				if (sw == 1)
				{
					break;
				}
			}
		}
		fprintf(out, "\n");
	}
	return 0;
}