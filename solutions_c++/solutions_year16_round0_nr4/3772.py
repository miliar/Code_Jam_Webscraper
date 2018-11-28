#include <stdio.h>
#include <math.h>

using namespace std;

int K, C, S;
long long curr;

inline void init()
{
	scanf("%d %d %d", &K, &C, &S);

	curr = pow(K, C - 1.0);
}

inline void solve()
{
	long long i;

	for (i = 0; i < K; i++)
		printf("%lld ", curr * i + 1);
}

int main()
{
	int T, i;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);

	for (i = 1; i <= T; i++)
	{
		init();
		printf("Case #%d: ", i);
		solve();
		printf("\n");
	}

	return 0;
}