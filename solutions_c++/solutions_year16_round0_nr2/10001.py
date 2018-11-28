#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	FILE *out = fopen("output.txt", "w");
	int Cnum,i,j,k,count,flag;
	char str[100][100],temp[100];
	scanf("%d", &Cnum);

	for (i = 0; i < Cnum; i++)
		scanf("%s", str[i]);


	for (i = 0; i < Cnum; i++)
	{
		flag = 0;
		count = 0;
		for (j = 0; j < strlen(str[i]); j++)
		{
			if (str[i][j] != str[i][j + 1])
			{
				temp[count] = str[i][j];
				count++;
			}

		}
		temp[count] = '\0';
		for (k = 0; k < strlen(temp); k++)
		{
			if (k == 0)
			{
				if (temp[k] == '-')
					flag = flag + 1;
			}
			else
				if (temp[k] == '-')
					flag = flag + 2;
		}
		fprintf(out,"Case #%d: %d\n", i + 1, flag);
	}
	return 0;
}