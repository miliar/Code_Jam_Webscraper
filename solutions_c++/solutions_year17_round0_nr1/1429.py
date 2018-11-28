#include <cstdio>
#include <cstring>

int main(int argc, char* argv)
{
	int T, t;
	
	char S[1024];
	int S_Len;
	int K;

	int ans;

	scanf("%d", &T);

	for (t = 1; t <= T; t++)
	{
		ans = 0;
		scanf("%s%d", S, &K);
		S_Len = strlen(S);

		for (int i = 0; i < S_Len + 1 - K; i++)
		{
			if (S[i] == '-')
			{
				ans++;

				for (int j = i; j < i + K; j++)
				{
					S[j] = (S[j] == '-') ? '+' : '-';
				}
			}
		}

		for (int i = S_Len + 1 - K; i < S_Len; i++)
		{
			if (S[i] == '-')
			{
				ans = -1;
				break;
			}
		}

		if (ans < 0)
		{
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
		else
		{
			printf("Case #%d: %d\n", t, ans);
		}
	}

	return 0;
}