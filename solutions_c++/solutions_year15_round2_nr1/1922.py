#include <bits/stdc++.h>
using namespace std;
#define long int64_t
#define mt make_tuple

const int n_max = 1000010;

int F[n_max];
int n, n_test;

int rev_int (int x)
{
	int y = 0;
	while (x) y = y * 10 + x % 10, x /= 10;
	return y;
}

void init ()
{
	list<int> P;
	int x, y;

	P.emplace_back(1);
	F[1] = 1;

	while (!P.empty())
	{
		x = P.front();
		P.pop_front();

		if ((y = rev_int(x)) < n_max && F[y] == 0) F[y] = F[x] + 1, P.emplace_back(y);
		if ((y = x + 1)      < n_max && F[y] == 0) F[y] = F[x] + 1, P.emplace_back(y);
	}
}

int main ()
{
	freopen("A.inp", "r", stdin);
	freopen("A.out", "w", stdout);

	init ();

	scanf("%d", &n_test);
	for (int i = 1; i <= n_test; ++i)
	{
		scanf("%d", &n);
		printf("Case #%d: %d\n", i, F[n]);
	}

	return 0;
}