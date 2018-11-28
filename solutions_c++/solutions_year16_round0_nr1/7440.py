#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int res(int input)
{
	if(input == 0) return -1;
	int ck[10] = {0};
	int jb = 0;
	int count = 0;
	long ip = input;
	long long result = 0;
	int j = 1;

	for(int i = 0 ; i < 10 ; i++) ck[i] = 0;

	while(jb != 1)
	{
		count = 0;

		while(ip != 0)
		{
			ck[ip % 10] = 1;
			ip /= 10;
		}


		for(int i = 0; i < 10; i++)
		{
			if(ck[i] == 1)
			{
				count++;
			}
		}
		if(count == 10)
		{
			jb = 1;
		}
		j++;

		ip = input * j;
		result = input * (j-1);
	}
	return result;
}

int main()
{
	FILE *fp1;
	FILE *fp2;

	int i;
	int cnt = 1;
	char buffer[256];

	fp1 = fopen("A-large.in","r");
	fp2 = fopen("A-large.out","w");

	while(1)
	{
		fgets(buffer,255,fp1);
		if(feof(fp1))
		{
			break;
		}

		for(i = 0; i < strlen(buffer); i++)
		{
			if(buffer[i] =='\n')
				buffer[i] = '\0';
		}

		if(res(atoi(buffer)) == -1)
		{
			fprintf(fp2,"Case #%d: INSOMNIA\n",cnt);
		}
		else
		{
			fprintf(fp2,"Case #%d: %d\n",cnt,res(atoi(buffer)));
		}
		cnt++;
	}
	fclose(fp1);
	fclose(fp2);
}
