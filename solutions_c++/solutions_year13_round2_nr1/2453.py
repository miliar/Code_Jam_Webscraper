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

const int maxn = 100;
int a[maxn];

void solve(int &testCase) {
	int A, n;
	scanf("%d%d", &A, &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	sort(a, a + n);
	int ans = INF;
	int pos = 0;
	int bal = 0;
	while (1) {
		while (pos < n && a[pos] < A)
			A += a[pos], pos++;
		ans = min(ans, bal + n - pos);
		if (pos == n)
			break;
		if (A == 1)
			break;	
		A = 2 * A - 1;
		++bal;
	}

	printf("Case #%d: %d\n", ++testCase, ans);
}

int main() {
	srand(rdtsc());
#ifdef DEBUG
	freopen(TASKNAME".in", "r", stdin);
	freopen(TASKNAME".out", "w", stdout);
#endif
	
	int testCase = 0;
	int maxt;
	while (scanf("%d", &maxt) >= 1) {
		for (int i = 0; i < maxt; i++)
			solve(testCase);
		//break;
	}
	return 0;
}
