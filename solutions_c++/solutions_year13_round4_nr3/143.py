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

vvi es;
int n;

const int maxn = 2001;
int a[maxn];

int prevVal[maxn];
int used[maxn];

int perm[maxn], cnt;

int ans[maxn];

void dfs(int v) {
  used[v] = 1;
  for (int it = 0; it < sz(es[v]); it++) {
  	int u = es[v][it];
  	if (used[u])
  		continue;
  	dfs(u);
  }
  perm[cnt++] = v;
}

void solve(int testCase) {
	printf("Case #%d: ", testCase);
	scanf("%d", &n);
	es = vvi(n);
	for (int rev = 1; rev >= 0; rev--) {
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		if (rev)
			reverse(a, a + n);
		//for (int i = 0; i < n; i++)
		//	eprintf("%d%c", a[i], " \n"[i == n - 1]);
		for (int i = 1; i <= n; i++)
			prevVal[i] = -1;
		for (int i = n - 1; i >= 0; i--) {
			int curVal = a[i];	
			//eprintf("%d\n", curVal);	
			if (prevVal[curVal] != -1) {
				int s = prevVal[curVal], t = i;
				if (rev)
					s = n - 1 - s, t = n - 1 - t;
				//eprintf("%d >= %d\n", s , t);

				es[s].pb(t);
			}
			if (curVal >= 2) {
				int s = i, t = prevVal[curVal - 1];
				assert(t != -1);
				if (rev)
					s = n - 1 - s, t = n - 1 - t;
				es[s].pb(t);
				//eprintf("%d >= %d\n", s, t);
			}
			prevVal[curVal] = i;
		}            
	}
	for (int i = 0; i < n; i++)
		sort(es[i].begin(), es[i].end());

	for (int i = 0; i < n; i++)
		used[i] = 0;
	cnt = 0;
	for (int i = 0; i < n; i++)
		if (!used[i])
			dfs(i);
	assert(cnt == n);
	for (int i = 0; i < n; i++)
		ans[perm[i]] = i + 1;
	for (int i = 0; i < n; i++)
		printf("%d%c", ans[i], " \n"[i == n - 1]);
	//exit(0);
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
