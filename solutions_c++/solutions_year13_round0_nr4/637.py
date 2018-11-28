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

const int maxn = 200;
int n;
int balance[maxn];
int info[maxn][2];
vvi inside;
int used[maxn];
int ans[maxn];

set<int> M;

bool go(int iter) {
	if (iter == n)
		return 1;
	int mask = 0;
	for (int i = 0; i < n; i++)
		if (used[i])
			mask |= (1 << i);
	if (M.count(mask))
		return 0;
	M.insert(mask);
	for (int i = 0; i < n; i++) {
		if (used[i] || !balance[info[i][0]])
			continue;
		balance[info[i][0]]--;
		for (int j = 0; j < info[i][1]; j++)
			balance[inside[i][j]]++;
		used[i] = 1;
		ans[iter] = i;
		if (go(iter + 1))
			return 1;
		used[i] = 0;
		balance[info[i][0]]++;
		for (int j = 0; j < info[i][1]; j++)
			balance[inside[i][j]]--;
	}
	return 0;
}

void solve(int &testCase) {
	eprintf("testCase = %d\n", testCase);
	printf("Case #%d: ", ++testCase);
	memset(balance, 0, sizeof(balance));
	int k;
	scanf("%d%d", &k, &n);
	for (int i = 0; i < k; i++) {
		int x;
		scanf("%d", &x);
		balance[--x]++;
	}
	inside.resize(n);
	for (int i = 0; i < n; i++) {
		scanf("%d%d", &info[i][0], &info[i][1]);
		info[i][0]--;
		inside[i].resize(info[i][1]);
		for (int j = 0; j < info[i][1]; j++)
			scanf("%d", &inside[i][j]), inside[i][j]--;
	}
	memset(used, 0, sizeof(used));
	M.clear();
	if (!go(0))
		printf("IMPOSSIBLE\n");
	else {
		for (int i = 0; i < n; i++)
			printf("%d%c", ans[i] + 1, " \n"[i == n - 1]);
	}
}

int main() {
	srand(rdtsc());
#ifdef DEBUG
	freopen(TASKNAME".in", "r", stdin);
	freopen(TASKNAME".out", "w", stdout);
#endif
	
	int testCase = 0;
	int n;
	while (scanf("%d", &n) >= 1) {
		for (int i = 0; i < n; i++)
			solve(testCase);
		//break;
	}
	return 0;
}
