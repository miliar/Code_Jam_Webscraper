#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <cassert>
#include <limits>
#include <functional>
#include <random>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) __typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }

vector<bool> isprime;
vector<int> primes;
void sieve(int n) {
	if((int)isprime.size() >= n + 1) return;
	isprime.assign(n + 1, true);
	isprime[0] = isprime[1] = false;
	int sqrtn = (int)(sqrt(n * 1.) + .5);
	for(int i = 2; i <= sqrtn; i ++) if(isprime[i]) {
		for(int j = i * i; j <= n; j += i)
			isprime[j] = false;
	}
	primes.clear();
	for(int i = 2; i <= n; i ++) if(isprime[i])
		primes.push_back(i);
}

int main() {
	sieve(100000);
	default_random_engine re;
	bernoulli_distribution dist;
	int T;
	scanf("%d", &T);
	for(int ii = 0; ii < T; ++ ii) {
		int N; int J;
		scanf("%d%d", &N, &J);
		printf("Case #%d:\n", ii + 1);
		set<uint64_t> vis;
		int num = 0;
		while(num < J) {
			uint64_t v = 1 | uint64_t(1) << (N - 1);
			rep(i, N - 2)
				v |= uint64_t(dist(re)) << (i + 1);
			if(!vis.emplace(v).second)
				continue;
			vi divisors;
			rer(base, 2, 10) {
				for(int p : primes) {
					if(p > 10000 || p >= v) break;
					int rem = 0;
					rep(i, N) {
						int digit = v >> (N - 1 - i) & 1;
						rem = (rem * base + digit) % p;
					}
					if(rem == 0) {
						divisors.push_back(p);
						break;
					}
				}
				if(divisors.size() != base - 1)
					break;
			}
			if(divisors.size() == 9) {
				rep(i, N)
					putchar('0' + (v >> (N - 1 - i) & 1));
				for(int d : divisors)
					printf(" %d", d);
				puts("");
				++ num;
			}
		}
	}
	return 0;
}
