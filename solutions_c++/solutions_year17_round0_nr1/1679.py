#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

char s[10005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d", &T);

	int N, K;

	for (int cn = 1; cn <= T; ++cn)
	{
		scanf("%s %d", s, &K); 
		N = strlen(s);
		int ret = 0;

		for (int i = 0; i <= N - K; ++i)
		{
			if (s[i] == '-')
			{
				ret++;
				for (int j = 0; j < K; ++j)
					s[i + j] = '-' + '+' - s[i + j];
			}
		}

		bool ispos = true;
		for (int i = 0; i < N; ++i)
			if (s[i] == '-') ispos = false;

		if (ispos)
			printf("Case #%d: %d\n", cn, ret);
		else
			printf("Case #%d: IMPOSSIBLE\n", cn);
	}	
}