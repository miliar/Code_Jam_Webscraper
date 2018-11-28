#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long LL;

LL C[20][20],G[20],D[20];
int a[20],tt;

void Pre()
{
	for (int i = 2; i <= 10; i ++)
	{
		C[i][0] = 1;
		for (int j = 1; j <= 16; j ++)
			C[i][j] = 1ll * C[i][j - 1] * i;
	}
}

bool isprime(int pos, LL x)
{
	LL p = sqrt(x) + 1;
	for (LL i = 2; i <= p; i ++)
	{
		G[pos] = i;
		if (x % i == 0) return 0;
	}
	return 1;
}

void Output(int n)
{
	printf("{");
	for (int i = n; i; i --) printf("%d", a[i]); printf(" ,");
	for (int i = 2; i <= 9; i ++) printf("%lld,", G[i]);
	printf("%lld", G[10]);
	puts("},");
	tt --;
}

void Output2(int n)
{
	for (int i = n; i; i --) printf("%d", a[i]); printf(" ");
	for (int i = 2; i <= 9; i ++) printf("%lld ", G[i]);
	printf("%lld\n", G[10]);
	tt --;
}

void Check(int n)
{
	memset(D, 0, sizeof D);
	for (int i = 1; i <= n; i ++)
	{
		for (int j = 2; j <= 10; j ++)
			D[j] += C[j][i-1] * a[i];
	}
	for (int i = 2; i <= 10; i ++)
		if (isprime(i, D[i])) return;
	Output2(n);
}

int main()
{
//	freopen("C.in", "r", stdin);
//	freopen("C.out", "w", stdout);

	Pre();

	int T,td,num;
	scanf("%d", &T);
	scanf("%d%d", &td, &num);
	printf("Case #1:\n");

	for (int i = td; i <= td; i ++, puts(""))
	{
		//printf("%d\n\n", i);
		int n = i-1;
		a[i] = 1; tt = num;
		for (int j = 0, lim = 1 << n; j < lim && tt; j ++)
		{
			if (!(j & 1)) continue;
			for (int k = 1; k <= n; k ++)
				if (j & (1 << (k-1))) a[k] = 1; else a[k] = 0;
			Check(i);
		}
		/*while (tt)
		{
			Output(i);
		}*/
	}

	return 0;
}
