#include <cstdio>
#include <iostream>

using namespace std;

int T, ans;
long long P, Q;

long long gcd (long long a, long long b) {
	return b ? gcd (b, a % b) : a;
}

bool solve ()
{
	bool p = false;
	long long z = gcd (P, Q);
	P /= z;
	Q /= z;
	for (int i=0; i < 45; ++i)
		if (1 << i == Q)
			p = true;
	if (!p)
		return false;
	ans = 0;
	if (Q % 2)
		return false;
	while (P / Q == 0)
	{
		ans ++;
		if (Q % 2)
			return false;
		Q /= 2;
	}
	return true;
}

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	char c;
	scanf ("%d", &T);
	for (int x = 1; x <= T; ++x)
	{
		scanf ("%lld%c%lld", &P, &c, &Q);
		printf ("Case #%d: ", x);
		if (solve ())
			printf ("%d\n", ans);
		else
			printf ("impossible\n");
	}
	return 0;
}