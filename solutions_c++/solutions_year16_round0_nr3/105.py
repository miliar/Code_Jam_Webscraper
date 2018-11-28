//TAG : 
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<algorithm>
#include<climits>
#include<functional>
#include<numeric>
#include<random>
#include<unordered_map>
#include<unordered_set>
using namespace std;
#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,j,n)  for(int (i)=(j),_n=(n); (i) < _n; (i)++)
#define FOR(i,a,b)  for(int _b=(b), (i)=(a); (i) <= _b; (i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define CLEAR(x) memset((x),0,sizeof(x))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define X first
#define Y second
#define MP make_pair
#define MT make_tuple
#define EPS 	(1e-9)
typedef pair<int, int>	PII;
typedef vector<int>		VI;
typedef unsigned int	uint;
typedef long long		LL;
typedef unsigned long long	ULL;
template<typename T> void check_max(T& a, T b) { if (a < b) a = b; }
template<typename T> void check_min(T& a, T b) { if (a > b) a = b; }
#ifdef _MSC_VER
#include "builtin_gcc_msvc.h"
#define gets	gets_s
#else
#define popcnt(x)	__builtin_popcount(x)
#define ctz(x)		__builtin_ctz(x)
#define clz(x)		__builtin_clz(x)
#define popcntll(x)	__builtin_popcountll(x)
#define ctzll(x)	__builtin_ctzll(x)
#define clzll(x)	__builtin_clzll(x)
#endif
mt19937 RE(random_device{}());
//[0,a), a not include,
template<typename T> T randNext(T a) {
	return uniform_int_distribution<T>(0, a - 1)(RE);
}
//[a,b] , a,b include
template<typename T> T randNext(T a, T b) {
	return uniform_int_distribution<T>(a, b)(RE);
}

#define MAX_PRIME	(10000000) //>2^16
#define PRIME_SIZE	(664579)

int pCount;
int prime[PRIME_SIZE];
bool sieve[MAX_PRIME + 1];//false means f(n) is prime.

void createPrime() {
	FOR(i, 2, (int)sqrt(MAX_PRIME))if (!sieve[i]) {
		for (int j = i*i; j <= MAX_PRIME; j += i)
			sieve[j] = true;
	}
	FOR(i, 2, MAX_PRIME)if (!sieve[i])
		prime[pCount++] = i;
}

void conv_bin(ULL n, char* s) {
	int len = 0;
	while (n > 0) {
		s[len++] = '0' + (n & 1);
		n >>= 1;
	}
	s[len] = 0;
	reverse(s, s + len);
}


int anyFactor(char* s, int len, int base) {
	//evaluate approximate value 
	double value = 0;
	rep(j, len)value = value*base + (s[j] - '0');
	LL sq = (LL)(sqrt(value) + 1e-1);
	int limit = min(pCount, (int)1e5);
	if (sq <= prime[pCount - 1])
		check_min(limit, upper_bound(prime, prime + pCount, (int)sq) - prime);
	
	REP(i, 0, limit) {
		int r = 0, p = prime[i];
		rep(j, len)r = (r*base + (s[j] - '0')) % p;
		if (r == 0)return p;
	}
	return 0;
}

int main()
{
	//create some primes
	createPrime();
	char line[101];
	int arr[11];
	unordered_set<string> table;

	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC)
	{
		printf("Case #%d:\n", T);
		int N, J; scanf("%d %d", &N, &J);
		const ULL mask = (1ULL << (N - 1)) + 1;
		const ULL L = 0, R = (1ULL << (N - 2));
		int try_cnt = 0;
		while (true) {
			//fprintf(stderr, "try %d, J=%d\n", try_cnt++, J);

			//try some random guess
			ULL j = mask | (randNext(L, R) << 1);
			conv_bin(j, line);
			
			string str(line);
			if (table.count(str) > 0)continue;
			table.insert(str);

			bool ok = true;
			FOR(k, 2, 10) {
				int f = anyFactor(line, N, k);
				if (f == 0) {
					ok = false; break;
				}
				arr[k] = f;
			}
			if (ok) {
				printf("%s", line);
				FOR(i, 2, 10)printf(" %d", arr[i]);
				puts("");
				if (--J == 0)break;
			}
		}
	}

	return 0;
}