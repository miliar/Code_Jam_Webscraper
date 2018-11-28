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
int a[maxn][maxn], b[maxn][maxn];
int rows[maxn], cols[maxn];

void solve(int &testCase) {
	printf("Case #%d: ", ++testCase);
	int h, w;
	scanf("%d%d", &h, &w);
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			int x;
			scanf("%d", &x);
			a[i][j] = b[j][i] = x;
		}
	}
	for (int i = 0; i < h; i++)
		rows[i] = *max_element(a[i], a[i] + w);
	for (int i = 0; i < w; i++)
		cols[i] = *max_element(b[i], b[i] + h);
	bool ok = 1;
	for (int i = 0; ok && i < h; i++)
		for (int j = 0; j < w; j++)
			if (min(rows[i], cols[j]) != a[i][j]) {
				ok = 0;
				break;
			}
	printf(ok ? "YES\n" : "NO\n");
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
