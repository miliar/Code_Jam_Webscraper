#include "problem_name.h"
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int T;
bool used[10];

void INIT()
{
	for (int i = 0; i < 10; i++)
		used[i] = false;
}

bool good()
{
	for (int i = 0; i < 10; i++)
		if (!used[i])
			return false;
	return true;
}

ll solve(ll x, ll h = 1)
{
	ll val = x * h;
	while (val > 0)
	{
		used[val % 10] = true;
		val /= 10;
	}
	if (good())
		return x * h;
	return solve(x, h + 1);
}

void cry()
{
	printf("INSOMNIA\n");
}

void solveLarge()
{
	scanf("%d", &T);
	int x;
	for (int i = 0; i < T; i++)
	{
		INIT();
		scanf("%d", &x);
		printf("Case #%d: ", i + 1);
		if (x == 0)
			cry();
		else
			printf("%I64d\n", solve(x));
	}
}

void test()
{
	for (int i = 1; i <= (int)1e6; i++)
	{
		INIT();
		printf("%d : %I64d\n", i, solve(i));
	}
}

int main()
{
	freopen("xxx.in", "r", stdin);
	freopen("xxx.out", "w", stdout);
	//test();
	solveLarge();
	return 0;
}