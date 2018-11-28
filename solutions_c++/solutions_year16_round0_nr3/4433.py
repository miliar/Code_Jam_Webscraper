#include <iostream> 
#include <vector>
using namespace std;

typedef long long ll;

////////////////////////////////////////////////////////////////////////////////

ll r[12] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37 };

ll mult(ll a, ll b, ll n)
{
	ll res = 0;
	while (b > 0)
	{
		if (b % 2 == 1) res += a, res %= n;
		a += a, a %= n;
		b /= 2;
	}
	return res;
}

ll power(ll a, ll b, ll n)
{
	ll res = 1;
	while (b > 0)
	{
		if (b % 2 == 1) res = mult(res, a, n);
		a = mult(a, a, n);
		b /= 2;
	}
	return res;
}

bool RB(ll n)
{
	if (n == 2) return 1;
	
	int exp = 0;
	ll u = n - 1;
	
	while (!(u & 1ll)) exp ++, u /= 2;
			
	for (int i = 0; i < 12 and r[i] < n - 1; i++)
	{	
		ll a = r[i];
		ll x = power(a, u, n);
		
		bool minus = false;
		
		if (x == 1 or x == n - 1) continue;
		for (int j = 0; j < exp - 1; j++)
		{
			x = mult(x, x, n) % n;
			if (x == 1) return 0;
			if (x == n - 1) { minus = true; break; }
		}
		
		if (minus) continue;
		return 0;
	}
	return 1;
}

//		cin >> n;
//		
//		bool prime = RB();
//		if (prime) cout << "YES\n";
//		else cout << "NO\n";

////////////////////////////////////////////////////////////////////////////////

const int SIZE = 20 * 1000 * 1000;
const int N = 16;
const int MASK_SIZE = 14;
const int J = 50;
int found_cnt;

int sieve[SIZE];

int divider_sqrt(ll n) // 1 if prime
{
	for (int i = 2; i * i <= n; i++)
		if (n % i == 0)
			return i;
	return 1;
}

void create_sieve()
{
	for (int i = 2; i * i < SIZE; i++)
	{
		if (sieve[i] > 0)
			continue;
		for (int j = i * i; j < SIZE; j += i)
			sieve[j] = i;
	}
}

ll to_system(int x, int sys)
{
	ll power = sys;
	ll result = 1;
	for (int i = 0; i < MASK_SIZE; i++)
	{
		if (x & (1 << i))
		{
			result += power;
		}
		
		power *= sys;
	}	
	
	result += power;
	
	return result;
}

void print_mask(int mask)
{
	cout << 1;
	for (int i = MASK_SIZE - 1; i >= 0; i--)
		if (mask & (1 << i))
			cout << 1;
		else cout << 0;
	cout << 1;
}

int main()
{
	create_sieve();

	cout << "Case #1:\n";	
	for (int mask = 0; mask < (1 << MASK_SIZE); mask++)
	{
//		print_mask(mask);
//		cout << "\n";
		vector <int> dividers;
		for (int i = 2; i <= 10; i++)
		{
			ll x = to_system(mask, i);
			if (x < SIZE)
			{
				if (sieve[x] == 0)
					break;
				dividers.push_back(sieve[x]);
			}
			else
			{
				if (RB(x))
					continue;
				int divider = divider_sqrt(x);
				if (divider == 1)
					break;
				dividers.push_back(divider);
			}
		}		
		
		if (dividers.size() < 9)
			continue;
		
//		cout << found_cnt + 1 << ":\n";
		print_mask(mask);
		cout << " ";
		for (int i = 0; i < dividers.size(); i++)
			cout << dividers[i] << " ";
		cout << "\n";
		
//		for (int i = 2; i <= 10; i++)
//			cout << "  sys " << i << ": " << to_system(mask, i) << "\n";

		found_cnt++;
		
		if (found_cnt == J)
			break;
//		print_mask(mask);
//		cout << "\n";	
	}

	return 0;
}
