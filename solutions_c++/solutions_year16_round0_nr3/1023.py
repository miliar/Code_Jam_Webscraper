#include <bits/stdc++.h>
using namespace std;

int N, J, cnt;
int divisor[100];

void check(int jamcoin)
{
	if (!(jamcoin & 1)) return;
	if (!((1 << N - 1) & jamcoin)) return;
	for (int i = 2; i <= 10; ++i)
	{
		long long n = 0, base = 1;
		for (int j = 0; j < N; ++j)
		{
			if ((1 << j) & jamcoin)	n += base;
			base *= i;
		}
		divisor[i] = -1;
		for (int j = 2; j < n && j <= 1000; ++j)
			if (n % j == 0) 
			{
				divisor[i] = j;
				break;
			}
		if (divisor[i] == -1) return;
	}
	for (int i = N - 1; i >= 0; --i)
		if ((1 << i) & jamcoin) printf("1");
		else printf("0");
	for (int i = 2; i <= 10; ++i)
		printf(" %d", divisor[i]);
	puts("");
	++cnt;
}

int main(int argc, char *argv[])
{
	scanf("%*d%d%d", &N, &J);
	puts("Case #1:");
	for (int i = 0; i < (1 << N); ++i)
	{
		check(i);
		if (cnt == J) break;
	}
	return 0;
}
