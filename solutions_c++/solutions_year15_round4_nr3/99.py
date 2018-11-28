#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <assert.h>
#include <math.h>
#include <string.h>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define FOREACH(it,vec) for(typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); it++)
#define MODD(a,b) (((a)%(b)+(b))%(b))
#define REP(i,a,n) for (int i = (a); i < (n); i++)

const int DOTS = 1000000;
const int INF = 1E9; // $\infty$: be careful to make this big enough!!!
int S; // source
int T; // sink
int FN; // number of nodes
int FM; // number of edges (initialize this to 0)
// ra[a]: edges connected to a (NO MATTER WHICH WAY!!!); clear this in the beginning
VI ra[DOTS];
int kend[DOTS], cap[DOTS]; // size: TWICE the number of edges
// Adds an edge from a to b with capacity c and returns the number of the new edge
int addedge(int a, int b, int c) {
	int i = 2*FM;
	kend[i] = b;
	cap[i] = c;
	ra[a].push_back(i);
	kend[i+1] = a;
	cap[i+1] = 0;
	ra[b].push_back(i+1);
	FM++;
	return i;
}

bool fou[DOTS];
PII pre[DOTS];
// Returns the maximum flow from the source to the sink
ll solve() { // reinitialize costs if rerun
	ll totflow = 0;
	while(true) {
		memset(fou, 0, sizeof(fou));
		queue<int> qu;
		qu.push(S);
		fou[S] = true;
		while(!qu.empty()) {
			int i = qu.front();
			qu.pop();
			if (i == T)
				break;
			for (int e : ra[i]) {
				int k = kend[e];
				if (cap[e] > 0 && !fou[k]) {
					qu.push(k);
					pre[k] = PII(i,e);
					fou[k] = true;
				}
			}
		}
		if (!fou[T])
			break;
		int mk = INF;
		for (int i = T; i != S; i = pre[i].first)
			mk = min(mk, cap[pre[i].second]);
		totflow += mk;
		for (int i = T; i != S; i = pre[i].first) {
			cap[pre[i].second] -= mk;
			cap[pre[i].second^1] += mk;
		}
	}
	return totflow;
}


char line[1000000];
int TE, N, W;
map<string,int> ma;

vector<int> readl() {
	fgets(line, sizeof(line), stdin);
	VI res;
	string s;
	for (int i = 0; line[i] && line[i] != '\n'; i++) {
		if (line[i] == ' ' && !s.empty()) {
			if (!ma.count(s)) {
				ma[s] = W;
				W++;
			}
			res.push_back(ma[s]);
			s.clear();
		} else
			s += line[i];
	}
	if (!s.empty()) {
		if (!ma.count(s)) {
			ma[s] = W;
			W++;
		}
		res.push_back(ma[s]);
		s.clear();
	}
	return res;
}

int main() {
	fgets(line, sizeof(line), stdin);
	sscanf(line, "%d", &TE);
	for (int test = 0; test < TE; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		ma.clear();
		W = 0;
		FM = 0;
		fgets(line, sizeof(line), stdin);
		sscanf(line, "%d ", &N);
// 		printf("N=%d\n", N);
		S = 0;
		T = 1;
		REP(i,0,N) {
			VI ws = readl();
			for (int w : ws) {
// 				printf("%d -> %d\n", i, w);
				addedge(i, N+2*w, INF);
				addedge(N+2*w+1, i, INF);
			}
		}
		REP(w,0,W)
			addedge(N+2*w, N+2*w+1, 1);
		FN = N+2*W;
		printf("%lld\n", solve());
		REP(i,0,FN)
			ra[i].clear();
	}
	return 0;
}
