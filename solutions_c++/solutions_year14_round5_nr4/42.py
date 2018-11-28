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

int T, N;
int v[4000];
vector<int> adj[4000];
bool taken[4000];
bool used[4000];

int dep = 0;
int visit(int a, int b, int d, bool other=true) {
	assert(taken[a] && taken[b]);
	int dp;
	dep++;
	if (d == 0) {
		dp = -1E9;
		bool any = false;
		for (int aa : adj[a]) {
			if (used[min(a,aa)])
				continue;
			any = true;
			used[min(a,aa)] = true;
			bool tb = taken[aa];
			taken[aa] = true;
			dp = max(dp, visit(aa, b, 1-d)+(!tb ? v[aa] : 0));
			taken[aa] = tb;
			used[min(a,aa)] = false;
		}
		if (!any && !other)
			dp = 0;
		if (!any && other)
			dp = visit(a, b, 1-d, false);
	} else {
		dp = 1E9;
		bool any = false;
		for (int bb : adj[b]) {
			if (used[min(b,bb)])
				continue;
			any = true;
			used[min(b,bb)] = true;
			bool tb = taken[bb];
			taken[bb] = true;
			dp = min(dp, visit(a, bb, 1-d)-(!tb ? v[bb] : 0));
			taken[bb] = tb;
			used[min(b,bb)] = false;
		}
		if (!any && !other)
			dp = 0;
		if (!any && other)
			dp = visit(a, b, 1-d, false);
	}
// 	printf("%d  %d %d %d %d %d %d\n", dep, r, s, a, b, d, dp);
	dep--;
	return dp;
}

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d", &N);
		REP(i,0,N) {
			adj[i].clear();
		}
		REP(i,0,N) {
			scanf("%d", v+i);
		}
		REP(i,0,N-1) {
			int j;
			scanf("%d", &j);
			j--;
			assert(j > i);
			adj[i].push_back(j);
			adj[j].push_back(i);
		}
// 		REP(i,0,N) REP(j,0,N)
// 			printf("d(%d,%d) = %d\n", i, j, dist[i][j]);
		int best = -1E9;
		REP(r,0,N) {
			int worst = 1E9;
			REP(s,0,N) {
				REP(i,0,N)
					taken[i] = used[i] = false;
				taken[r] = taken[s] = true;
				int res = visit(r, s, 0);
				taken[r] = taken[s] = false;
				res += v[r];
				if (r != s)
					res -= v[s];
// 				printf("%d %d: %d\n", r, s, res);
				worst = min(worst, res);
			}
			best = max(best, worst);
		}
		printf("%d\n", best);
// 		break;
	}
	return 0;
}
