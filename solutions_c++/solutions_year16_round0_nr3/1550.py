#include <bits/stdc++.h>
#define TEST_PRIME_LIMIT 10

using namespace std;

typedef long long ll;

ll eqtest(ll x, int b, ll k)
{
	ll kb = 0;
	int i = 0;
	while(k)
	{
		ll d = k%(ll)b;
		k/=(ll)b;
		if (d > 1LL) return false;
		if (d)
			kb |= (1LL << i);
		i++;
	}
	if (x == kb)
		return true;
	return false;
}

bool test(ll x, int b, ll k)
{
	ll pwr = 1LL, res = 0LL;
	
	for (int i = 0; i < 32; i++)
	{
		if ((x >> i)&1)
		{
			res += pwr;
			res %= k;
		}
		pwr *= (ll)b;
		pwr %= k;
	}

	if (res == 0 and !eqtest(x, b, k))
		return true;
	return false;
}

vector<ll> primes;
void generate_primes()
{
	ll N = TEST_PRIME_LIMIT;
	vector<bool> v(N+1);
	for (ll i = 2; i*i <= N; i++)
	{
		if (!v[i])
		{
			for (ll j = i*i; j <= N; j += i)
			{
				v[j] = true;
			}
		}	
	}

	for (int i = 2; i <= N; i++)
	{
		if (!v[i])
			primes.push_back((ll)i);
	}
}


void printb(ll x)
{
	int i = 33;
	while (((x >> i)&1) == 0)
		i--;
	for (; i >= 0; i--)
	{
		if ((x >> i)&1)
			printf("1");
		else
			printf("0");
	}
}

int main()
{
	generate_primes();
	int T, casecnt = 0;
	scanf("%d", &T);
	while(T--)
	{
		int n, j;
		scanf("%d %d", &n, &j);
		ll x = (1LL << (n-1)) | (1LL);
		printf("Case #%d:\n", ++casecnt);
		while(j)
		{
			int mask = 3;
			ll ans[11] = {0};
			bool ok = false;
			for (int i = 0; i < primes.size() and !ok; i++)
			{
				for (int b = 2; b <= 10; b++)
				{
					if ((mask >> b)&1) continue;
					if (test(x, b, primes[i]))
					{
						mask |= (1 << b);
						ans[b] = primes[i];
					}
				}
				if (mask == (1 << 11)-1)
					ok = true;
			}
			if (ok)
			{
				j--;
				printb(x);
				for (int i = 2; i <= 10; i++)
					printf(" %lld", ans[i]);
				printf("\n");
			}
			x += 2LL;
		}	
	}
	return 0;
}
