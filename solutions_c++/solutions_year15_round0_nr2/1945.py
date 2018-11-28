#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

#include<algorithm>
#include<utility>
#include<string>

#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>

using namespace std;

#define REP(i,N) for (int i = 0; i < (N); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FORD(i, b, a) for (int i = (b) - 1; i >= a; i--)
#define DP(arg...) fprintf(stderr, ## arg) //COMPILER SPECIFIC!!!

typedef long long ll;

int T;

int D;
int P[10000];
int F[1001][1001];

void compute(int v, int t) {
	if (F[v][t] != -1) return;
	
	if (v <= t) F[v][t] = 0;
	else {
		int p1 = v/2;
		int p2 = v - p1;
		int x1 = v - t;
		compute(p1,t);
		compute(p2,t);
		compute(x1,t);
		F[v][t] = min(1 + F[p1][t] + F[p2][t], 1 + F[x1][t]);
	}
}

void precompute() {
	for (int v = 0; v <= 1000; v++)
		for (int t = 1; t <= 1000; t++)
			F[v][t] = -1;
	for (int v = 0; v <= 1000; v++)
		for (int t = 1; t <= 1000; t++)
			compute(v,t);
}

int try_t(int t) {
	int spec_d = 0;
	REP(d,D) {
		int v = P[d];
		spec_d += F[v][t];
	}
	return spec_d + t;
}

void solve(int _case) {
	scanf("%d", &D);
	int sol = 1<<20;
	REP(d,D) scanf("%d", &P[d]);

	for (int t = 1; t <= 1000; t++) {
		sol = min(sol,try_t(t));
	}
	printf("Case #%d: %d\n", _case, sol);
}

int main() {
	precompute();
	scanf("%d", &T);
	REP(t,T) solve(t+1);
	return 0;
}
