#include <stdio.h>
#include <string.h>

bool check(char s[])
{
	for (int i = 0; i < strlen(s); ++i)
	{
		if (s[i] == '-')
			return false;
	}

	return true;
}

int main()
{
	int t;
	char s[101], tmp[101];

	FILE *in = fopen("input.txt", "rt");
	FILE *out = fopen("output.txt", "wt");

	fscanf(in, "%d", &t);

	for (int tcnt = 1; tcnt <= t; ++tcnt)
	{
		int answer = 0;
		fscanf(in, "%s", s);

		int n = strlen(s);
		int i;

		while (!check(s))
		{
			if (s[0] == '+')
			{
				for (i = 0; i < n; ++i)
				{
					if (s[i] == '-') 
						break;
					s[i] = '-';
				}
				
				++answer;

			}

			for (i = n - 1; i >= 0; --i)
			{
				if (s[i] == '-')
					break;
			}

			memcpy(tmp, s, n + 1);

			for (int j = 0; j <= i; ++j)
			{
				if (tmp[i - j] == '-') s[j] = '+';
				else s[j] = '-';
			}
			
			answer++;
		}

		fprintf(out, "Case #%d: %d\n", tcnt, answer);
	}

	fclose(in);
	fclose(out);

	return 0;
}