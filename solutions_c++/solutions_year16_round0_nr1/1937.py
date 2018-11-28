#include <cstdio>
#include <cstring>

typedef long long ll;

int Count;
bool vis[10];

void change(int index)
{
	if (vis[index] == false)	Count ++;
	vis[index] = true;
}

void check(ll N)
{
//	printf("%lld\n", N);
	for (;;)
	{
		if (N == 0)	break;
		change(N % 10);
		N /= 10;
	}
//	printf("%d\n", Count);
}

void domain()
{
	ll N;
	scanf("%lld", &N);
	if (N == 0)
	{
		puts("INSOMNIA");
	}
	else
	{
		Count = 0;
		for (int i = 0; i < 10; ++i)	vis[i] = false;
		for (int i = 1; ; ++i)
		{
			check(1ll * i * N);
			if (Count == 10)
			{
				printf("%lld\n", 1ll * i * N);
				return;
			}
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++ kase)
	{
		printf("Case #%d: ", kase);
		domain();
	}
	return 0;
}
