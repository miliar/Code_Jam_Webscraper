#include <cstdio>
typedef long long lld;

bool visit[12]{ };
lld C, M, N, T;

void check(const lld& Num)
{
	lld tem = Num;
	while(tem)
	{
		lld mod = tem % 10;
		if(!visit[mod])
		{
			visit[mod] = true;
			C++;
		}
		tem /= 10;
	}
}

int main()
{
	scanf(" %lld", &T);
	for(int _i = 1; _i <= T; ++_i)
	{
		scanf("%lld", &N);
		printf("Case #%d: ", _i);
		if(N != 0)
		{
			C = 0;
			for(int i = 0; i <= 9; ++i)
				visit[i] = false;
			M = 0;
			do {
				M += N;
				check(M);
			} while(C <= 9);
			printf("%lld\n", M);
		}
		else
			puts("INSOMNIA");
	}
	return 0;
}