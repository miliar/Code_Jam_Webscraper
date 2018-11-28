#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int t, n, cate;
int sir[50];

long long convert(int base)
{
    long long rez = 0;
    long long cnt = 1;
    for (int i = 0; i < n; i++) {
		rez += cnt*sir[i];
		cnt *= base;
    }
    return rez;
}

long long diviz(long long val)
{
	for (long long d = 2; d*d <= val; d++)
		if (val % d == 0)
			return d;
	return 1;
}

int isJam()
{
	for (int base = 2; base <= 10; base++)
	{
		long long val = convert(base);
        long long x = diviz(val);
        if (x == 1)
			return 0;
	}
}

void print()
{
	for (int i = n-1; i >= 0; i--)
		printf("%d", sir[i]);
	printf(" ");
    for (int base = 2; base <= 10; base++)
        printf("%lld ", diviz(convert(base)));
	printf("\n");
}

void solve()
{
    /// sir's bites rest in reversed order
    sir[0] = 1;
    sir[n-1] = 1;
    int gata = 0;
    for (unsigned int nr = 0; nr < ((unsigned int)1) << n-2 && gata < cate; nr++) {
		for (int i = 1; i <= n-2; i++)
			sir[i] = (nr>>(i-1)) & 1;
		if (isJam()) {
			print();
			gata++;
		}
	}

}

int main()
{
	freopen("coin.in", "r", stdin);
	freopen("coin.out", "w", stdout);

	scanf("%d", &t);
	scanf("%d %d", &n, &cate);
	printf("Case #1:\n");
    solve();


    return 0;
}
