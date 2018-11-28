#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>

using namespace std;
using ll = __int128;

void SolveCase(int caseId);
bool Try(ll x);
ll ToValue(ll x, ll base);
bool IsPrime(ll x);
bool MaR(ll x, ll n);
ll NonTrivalDivisor(ll x);
int Print(ll x);
void MakeSieve();

const ll Lim = 100000;
bool Sieve[Lim + 1];
vector<ll> Primes;

int main()
{
	MakeSieve();
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
		SolveCase(i);
	return 0;
}

void SolveCase(int caseId)
{
	int N, J;
	scanf("%d%d", &N, &J);
	printf("Case #%d:\n", caseId);
	
	ll x = (((ll)1)<<(N-1)) + 1;
	while (J > 0)
	{
		if (Try(x))
			--J;
		x += 2;
	}
}

bool Try(ll x)
{
	ll values[11];
	ll divs[11];
	for(ll base = 2; base <= 10; ++base)
	{
		values[base] = ToValue(x, base);
		divs[base] = NonTrivalDivisor(values[base]);
		if(divs[base] == 0)
			return false;
	}
	Print(values[10]);
	for(ll base = 2; base <= 10; ++base)
		Print(divs[base]);
	puts("");
	return true;
}

int Print(ll x)
{
	if (x == 0)
		return printf("0 ");
	char str[40] = {0};
	char *s = str + sizeof(str) - 1;
	while (x != 0)
	{
		*--s = "0123456789"[x % 10];
		 x /= 10;
	}
	return printf("%s ", s);
}

ll ToValue(ll x, ll base)
{
	ll value = 0;
	ll p = 1;
	while(x > 0)
	{
		if(x&1)
			value += p;
		p *= base;
		x >>= 1ll;
	}
	return value;
}

ll NonTrivalDivisor(ll x)
{
	if((x & 1) == 0)
		return 2;
		
	for(ll i : Primes)
		if(i*i >= x)
			break;
		else if(x%i == 0)
			return i;
			
	//for(ll i = Primes.back() + 2; i*i <= x; i+=2)
	//	if(x%i == 0)
	//		return i;
	return 0;
}

void MakeSieve()
{
	Sieve[0] = Sieve[1] = true;
	bool cnt = true;
	int n = Lim;
	for(int i = 2; i <= n; ++i)
	{
		if(!Sieve[i])
		{
			Primes.push_back(i);
			if(cnt)
			{
				int x = i*i;
				if(x <= n)
					for(; x <= n; x+=i)
						Sieve[x] = true;
				else
					cnt = false;
			}
		}
	}
}

