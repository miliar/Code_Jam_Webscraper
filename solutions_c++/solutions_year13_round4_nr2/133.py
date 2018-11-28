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

ll firstValue(int n, ll p) {
	int tmp = -1;
	while ((1ll << (tmp + 1)) < ((1ll << n) + 1 - p))
		tmp++;
	++tmp;
	int k = n - tmp;
	return min((1ll << (k + 1)) - 2, (1ll << n) - 1);
}

ll secondValue(int n, ll p) {
	int tmp = 0;
	while ((1ll << (tmp + 1)) <= p)
		tmp++;
	int k = n - tmp;
	return (1ll << n) - (1ll << k);
}

void solve(int testCase) {
	printf("Case #%d: ", testCase);
	int n;
	ll p;
	scanf("%d%I64d", &n, &p);
	assert(0 <= firstValue(n, p) && firstValue(n, p) <= secondValue(n, p) && secondValue(n, p) <= (1ll << n) - 1);
	printf("%I64d %I64d\n", firstValue(n, p), secondValue(n, p));
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
