#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
int fair(int n)
{
	int flag = 1;
	char num[30];
	itoa(n, num, 10);
	int len = strlen(num);
	for(int j = 0; j < len; j++)
	{
		if(num[j] != num[len - 1 - j])
		{
			flag = 0;
			break;
		}
	}
	return flag;	
}
int square(int n)
{
	float x = sqrt(n);
	if((x * x) == n)
		return 1;
	return 0;
}
int main(int argc, char *argv[])
{
	if(argc == 2)
	{
		FILE *in = fopen(argv[1],"r");
		FILE *out = fopen("C.out","w");
		if(in != 0)
		{
                        char line[50];
			fgets(line, 50, in);
			int n = atoi(line);
			for(int i = 1; i <= n; i++)
			{
				fgets(line, 50, in);
				char word[2][30];
				char wordx[2][30];
				int k = 0, j = 0, l  = 0;
				for(j = 0; j < strlen(line); j++)
				{
					if(line[j] != ' ' && line[j] != '\n') 
						word[l][k++] = line[j];
					else
					{
						word[l][k] = '\0';
						l++;
						k = 0;
					}
				}
				word[l][k] = '\0';
				int n1 = atoi(word[0]);
				int n2 = atoi(word[1]);
				int count = 0;							
				for(int z = n1; z <= n2; z++)
					if(fair(z))
						if(square(z))
							if(fair(sqrt(z)))
								count++;
				
				fputs("Case #", out);
				char num[10];
				itoa(i, num, 10);
				fputs(num, out);
				fputs(": ", out);
				itoa(count, num, 10);
				fputs(num, out);
				fputs("\n", out);
			}
			fclose(out);
			fclose(in);
		}
	}
	return 1;
}
