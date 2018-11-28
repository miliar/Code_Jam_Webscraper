#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cassert>
#include <ctime>


using namespace std;

#ifdef WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<ll> vll;
typedef vector<vll> vvll;

ll rdtsc() {
    ll tmp;
    asm("rdtsc" : "=A"(tmp));
    return tmp;
}

#define TASKNAME "text"
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
#define INF ((int)1e9)
#define sqr(x) ((x) * (x))         
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())

const int maxn = 22;
int prev[maxn];
char s[maxn];
double d[1 << maxn];

void solve(int testCase) {
	printf("Case #%d: ", testCase);
	scanf("%s", s);
	int n = strlen(s);
	assert(n <= 20);
	reverse(s, s + n);
	int mask0 = 0;
	for (int i = 0; i < n; i++)
		if (s[i] == 'X')
			mask0 ^= (1 << i);
	d[(1 << n) - 1] = 0;
	for (int mask = (1 << n) - 2; mask >= mask0; mask--) {
		d[mask] = 0;
		memset(prev, -1, sizeof(prev));
		int curprev = -1;
		for (int iter = 0; iter < 2; iter++) {
			for (int i = 0; i < n; i++) {
				if (!((mask >> i) & 1))
					curprev = i;
				if (curprev != -1)
					prev[i] = curprev;	
			}
		}
		for (int boat = 0; boat < n; boat++) {
			assert(prev[boat] != -1);
			int dist = boat - prev[boat];
			if (dist < 0)
				dist += n;
			d[mask] += d[mask ^ (1 << prev[boat])] + n - dist;
		}
		d[mask] /= n;
		//eprintf("d[%d] = %.3lf\n", mask, d[mask]);
	}

	printf("%.18lf\n", d[mask0]);
}

int main() {
	srand(rdtsc());
#ifdef DEBUG
	freopen(TASKNAME".in", "r", stdin);
	freopen(TASKNAME".out", "w", stdout);
#endif
	
	int testCase = 0, n;
	while (scanf("%d", &n) >= 1) {
		for (int i = 0; i < n; i++)
			solve(++testCase);
		//break;
	}
	return 0;
}
