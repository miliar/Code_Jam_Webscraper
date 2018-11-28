#include <cstdio>

using namespace std;

int S[110];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int te = 1; te <= T; te++)
	{
		printf("Case #%d: ", te);
		char c = getchar();
		while (c != '+' && c != '-')
		{
			c = getchar();
		}
		int n = 0;
		while (c == '+' || c == '-')
		{
			S[++n] = (c == '+');
			c = getchar();
		}
		int res = 0;
		for (int i = n; i >= 1; i--)
		{
			if (S[i] == 0)
			{
				res++;
				for (int j = i; j >= 1; j--) 
				{
					S[j] = 1 - S[j];
				}
			}
		}
		printf("%d\n", res);
	}
	return 0;
}