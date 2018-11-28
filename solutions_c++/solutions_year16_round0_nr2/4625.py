#include<stdio.h>
#include<string.h>

FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int T;
char str[105];
int len;
int cnt = 0;


int main()
{
	fscanf(in,"%d", &T);
	for (int t = 1; t <= T;t++)
	{
		cnt = 0;
		fscanf(in ,"%s", str);
		len = strlen(str);
		for (int i = len - 1; i >= 0; i--)
		{
			if (str[i] == '-')
			{
				cnt++;
				for (int j = i; j >= 0; j--)
				{
					if (str[j] == '-')str[j] = '+';
					else str[j] = '-';
				}
			}
		}
		fprintf(out,"Case #%d: %d\n", t, cnt);
	}

}