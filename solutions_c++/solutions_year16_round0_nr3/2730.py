#include <cstdio>
#include <cstdlib>

using namespace std;

#define ll long long

int n, J;
ll p[20];

void ghi(ll n)
{
	char s[50];
	itoa((int)n, s, 2);
	printf("%s", s);
}

ll interpete(ll k, int base)
{
	ll sm = 1, res = 0;
	while (k > 0)
	{
		res += (sm*(k % 2));
		k /= 2;
		sm *= base;
	}
	return res;
}

ll checkPrime(ll n)
{
	for (ll i = 2; i*i <= n; i++)
	{
		if (n%i == 0)
		{
			return i;
		}
	}
	return -1;
}

int main()
{
	//freopen("", "r", stdin);
	freopen("C.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int te = 1; te <= T; te++)
	{
		printf("Case #%d:\n", te);
		scanf("%d%d", &n, &J);
		int cnt = 0;
		ll fb = 1ll << (n - 1);
		for (ll mask = 0; mask < (1 << (n - 2)); mask++)
		{
			ll nmask = (mask * 2ll) + 1 + fb;
			//printf("%I64d\n", nmask);
			bool flag = 1;
			for (int j = 2; j <= 10; j++)
			{
				ll k = interpete(nmask, j);
				p[j] = checkPrime(k);
				if (p[j] == -1)
				{
					flag = 0;
					break;
				}
			}
			if (flag)
			{
				ghi(nmask);
				for (int j = 2; j <= 10; j++)
				{
					printf(" %I64d", p[j]);
				}
				printf("\n");
				cnt++;
				if (cnt == J)
				{
					break;
				}
			}
		}
	}
	return 0;
}