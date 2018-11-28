/*input
1
6 10
*/
#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int ull;
typedef long long int lli;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define rep(i,n) for(int i = 0; i < n; i++)
#define INF    0x3f3f3f3f
#define NEGINF 0xC0C0C0C0
#define LINF   0x3f3f3f3f3f3f3f3fLL
#define all(v) v.begin(), v.end()
#define NULO -1
#define EPS 1e-10
#define PI 2 * acos(0)
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s))
#define F first
#define S second

inline int cmp(double x, double y = 0, double tol = EPS)
{ return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }

void arquivo()
{
	freopen("C.in", "rt", stdin);
	freopen("C.out", "wt", stdout);
}

bitset<10000010> bs;
lli size;
vector<int> primes;
bool isPrime(lli n)
{
	if(n <= size)
		return bs[n];
	for(int i = 0; i < primes.size(); i++)
		if(n % primes[i] == 0)
			return false;
	return true;
}

void sieve(lli up)
{
	size = up + 1;
	bs.set();
	bs[0] = bs[1] = 0;
	for(lli i = 2; i <= size; i++)
	{
		if(bs[i])
		{
			for(lli j = i * i; j <= size; j += i)
				bs[j] = 0;
			primes.push_back((int)i);
		}
	}
}

vector<pair<string, vector<lli> > > base;

void valid(string s, int MAX)
{
	if(base.size() == MAX)
		return;
	vector<lli> v;
	for(lli b = 2LL; b <= 10LL; b++)
	{
		lli num = 0;
		for(lli i = s.size() - 1, base = 1; i >= 0; i--, base *= b)
			num += ((lli)(s[(int)i] - '0')) * base;
		v.push_back(num);
		if(isPrime(num))
			return;
	}
	for(int i = 0; i < v.size(); i++)
	{
		if(v[i] % 2LL == 0)
			v[i] = 2LL;
		else
			for(lli j = 3LL; j < v[i]; j += 2LL)
				if(v[i] % j == 0)
				{
					v[i] = j;
					break;
				}
	}
	base.push_back(make_pair(s, v));
}
// 5 13 147 31 43 1121 73 77 629
void gerar(string s, int n, int MAX)
{
	if(s.size() == n - 1)
	{
		s += "1";
		valid(s, MAX);
		return;
	}
	gerar(s + "0", n, MAX);
	gerar(s + "1", n, MAX);
}

int main()
{	
	
	arquivo();
	sieve(10000000);

	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		base.clear();

		int n, j;
		scanf("%d %d", &n, &j);
		gerar("1", n, j);

		printf("Case #%d:\n", t);
		for(int i = 0; i < j && i < base.size(); i++)
		{
			printf("%s", base[i].F.c_str());
			for(auto x : base[i].S)
					printf(" %lld", x);
			printf("\n");

		}


	}
	return 0;
}