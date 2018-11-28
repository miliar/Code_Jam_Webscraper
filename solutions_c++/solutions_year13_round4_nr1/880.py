#include <iostream>
#include <cstdio>
#include <fstream>

#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <string>
#include <cstring>

#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <memory.h>
using namespace std;

#define fr(i, n) for (int i = 0; i < (int)(n); i++)
#define fb(i, n) for (int i = n - 1; i >= 0; i--)
#define all(a) (a).begin(), (a).end()
#define _(a, b) memset(a, b, sizeof(a))
#define mp make_pair
#define pb push_back
#define sz(v) ((int)(v).size())

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

inline int ni() { int a; scanf("%d", &a); return a; }
inline double nf() { double a; scanf("%lf", &a); return a; }
template <class T> void out(T a, T b) { bool first = true; for (T i = a; i != b; i++) { if (!first) printf(" "); first = false; cout << *i; } puts(""); }
template <class T> void outl(T a, T b) { for (T i = a; i != b; i++) cout << *i << "\n"; } 

const int MOD = 1000002013;
const int MAXN = 101;

struct eve {
	ll o, e, p;	
};

int T;
int N, M;
vector<eve> v;
ll cost, dist;
ll d[MAXN][MAXN];

inline int solve() {
	N = ni(); M = ni();
	cost = 0;
	v.resize(M);
	fr(i, M) {
		v[i].o = ni(); v[i].e = ni(); v[i].p = ni();			    	
		v[i].o--, v[i].e--;
		dist = v[i].e - v[i].o;
		dist--;
		cost += ((dist + 1) * N - dist * (dist + 1) / 2) * v[i].p;
		cost %= MOD;
	}
	
	_(d, 0);

	fr(i, M) {
		d[v[i].o][v[i].e] += v[i].p;
	}	
	fr(i, N) {
		for (int j = i + 1; j < N; j++) {
			if (d[i][j]) {
				for (int k = i + 1; k <= j && d[i][j]; k++) {
					for (int l = j + 1; l < N && d[i][j]; l++) {
						if (d[k][l]) {
							int mm = min(d[k][l], d[i][j]);
							d[i][j] -= mm;
							d[k][l] -= mm;
							d[i][l] += mm;
							d[k][j] += mm;
						}
					}
				}
			}
		}
	}

	ll cur = 0;
	fr(i, N) {
		for (int j = i + 1; j < N; j++) {
			dist = j - i;
			dist--;
			cur += ((dist + 1) * N - dist * (dist + 1) / 2) * d[i][j];
			cur %= MOD;
		}
	}

	return (cost - cur + MOD) % MOD;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);  
	T = ni();
	fr(test, T) {
		printf("Case #%d: %d\n", test + 1, solve());
	}
}
        