#include<stdio.h>
#include<math.h>

bool scan(__int64 n, bool visited[])
{
	while (n > 0)
	{
		visited[n % 10] = true;
		n /= 10;
	}
	for (int i = 0; i < 10; i++)
	{
		if (!visited[i]) return false;
	}
	return true;
}

int countDigits(__int64 n)
{
	int r = 1;
	while (n /= 10)
	{
		r++;
	}
	return r;
}

__int64 solve(int n)
{
	if (n == 0)return 0;
	int cnt = countDigits(n);
	bool visited[10] = {};
	__int64 tmp = n;
	for (int i = 1; i <= 100; i++)
	{
		if (scan(tmp, visited)) return tmp;
		tmp += n;
	}
	return 0;
}

int main()
{
	int T, N;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d", &N);
		__int64 res = solve(N);
		printf("Case #%d: ", i + 1);
		if (res == 0) printf("INSOMNIA\n");
		else printf("%I64d\n", res);
	}
	return 0;
}



