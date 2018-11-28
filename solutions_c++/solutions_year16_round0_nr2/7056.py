#include <cstdio>
#include <cstring>

using namespace std;

bool check(char S[101], int N)
{
	char T[101];

	for (int i = 0; i < N; i++)
		T[i] = '+';
	
	T[N] = '\0';

	for (int i = 0; i < N; i++)
	{
		if (S[i] != T[i])
			return false;
	}

	return true;
}

int main()
{
	// freopen("B.in", "r", stdin);
	// freopen("out.txt", "w", stdout);

	int T, case_count = 1;
	char S[101];

	scanf("%d", &T);

	while (T--)
	{
		scanf("%s", S);
		
		int N = strlen(S);
		int ans = 0;

		while (!check(S, N))
		{
			for (int i = N-1; i >= 0; i--)
			{
				if (S[i] == '-')
				{
					for (int j = 0; j <= i; j++)
					{
						if (S[j] == '-')
							S[j] = '+';
						else
							S[j] = '-';
					}
					ans++;
				}
			}
		}

		printf("Case #%d: %d\n", case_count++, ans);
	}

	return 0;
}