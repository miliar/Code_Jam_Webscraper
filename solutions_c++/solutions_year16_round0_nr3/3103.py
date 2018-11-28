#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define INF 0x3f3f3f3f
#define MAXPRIME 40000000

const int N = 16, J = 50;

vector<ll> primes;
void sieve(ll n)
{
	bitset<MAXPRIME> isPrime;
	isPrime.set();
	isPrime[0] = isPrime[1] = 0;
	for(ll i=2; i<n; ++i)
		if(isPrime[i])
		{
			for(ll j=i*i; j<n; j+=i) isPrime[j] = 0; 
			primes.pb(i);
		}
}

void print_mask(ll mask)
{
	for(int i=N-1; i>=0; --i)
	{
		if(mask & (1LL << i)) putchar('1');
		else putchar('0');
	}
}

vector<ll> get_divisors(ll mask)
{
	vector<ll> ret;
	for(ll base=2; base<=10; ++base)
	{
		ll x = 0, k = 1;
		for(int i=0; i<N; ++i, k *= base)
			if(mask & (1LL << i))
				x += k;
				
		bool is_prime = 1;
		for(int i=0; is_prime && i<(int)primes.size(); ++i)
		{
			if(primes[i] >= x) break;

			if((x % primes[i] == 0))
			{
				is_prime = 0;
				ret.pb(primes[i]);
			}
		}

		if(is_prime) return ret;
	}
	return ret;
}

int main()
{
	sieve(MAXPRIME);

	puts("Case #1:");
	
	int cnt = J;
	for(ll mask=0; cnt && (mask < (1 << N)); ++mask)
	{
		if((mask & (1)) && (mask & (1LL << (N-1))))
		{
			vector<ll> divisors = get_divisors(mask);
			if((int)divisors.size() == 9)
			{
				cnt--;
				print_mask(mask);
				for(int i=0; i<(int)divisors.size(); ++i) printf(" %lld", divisors[i]);
				puts("");
			}
		}
	}

	return 0;
}
