#include<stdio.h>
#include <string.h>
char input[2000+2] = {'\0', };

int a[26+1];
int digit[10+1];

int main()
{
	int T;
	int k;
	scanf("%d", &T);
	for (k = 0; k < T; k++)
	{
		scanf("%s", input);

		memset(a, 0, sizeof(a));
		memset(digit, 0, sizeof(digit));
		for (int i = 0; i < strlen(input); i++)
		{
			a[input[i]-'A']++;
			if (input[i] == 'Z')
			{
				digit[0]++;
				a['E'-'A']--;
				a['O'-'A']--;
				a['R'-'A']--;	
			}

			else if (input[i] == 'G')
			{
				digit[8]++;
				a['E'-'A']--;
				a['I'-'A']--;
				a['H'-'A']--;
				a['T'-'A']--;
			}

			else if (input[i] == 'X')
			{
				digit[6]++;
				a['S'-'A']--;
				a['I'-'A']--;
			}
			else if (input[i] == 'U')
			{

				digit[4]++;
				a['F'-'A']--;
				a['O'-'A']--;
				a['R'-'A']--;
			}

			else if (input[i] == 'W')
			{
				digit[2]++;
				a['T'-'A']--;
				a['O'-'A']--;
			}
		}
		{
			if (a['O' -'A'] >=1)
			{
				digit[1] = a['O'-'A'];
				a['N'-'A'] -= a['O'-'A'];
				a['E'-'A'] -= a['O'-'A'];
				a['O'-'A'] = 0;
			}
		}	
		{

			if (a['H'-'A'] >= 1)
			{
				digit[3] = a['H'-'A'];
				a['T'-'A'] -= a['H'-'A'];
				a['R'-'A'] -= a['H'-'A'];
				a['E'-'A'] -= a['H'-'A'];
				a['E'-'A'] -= a['H'-'A'];
				a['H'-'A'] = 0;
			}

			if (a['F'-'A'] >=1)
			{
				digit[5] = a['F'-'A'];
				a['I'-'A'] -= a['F'-'A'];
				a['V'-'A'] -= a['F'-'A'];
				a['E'-'A'] -= a['F'-'A'];
				a['F'-'A'] = 0;
			}
		}
		{
			if (a['I'-'A'] >=1)
			{
				digit[9] = a['I'-'A'];
				a['N'-'A'] -= a['I'-'A'];
				a['N'-'A'] -= a['I'-'A'];
				a['E'-'A'] -= a['I'-'A'];
				a['I'-'A'] = 0;
			}
		}
		{

			if (a['V'-'A'] >= 1)
			{
				digit[7] += a['V'-'A'];
				a['E'-'A'] -= a['V'-'A'];
				a['E'-'A'] -= a['V'-'A'];
				a['N'-'A'] -= a['V'-'A'];
				a['S'-'A'] -= a['V'-'A'];
				a['V'-'A'] = 0;
			}
		}

		{
			if (a['S' -'A'] >=1)
			{
				digit[7] += a['S'-'A'];
				a['E'-'A'] -= a['S'-'A'];
				a['E'-'A'] -= a['S'-'A'];
				a['N'-'A'] -= a['S'-'A'];
				a['S'-'A'] = 0;
			}
		}

		{
			if(a['N' - 'A'] >=1)
			{
				digit[7] += a['N'-'A'];
				a['E'-'A'] -= a['N'-'A'];
				a['E'-'A'] -= a['N'-'A'];
				a['N'-'A'] = 0;
			}
		}
	
		printf("Case #%d: ", (k+1));
		for (int i = 0; i <= 9; i++)
		{
			for (int j = 0; j < digit[i]; j++)
			{
				printf("%d",i);
			}
		}

		printf("\n");

	}
}
