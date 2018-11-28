#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;


int main()
{
	int T;
	scanf("%d", &T);

	for (int ca = 1; ca <= T; ca ++)
	{
		char s[200];
		scanf("%s", s);
		
		int len = strlen(s);
		int ans = 0;

		for (int i = len - 1; i >= 0; i --)
		{
			if (s[i] == '-')
			{
				bool f = 0;
				for (int j = 0; j < i; j ++)
				{
					if (s[j] == '+')
						s[j] = '-', f = 1;
					else
						break;
				}
				if (f == 1)
					ans ++;

				for (int j = 0; j <= i / 2; j ++)
				{
					int t = s[j];
					s[j] = s[i - j];
					s[i - j] = t;
				}
				for (int j = 0; j <= i; j ++)
				{
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
				ans ++;
			}
		}

		printf("Case #%d: %d\n", ca, ans);
	}
}