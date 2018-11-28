#include <cstdio>

#define ULL unsigned long long
#define DONE ( (1<<10) - 1 )

int T, N;

int count (ULL n)
{
	int r = 0;

	while (n > 0)
	{
		r |= (1 << (n%10));
		n /= 10;
	}

	return r;
}

void solve (int n)
{
	if (n == 0)
	{
		printf("INSOMNIA\n");
		return;
	}

	int cnt = 0;
	ULL cur = 0;

	do {
		cur += n;
		cnt |= count(cur);
	} while ( cnt != DONE );

	printf("%llu\n", cur);
}

int main ()
{
	scanf("%d", &T);

	for (int t=1; t<=T; t++)
	{
		printf("Case #%d: ", t);
		scanf("%d", &N);
		solve(N);
	}

	// test
	// for (int i = 0; i <= 1000000; ++i)
	// {
	// 	printf("Case #%d: ", i);
	// 	solve(i);
	// }

	return 0;
}