#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define INF (1 << 30)
#define SQR(a) ((a) * (a))

using namespace std;

const int N = 1111;

int getMask(int a)
{
	int res = 0;
	while (a > 0)
	{
		res |= (1 << a % 10);
		a /= 10;
	}
	return res;
}

int solve(int x)
{
	int mask = getMask(x), target = (1 << 10) - 1;
	int cur = x;
	while (target != mask)
	{
		cur += x;
		mask |= getMask(cur);	
	}
	return cur;
}

int main()
{
	int t;
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		int x = i;
		scanf("%d", &x);
		if (x == 0)
			printf("Case #%d: INSOMNIA\n", i);
		else
			printf("Case #%d: %d\n", i, solve(x));
	}	
	return 0;
}
