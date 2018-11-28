#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define DEBUG(x) cout << ">>> " << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)

#define INF (1<<29)
typedef long long ll;

const int MAXN = 2300;

int T, N, A[MAXN], B[MAXN];

vector<int> edges[MAXN];
bool done[MAXN];
int last[MAXN];
int res[MAXN];
int ord[MAXN], ordI;

void topo(int i) {
	if (done[i]) return;
	for (int j : edges[i]) {
		topo(j);
	}
	done[i] = true;
	ord[ordI++] = i;
}

int main() {
	scanf("%d", &T);
	REP(t,T) {
		REP(i, MAXN) edges[i].clear();
		REP(i, MAXN) done[i] = false;
		scanf("%d", &N);
		REP(i,N) scanf("%d", A+i);
		REP(i,N) scanf("%d", B+i);
		REP(i,N+1) last[i] = -1;
		REP(i,N) {
			if (A[i] != 1) {
				int l = last[A[i]-1];
				edges[i].push_back(l);
				l = last[A[i]];
				if (l != -1) edges[l].push_back(i);
			}
			last[A[i]] = i;
		}
		REP(i,N+1) last[i] = -1;
		FORD(i,N-1,0) {
			if (B[i] != 1) {
				int l = last[B[i]-1];
				edges[i].push_back(l);
				l = last[B[i]];
				if (l != -1) edges[l].push_back(i);
			}
			last[B[i]] = i;
		}
		REP(i,N) sort(edges[i].begin(), edges[i].end());
		ordI = 0;
		REP(i,N) topo(i);
		REP(i,N) res[ord[i]] = i;
		printf("Case #%d:", t+1);
		REP(i,N) printf(" %d", res[i]+1);
		printf("\n");
	}
	return 0;
}
