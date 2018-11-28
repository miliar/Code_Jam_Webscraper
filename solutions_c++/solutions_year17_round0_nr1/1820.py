#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

char s[1005];
void Solve()
{
	int k, res = 0;
	scanf("%s%d", s, &k);
	int n = strlen(s);
	for (int i = 0; i < n; ++i)
		if (s[i] == '-')
		{
			if (n - i < k)
			{
				puts("IMPOSSIBLE");
				return;
			}
			++res;
			for (int j = i; j <= i + k - 1; ++j)
				if (s[j] == '+') s[j] = '-'; else s[j] = '+';
		}
	printf("%d\n", res);
}

int T;
int main()
{
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		Solve();
	}
}
