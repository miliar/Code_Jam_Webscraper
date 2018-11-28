#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctype.h>

using namespace std;

int round(double d)
{
	return static_cast<int>(d + 0.5);
}

int main()
{
	int T, test, N, i, j, k, p_count, t[101], n[101], count, resp;
	char s[101][100+1], pattern[100+1], last;
	bool b;

	scanf("%d", &T);
	for (test = 1; test <= T; test++)
	{
		scanf("%d", &N);

		for (i = 0; i < N; i++)
		{
			scanf("%s", s[i]);
		}

		last = '\0';
		p_count = 0;
		for (j = 0; isalpha(s[0][j]); j++)
		{
			if (last != s[0][j])
			{
				t[p_count] = 0;
				pattern[p_count++] = last = s[0][j];
			}
		}

		b = true;
		for (i = 0; i < N && b; i++)
		{
			for (j = 0, k = 0; j < p_count && b; j++)
			{
				if (s[i][k] == pattern[j])
				{
					while (s[i][k] == pattern[j])
					{
						t[j]++;
						k++;
					}
				}
				else
				{
					b = false;
				}
			}

			if (j < p_count || isalpha(s[i][k]))
			{
				b = false;
			}
		}

		if (b)
		{
			for (j = 0; j < p_count; j++)
			{
				n[j] = round((double)t[j] / (double)N);
			}

			resp = 0;
			for (i = 0; i < N; i++)
			{
				for (j = 0, k = 0; j < p_count; j++)
				{
					count = 0;
					while (s[i][k] == pattern[j])
					{
						count++;
						k++;
					}

					resp += abs(count - n[j]);
				}
			}

			printf("Case #%d: %d\n", test, resp);
		}
		else
		{
			printf("Case #%d: Fegla Won\n", test);
		}
	}

	return 0;
}
