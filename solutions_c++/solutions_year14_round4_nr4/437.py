#include <cstdio>
#include <algorithm>
using namespace std;

using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); i++)
#define REPD(i,a,b) for (int i = (a); i >=(b); i--)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (auto i = t.begin(); i != t.end(); i++)
#define fi first
#define se second

int n,m,nnodes;
char s[22][22];
int nxt[12345][33];
int res[1234];
bool vis[1234];

int getmask(int mask, int val) {
	int ret = 0;
	FOR(i,m) {
		int last = mask % n;
		if (last == val) ret = 2*ret+1;
		else ret = 2*ret;
		mask /= n;
	}
	return ret;
}

void clear() {
	FOR(i,nnodes) FOR(j,26) nxt[i][j] = 0;
	nnodes = 1;
}

void add(int who) {
	int pos = 0, where = 0;
	while (s[who][pos]) {
		int nr = s[who][pos]-'A';
		if (nxt[where][nr] == 0) {
			nxt[where][nr] = nnodes++;
		}
		where = nxt[where][nr];
		pos++;
	}
}

int build(int mask) {
	if (vis[mask]) return res[mask];
	vis[mask] = true;
	clear();
	FOR(i,m) if (mask & (1<<i)) add(i);
	//printf("mask=%d, nodes=%d\n", mask, nnodes);
	if (nnodes==1) return res[mask]=0;
	return res[mask]=nnodes;
}

void test() {
	scanf("%d%d", &m, &n);
	FOR(i,(1<<m)) vis[i]=false;
	FOR(i,m) scanf("%s", s[i]);
	int nodes = 0, ways = 0;
	int maxm = 1;
	FOR(i,m) maxm *= n;
	FOR(mask, maxm) {
		int cur = 0;
		FOR(i,n) {
			cur += build(getmask(mask, i));
		}
		if (cur > nodes) {
			nodes = cur;
			ways = 1;
		} else if (cur == nodes) {
			ways++;
		}
		//printf("mask = %d, nodes = %d\n", mask, cur);
	}
	printf("%d %d\n", nodes, ways);
}

int main() {
	int te;
	scanf("%d", &te);
	for (int tt = 1; tt <= te; tt++) {
		printf("Case #%d: ", tt);
		test();
	}
	return 0;
}