#include <bits/stdc++.h>
#define ll long long
using namespace std;

/*
* calculates (a * b) % c taking into account that a * b might overflow
*/
ll mulmod(ll a, ll b, ll mod)
{
	ll x = 0, y = a % mod;
	while (b > 0)
	{
		if (b % 2 == 1)
		{
			x = (x + y) % mod;
		}
		y = (y * 2) % mod;
		b /= 2;
	}
	return x % mod;
}
/*
* modular exponentiation
*/
ll modulo(ll base, ll exponent, ll mod)
{
	ll x = 1;
	ll y = base;
	while (exponent > 0)
	{
		if (exponent % 2 == 1)
			x = (x * y) % mod;
		y = (y * y) % mod;
		exponent = exponent / 2;
	}
	return x % mod;
}

/*
* Miller-Rabin primality test, iteration signifies the accuracy
*/
bool Miller(ll p, int iteration)
{
	if (p < 2)
	{
		return false;
	}
	if (p != 2 && p % 2 == 0)
	{
		return false;
	}
	ll s = p - 1;
	while (s % 2 == 0)
	{
		s /= 2;
	}
	for (int i = 0; i < iteration; i++)
	{
		ll a = rand() % (p - 1) + 1, temp = s;
		ll mod = modulo(a, temp, p);
		while (temp != p - 1 && mod != 1 && mod != p - 1)
		{
			mod = mulmod(mod, mod, p);
			temp *= 2;
		}
		if (mod != p - 1 && temp % 2 == 0)
		{
			return false;
		}
	}
	return true;
}
int iteration = 5;
int ans = 0;
void solve(int n, string s)
{
	//while (ans <50)
	{
		if (n == 16)
		{
			if (s[0] == '1' && s[15] == '1')
			{
				ll tmp = 0, pw = 1;
				int flag = 0;
				for (ll i = 2; i <= 10; ++i)
				{
					tmp = 0;
					pw = 1;
					for (int j = 15; j >= 0; --j)
					{
						tmp = tmp + (s[j] - '0') * pw;
						pw = pw*i;
					}
					if (Miller(tmp, iteration))
					{
						flag = 1;
						break;
					}
				}
				if (flag == 0)
				{
					++ans;
					cout << s << " ";
					for (int i = 2; i <= 10; ++i)
					{
						tmp = 0;
						pw = 1;
						for (int j = 15; j >= 0; --j)
						{
							tmp = tmp + (s[j] - '0') * pw;
							pw = pw*i;
						}
						for (ll j = 2;j<sqrt(tmp); ++j)
						{
							if (tmp%j == 0)
							{
								cout << j << " ";
								break;
							}
						}
						cout << "\n";
					}
				}
			}
		}
		else
		{
			solve(n + 1, s + '0');
			solve(n + 1, s + '1');
		}
	}
}
//Main
int main()
{
	ll num;
	//string s = "";
	//solve(0, s);
	for (int i = 0; i < 50; ++i)
	{
		string s;
		cin >> s;
		ll tmp = 0;
		ll pw = 0;
		for (int i = 2; i <= 10; ++i)
		{
			tmp = 0;
			pw = 1;
			int j;
			for (int j = 15; j >= 0; --j)
			{
				tmp = tmp + (s[j] - '0') * pw;
				pw = pw*i;
			}
			cin >> j;
			if (tmp%j != 0)
				cout << "yolo" << s << endl;
			cout << "\n";
		}
	}
	return 0;
}