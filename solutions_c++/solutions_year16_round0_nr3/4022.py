#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<stdlib.h>
#include<time.h>

#define ll long long
using namespace std;
int n, j, tmp;
char arr[20];
long long add[20];
vector<char> makenum;
int cnt;
bool poss = false;
bool side;

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
long long modular_pow(long long base, int exponent,
	long long modulus)
{
	/* initialize result */
	long long result = 1;

	while (exponent > 0)
	{
		/* if y is odd, multiply base with result */
		if (exponent & 1)
			result = (result * base) % modulus;

		/* exponent = exponent/2 */
		exponent = exponent >> 1;

		/* base = base * base */
		base = (base * base) % modulus;
	}
	return result;
}

long long __gcd(long long x, long long y)
{
	long long t;
	while (y != 0)
	{
		t = x%y;
		x = y;
		y = t;
	}
	return x;
}

bool isPrime(long long num)
{
	for (int i = 2; i*i<=num; i++)
	{
		if (num%i == 0) return false;
	}
	return true;
}

long long f(int base)
{
	long long sum = 0;
	for (int i = 0; i < n; i++)
	{
		if (arr[i] == '1') sum += (long long)powl(base, n - i - 1);
	}
	return sum;
}

bool check(long long n){
	if (n <= 3) {
		return n > 1;
	}
	if (n % 2 == 0 || n % 3 == 0) {
		return false;
	}
	for (int i = 5; i*i<n; i += 6){
		if (n%i == 0 || n % (i + 2) == 0)
			return false;
	}
	return true;
}

void ff(int pos)
{
	if (poss) return;

	if (pos == n - 1)
	{
		arr[pos] = '1';
		memset(add, 0, sizeof(add));
		int i;
		side = true;
		int iteration = 15;
		for (i = 2; i < 10; i++)
		{
			long long chknum = f(i);
			//printf("%lld\n", chknum);

			if (Miller(chknum, iteration))
			{
				side = false;
				break;
			}

			long long k;
			for (k = 2; k*k <= chknum; k++)
			{
				if (chknum%k == 0)
				{
					add[i] = k;
					break;
				}
			}

			if (k*k > chknum)
			{
				side = false;
				break;
			}
			//add.push_back(PollardRho(chknum));
		}

		if (side && !Miller(atoll(arr), iteration))
		{
			long long pv = atoll(arr);
			long long k;
			for (k = 2; k*k <= pv; k++)
			{
				if (pv%k == 0)
				{
					add[10] = k;
					break;
				}
			}
			if (k*k > pv)
			{
				side = false;
			}
			else i++;
		}

		if (i == 11)
		{
			printf("%s ", arr);
			for (int k = 2; k <= 10; k++) printf("%lld ", add[k]);
			puts("");
			cnt++;
		}

		if (cnt == j) poss = true;


		//for (int k = 0; k < add.size(); k++) add[k] = 0;

		return;
	}

	if (pos == 0)
	{
		arr[pos] = '1';
		ff(pos + 1);
	}
	else
	{
		arr[pos] = '0';
		ff(pos + 1);
		arr[pos] = '1';
		ff(pos + 1);
	}
}



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++)
	{
		printf("Case #%d:\n", T);
		scanf("%d%d", &n, &j);
		ff(0);
	}
}