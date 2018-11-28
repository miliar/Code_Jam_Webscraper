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
#define MOD(a,b) (((a)%(b)+(b))%(b))
#define REP(i,n) for (int i = 0; i < (n); i++)

struct ka {
	int u,v,a,b,id,len;
};

int T, N, M, P;
vector<ka> adj[1001];
vector<ka> radj[1001];
int rdist[1001];
int dist[1001];
bool done[1001];

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d%d%d", &N, &M, &P);
		REP(i, N) {
			adj[i].clear();
			radj[i].clear();
		}
		REP(i, M) {
			ka k;
			scanf("%d%d%d%d", &k.u, &k.v, &k.a, &k.b);
			k.u--; k.v--;
			k.id = i;
			k.len = k.b;
			adj[k.u].push_back(k);
			radj[k.v].push_back(k);
		}
		REP(i, N) {
			rdist[i] = 2.1E9;
			done[i] = false;
		}
		{
			rdist[1] = 0;
			priority_queue<PII> qu;
			qu.push(PII(0, 1));
			while(!qu.empty()) {
				int i= qu.top().second;
				qu.pop();
				if (done[i])
					continue;
				done[i] = true;
				FOREACH(it, radj[i]) {
					int d = rdist[i]+it->a;
					int j = it->u;
					if (rdist[j] > d) {
						rdist[j] = d;
						qu.push(PII(-d, j));
					}
				}
			}
		}
		vector<int> path;
		REP(i, P) {
			int a;
			scanf("%d", &a);
			path.push_back(a-1);
		}
		bool found = false;
		int end = 0;
		int totlen = 0;
		for (int p = 0; p < P; p++) {
			FOREACH(it, adj[end]) {
				if (it->id == path[p]) {
					it->len = it->a;
					totlen += it->len;
					end = it->v;
					break;
				}
			}
			REP(i, N) {
				dist[i] = 2.1E9;
				done[i] = false;
			}
			priority_queue<PII> qu;
			dist[0] = 0;
			qu.push(PII(0,0));
			while(!qu.empty()) {
				int i= qu.top().second;
				qu.pop();
				if (done[i])
					continue;
				done[i] = true;
				FOREACH(it, adj[i]) {
					int d = dist[i]+it->len;
					int j = it->v;
					if (dist[j] > d) {
						dist[j] = d;
						qu.push(PII(-d, j));
					}
				}
			}
			assert(dist[end] <= totlen);
			if (dist[end] < totlen || dist[1] < totlen+rdist[end]) {
				found = true;
				printf("%d\n", path[p]+1);
				break;
			}
		}
		if (!found)
			printf("Looks Good To Me\n");
	}
	return 0;
}
