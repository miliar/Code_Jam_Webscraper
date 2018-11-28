/*
Problem #524 Prime Ring Problem - UVA
http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=465
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <bitset>
#include <string>
using namespace std;

typedef long long ll;

bitset<31622790> bs;
vector<int> primes;

void sieve()
{
	ll _sieve_size = 31622780 + 1;                   // add 1 to include upperbound
	bs.set();                                                 // set all bits to 1
	bs[0] = bs[1] = 0;                                     // except index 0 and 1
	for (ll i = 2; i <= _sieve_size; i++) if (bs[i])
	{
		for (ll j = i * i; j <= _sieve_size; j += i)
			bs[j] = 0;
		primes.push_back((int)i);  // also add this vector containing list of primes
	}
}

bool isPrime(ll a)
{
	if (a <= 31622780)
		return bs[a];

	for (int i = 0; i < primes.size() && primes[i] * primes[i] <= a; i++)
		if (a % primes[i] == 0)
			return false;

	return true;
}

int div(ll a)
{
	for (int i = 0; i < primes.size() && primes[i] * primes[i] <= a; i++)
		if (a % primes[i] == 0)
			return primes[i];

	return 0;
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	
	int t;
	int ans;
	ll a, b, c, d;
	string s;
	sieve();
	cin >> t;
	bool found;
	cerr << "starting\n";
	for (int z = 1; z <= t; z++)
	{
		printf("Case #%d:", z);
		int n, j;
		cin >> n >> j;

		a = (1 << (n - 1)) + 1;
		ans = 0;
		while (ans < j)
		{
			found = true;
			for (int i = 2; i <= 10; i++)
			{
				b = a;
				d = 1;
				c = 0;
				while (b)
				{
					c += (b & 1) * d;
					d *= i;
					b >>= 1;
				}
				if (isPrime(c))
				{
					found = false;
					break;
				}
			}

			if (found)
			{
				cout << endl;
				b = a;
				s = "";
				while (b)
				{
					s += (b & 1) + '0';
					b >>= 1;
				}
				reverse(s.begin(), s.end());
				cout << s;
				for (int i = 2; i <= 10; i++)
				{
					b = a;
					d = 1;
					c = 0;
					while (b)
					{
						c += (b & 1) * d;
						d *= i;
						b >>= 1;
					}
					cout << ' ' << div(c);
				}
				ans++;
			}
			a += 2;
		}

	}
	return 0;
}
