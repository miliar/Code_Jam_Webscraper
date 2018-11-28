#include <cstdio>
#include <stack>
#include <cmath>

typedef long long ll;

ll isPrime(ll n)
{
	ll sqrtN = ceil(sqrt(n));
	for (ll i = 2; i <= sqrtN; ++i)
	{
		if (n%i == 0) return i;
	}
	return false;
}

ll transfer(ll n, ll base)
{
	ll ans = 0, temp = 1;
	while (n)
	{
		ans += temp*(n & 1);
		n >>= 1;
		temp *= base;
	}
	return ans;
}

int main()
{
	ll count = 0, T, N, J, temp;
	ll table[11];
	bool isJamcoin;
	scanf("%lld", &T);
	while (T--)
	{
		scanf("%lld%lld", &N, &J);
		printf("Case #%lld:\n", ++count);
		for (ll i = (1 << (N - 1)) + 1, max = 1 << N; i < max&&J; i += 2)
		{
			isJamcoin = true;
			for (ll j = 2; j <= 10; ++j)
			{
				temp = isPrime(transfer(i, j));
				if (temp)
				{
					table[j] = temp;
				}
				else
				{
					isJamcoin = false;
					break;
				}
			}
			if (isJamcoin)
			{
				--J;
				std::stack<int> s;
				temp = i;
				while (temp)
				{
					s.push(temp & 1);
					temp >>= 1;
				}
				while (!s.empty())
				{
					putchar(s.top() + '0');
					s.pop();
				}
				for (ll j = 2; j <= 10; ++j) printf(" %lld", table[j]);
				putchar('\n');
			}
		}
	}
	return 0;
}