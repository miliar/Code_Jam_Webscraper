#include <stdio.h>
#include <string.h>

using namespace std;

bool D[10];
long long N;

inline void init()
{
	memset(D, 0, sizeof(D));
	scanf("%lld", &N);
}

inline void get_digit(long long num)
{
	int i;

	while (num)
	{
		D[num % 10] = 1;
		num /= 10;
	}
}

inline bool check()
{
	int i;

	for (i = 0; i < 10; i++)
		if (!D[i])
			return 0;

	return 1;
}

inline void solve()
{
	long long ans = N;

	if (N == 0)
	{
		printf("INSOMNIA\n");
		return;
	}

	get_digit(ans);
	while (!check())
	{
		ans += N;
		get_digit(ans);
	}

	printf("%lld\n", ans);
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
	}

	return 0;
}