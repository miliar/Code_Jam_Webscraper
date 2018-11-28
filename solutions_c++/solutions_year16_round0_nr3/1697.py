#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define MAX 10000010
int n,q,t;
int h[MAX];
vector<int> primes;

void sieve()
{
	for (int i = 2; i < MAX; ++i)
	{
		if (!h[i])
		{
			for (int j = i; j < MAX; j += i)
			{
				h[j] = 1;
			}
			primes.push_back(i);
		}
	}
}

ll fexp(int a, int b, int mod)
{
	if (b == 0)
		return 1%mod;
	if (b%2 == 0)
	{
		ll x = fexp(a, b/2, mod);
		return (x%mod * x%mod)%mod;
	}
	return ((ll)a%mod * fexp(a, b - 1, mod)%mod)%mod;
}

void add(string &t)
{
	int carry = 1;
	int pos = n - 1;
	int newcarry = 0;
	while (carry)
	{
		newcarry = carry + t[pos] - '0' >= 2;
		t[pos] = (carry + t[pos] - '0')%2 + '0';
		carry = newcarry;
		pos--;
	}
}

int main(void)
{
	scanf("%d",&t);
	scanf("%d%d",&n,&q);

	printf("Case #%d:\n",1);
	string t;
	sieve();
	for (int i = 0; i < n; ++i)
	{
		if (i == 0 || i == n - 1)
			t += '1';
		else
			t += '0';
	}

	while(q)
	{
		add(t);
		add(t);
		// printf("t = %s\n",t.c_str());
		bool ok = true;
		vector<int> ans;
		for (int j = 2; j <= 10; ++j)
		{
			bool ok2 = false;
			for (int a = 0; a < primes.size(); ++a)
			{
				int num = 0;
				int num2 = 0;
				for (int k = 0; k < n; ++k)
				{
					if (t[k] == '1')
					{
						num = (num%primes[a] + fexp(j, n - k - 1, primes[a])%primes[a])%primes[a];
						num2 += fexp(j, n - k - 1, 1000000007);
					}
				}
				if (num == 0 && num2 != primes[a])
				{
					ok2 = true;
					ans.push_back(primes[a]);
					break;
				}
			}
			if (!ok2)
			{
				ok = false;
				break;
			}
		}
		if (ok)
		{
			printf("%s",t.c_str());
			for (int i = 0; i < ans.size(); ++i)
			{
				printf(" %d",ans[i]);
			}
			printf("\n");
			q--;
		}
	}
	return 0;
}