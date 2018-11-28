#include <bits/stdc++.h>
using namespace std;

int n, m, k;
int a[55];
int c[55];

typedef long long ll;

ll powMod(ll x, ll k, ll m) {
  if (k == 0)     return 1;
  if ((k & 1))    return x*powMod(x, k-1, m) % m;
  else            return powMod(x*x % m, k/2, m);
}

bool suspect(ll a, ll s, ll d, ll n) {
   ll x = powMod(a, d, n);
   if (x == 1) return true;
   for (int r = 0; r < s; ++r) {
      if (x == n - 1) return true;
      x = x * x % n;
   }
   return false;
}
// {2,7,61,-1}                 is for n < 4759123141 (= 2^32)
// {2,3,5,7,11,13,17,19,23,-1} is for n < 10^16 (at least)
bool isPrime(ll n) {
   if (n <= 1 || (n > 2 && n % 2 == 0)) return false;
   ll test[] = {2,3,5,7,11,13,17,19,23,-1};
   ll d = n - 1, s = 0;
   while (d % 2 == 0) ++s, d /= 2;
   for (int i = 0; test[i] < n && test[i] != -1; ++i)
      if (!suspect(test[i], s, d, n)) return false;
   return true;
}

ll convert(int x)
{
	ll s = 0;
	ll d = 1;
	for(int i = n; i > 0; i--)
	{
		if(a[i] == 1)
			s += d;
		d *= x;
	}
	return s;
}

void process(int x);

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> n;
	cin >> n >> m;
	cout << "Case #1:\n";
	memset(a, 0, sizeof a);
	k = 0;
	/*for(int i = 2; i < 100000000; i++)
		if(isPrime(i)) 
		{
			pr[k] = i;
			k++;
		}*/
	a[1] = 1; a[n] = 1;
	process(2);
	return 0;
}

void process(int x)
{
	if(m <= 0) exit;
	if(x == n)
	{
		bool ok = true;
		for(int i = 2; i <= 10; i++)
			if(isPrime(convert(i))) ok = false;
		if(m > 0 && ok)
		{
			for(int i = 2; i <= 10; i++)
			{
				ll v = convert(i);
				int u = 2;
				while(u < 1000000 && v % u != 0)
					u++;
				c[i] = u;
				if(u == 1000000) break;
			}
			bool kt = true;
			for(int i = 2; i <= 10; i++)
				if(c[i] == 1000000) kt = false;
			if(kt)
			{
				for(int i = 1; i <= n; i++) cout << a[i];
				for(int i = 2; i <= 10; i++) cout << " " << c[i];
				cout << "\n";
				m--;
			}
		}
	}
	else
	for(int i = 0; i < 2; i++)
	{
		a[x] = i;
		process(x + 1);
	}
}