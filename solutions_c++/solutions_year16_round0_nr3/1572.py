#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <set>
#include <limits.h>

#define inp(x) scanf("%d",&x)
#define inp_l(x) scanf("%lld",&x)
#define inp_d(x) scanf("%lf",&x)
#define MOD 1000000007
const int L1D_CACHE_SIZE = 32768;

using namespace std;

typedef long long int ll;
typedef vector <int> VI;
typedef vector <long long int> VLL;
typedef pair<int,int> PI;
typedef pair<ll,ll> PLL;

vector <int> P;
int cnt;
void segmented_sieve(int64_t limit, int segment_size = L1D_CACHE_SIZE)
{
	int sqrt = (int) std::sqrt((double) limit);
	cnt = (limit < 2) ? 0 : 1;
	int64_t s = 2;
	int64_t n = 3;
	P.push_back(2);
	// vector used for sieving
	std::vector<char> sieve(segment_size);

	// generate small primes <= sqrt
	std::vector<char> is_prime(sqrt + 1, 1);
	for (int i = 2; i * i <= sqrt; i++)
		if (is_prime[i])
			for (int j = i * i; j <= sqrt; j += i)
				is_prime[j] = 0;

	std::vector<int> primes;
	std::vector<int> next;

	for (int64_t low = 0; low <= limit; low += segment_size)
	{
		std::fill(sieve.begin(), sieve.end(), 1);

		// current segment = interval [low, high]
		int64_t high = std::min(low + segment_size - 1, limit);

		// store small primes needed to cross off multiples
		for (; s * s <= high; s++)
		{
			if (is_prime[s])
			{
				primes.push_back((int) s);
				next.push_back((int)(s * s - low));
			}
		}
		// sieve the current segment
		for (std::size_t i = 1; i < primes.size(); i++)
		{
			int j = next[i];
			for (int k = primes[i] * 2; j < segment_size; j += k)
				sieve[j] = 0;
			next[i] = j - segment_size;
		}

		for (; n <= high; n += 2)
			if (sieve[n - low]) // n is a prime
			{
				P.push_back(n);
				cnt++;
			}
	}

	//std::cout << cnt << " primes found." << std::endl;
}


string tostr(ll x)
{
	if(x==0)
		return "0";
	string ans="",rev="";
	while(x!=0)
	{
		if(x%2)
			ans= ans + "1";
		else
			ans = ans + "0";
		x/=2;
	}
	int i;
	for(i = ans.size() - 1; i >= 0; i--)
	{
		rev = rev + ans[i];
	}
	return rev;
}

ll tobase(string str, ll b)
{
	int i,l;
	l = str.size();
	ll p = 1ll,ans = 0ll;
	for(i = l-1; i>=0; i--)
	{
		if(str[i] == '1')
		{
			ans += p;
		}
		p *= b;
	}
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	segmented_sieve(100000);
	int t, n, j, i, l, k, bb, p, c, ans, z;
	bool flag;
	cin >> t >> n >> j;
	string str;
	ll x = (1ll << (n-1)) + 1, tmp;
	int arr[11];
	bb = 0;
	for(z = 1; z <= t; z++)
	{
		cout << "Case #" << z << ":" << endl;
		while(bb < j)
		{
			//cout << x << endl;
			/*flag = true;
			for(k = 2; k <= 10; k++)
			{
				tmp = x;
				c = 1;
				ans = 0;
				while(tmp!=0)
				{
					p = tmp % 2;
					if(p == 1)
					{
						ans = (ans + c) % 6;
					}
					c = (c*k) % 6;
					tmp/=2;
				}
				//cout << x << " " << k << " " << ans << endl;
				if(ans==1 || ans==5)
				{
					flag = false;
					break;
				}
			}
			if(flag)
			{
				cout << tostr(x) << " ";*/
			flag = true;
			for(k = 2; k <= 10; k++)
			{
				arr[k] = -1;
				for(l = 0; l < cnt && P[l] * P[l] <= x; l++ )
				{
					tmp = x;
					ans = 0;
					c = 1;
					while(tmp!=0)
					{
						p = tmp % 2;
						if(p == 1)
						{
							ans = (ans + c)%P[l];
						}
						c = (c*k) % P[l];
						tmp/=2;
					}
					if(ans == 0)
					{
						arr[k] = P[l];
						break;
					}
				}
				if(arr[k] == -1)
				{
					flag = false;
					break;
				}
			}
			if(flag)
			{
				cout << tostr(x) << " ";
				for(k = 2; k <= 10; k++)
				{
					cout << arr[k] << " ";
				}
				cout << endl;
				bb++;
			}
			x += 2ll;
		}
	}
	return 0;
}

