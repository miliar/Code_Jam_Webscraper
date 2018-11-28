#include <cstdio>
#include <cmath>
#define ll long long
int tests, r, res;
ll a, b;
int A[] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};

inline int palindrome(ll x)
{
	ll y = x, z = 0;
	while (y)
	{
		z = z * 10 + y % 10;
		y /= 10;
	}
	
	return x == z;
}

int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int i, j;
	r = 39;
	
	scanf("%d", &tests);
	for (i = 1; i <= tests; i++)
	{
		scanf("%lld%lld", &a, &b);
		res = 0;
		for (j = 0; j < r; j++)
			if ((ll)A[j] * A[j] >= a && (ll)A[j] * A[j] <= b)
				res++;
			
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}
