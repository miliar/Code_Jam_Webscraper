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

const int maxlen = 7, maxhalf = 4, maxTenHalf = (int)1e4;
int rev[maxTenHalf];
char s[100];
ll ten[100];

inline bool ispalin(ll x) {
	sprintf(s, LLD, x);
	int len = strlen(s);
	for (int i = 0; i < len / 2; i++)
		if (s[i] != s[len - 1 - i])
			return 0;
	return 1;
}

void solve(int &testCase) {
	printf("Case #%d: ", ++testCase);
	ll l, r;
	scanf(LLD LLD, &l, &r);
	ll ans = 0;
	for (int len = 1; len <= maxlen; len++) {
		int halflen = (len + 1) / 2;
// 		eprintf("---%lld\n", ten[halflen]);
		for (int i = ten[halflen - 1]; i < ten[halflen]; i++) {
			ll x = rev[i];
			if (len & 1)
				x /= 10;
			x = x * ten[halflen] + i;
			x *= x;
			if (l <= x && x <= r && ispalin(x)) {
// 				eprintf("%lld\n", x);
				ans++;
			}
		}
	}
	printf(LLD"\n", ans);
// 	exit(0);
}

void init() {
	ten[0] = 1;
	for (int i = 1; i <= 15; i++)
		ten[i] = ten[i - 1] * 10;
	
	for (int i = 1; i < 1e4; i++) {
		sprintf(s, "%d", i);
		int len = strlen(s);
		reverse(s, s + len);
		sscanf(s, "%d", &rev[i]);
	}
}

int main() {
	srand(rdtsc());
#ifdef DEBUG
	freopen(TASKNAME".in", "r", stdin);
	freopen(TASKNAME".out", "w", stdout);
#endif
	
	init();
	
	int testCase = 0;
	int n;
	while (scanf("%d", &n) >= 1) {
		for (int i = 0; i < n; i++)
			solve(testCase);
		//break;
	}
	return 0;
}
