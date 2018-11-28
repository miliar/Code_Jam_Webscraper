#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int T, n;
long long p;

bool pass(int k, long long x)
{
	if (k == 0)
	{
		long long w = x, ret = 0;
		for (long long l = (1LL) << (n - 1); l >= 1; l >>= 1)
			if (w)
			{
				ret += l;
				w--;
				w >>= 1;
			}
//		cout << "\t" << x << " " << ret << endl;
		return ret < p;
	}
	else
	{
		long long w = ((1LL) << n) - x - 1, ret = 0;
		for (long long l = (1LL) << (n - 1); l >= 1; l >>= 1)
			if (!w)
				ret += l;
			else
			{
				w--;
				w >>= 1;
			}
//		cout << "\t" << x << " " << ret << endl;
		return ret < p;
	}
}

long long calc(int k, long long p1, long long p2)
{
//	cout << "\t\t" << k << " " << p1 << " " << p2 << endl;
	if (p1 == p2) return p1;
	long long pp = (p1 + p2 + 1) / 2;
	if (pass(k, pp))
		return calc(k, pp, p2);
	else return calc(k, p1, pp - 1);
}

int main()
{
	scanf("%d", &T);
	int ca = 0;
	while (T--)
	{
		ca++;
		scanf("%d%lld", &n, &p);
		printf("Case #%d: %lld %lld\n", ca, calc(0, 0, (1LL << n) - 1), calc(1, 0, (1LL << n) - 1));
	}
	return 0;
}
