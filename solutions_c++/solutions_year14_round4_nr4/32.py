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

int T;
int M, N;

const int DOTS = 1000000;
const int LETTERS = 26; // Number of different letters
int P; // Number of nodes in the prefix tree
char ltt[DOTS]; // Character for this node
VI wend[DOTS]; // Numbers of the words ending here
int adj[DOTS][LETTERS]; // [node][character]: child node (-1 if non-existent)
vector<int> vadj[DOTS]; // Numbers of the child nodes

int dec(char c) { // ``character $\rightarrow$ number'' mapping, for example:
	return c-'A';
}

void init() {
	wend[0].clear();
	fill_n(adj[0], LETTERS, -1);
	vadj[0].clear();
	P = 1;
}

// Add a word to the prefix tree and give it the number w
void add(const char *wort, int w) {
	int c = 0;
	for (int i = 0; wort[i]; i++) {
		int &cs = adj[c][dec(wort[i])]; // Don't forget the ``\verb|&|''
		if (cs == -1) {
			cs = P;
			vadj[c].push_back(P);
			ltt[P] = wort[i];
			wend[P].clear();
			fill_n(adj[P], LETTERS, -1);
			vadj[P].clear();
			P++;
		}
		c = cs;
	}
	wend[c].push_back(w);
}

ll powermod(ll a, ll b, ll m) {
	ll e = a, r = 1;
	for (int i = 0; (1ll<<i) <= b; i++) { // ``one el el''
		if (b&(1ll<<i))
			r = r*e%m; // use multmod if necessary
		e = e*e%m; // use multmod if necessary
	}
	return r;
}

char line[1000];
ll fac[2000];
ll facinv[2000];

const ll MOD = 1000000007;

int h[DOTS];
ll dp[DOTS];

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d%d", &M, &N);
		init();
		REP(i,0,M) {
			scanf("%s", line);
			add(line, i);
		}
		fac[0] = facinv[0] = 1;
		REP(i,1,2000) {
			fac[i] = fac[i-1]*i%MOD;
			facinv[i] = powermod(fac[i], MOD-2, MOD);
			assert(fac[i]*facinv[i]%MOD == 1);
		}
		ll res1 = 0;
		for (int i = P-1; i >= 0; i--) {
			h[i] = wend[i].size();
			for (int j : vadj[i])
				h[i] += h[j];
			h[i] = min(h[i], N);
			res1 += h[i];
			
			dp[i] = 0;
			ll vorz = 1;
			REP(w,0,h[i]+1) {
				ll z = vorz*fac[h[i]]%MOD*facinv[w]%MOD*facinv[h[i]-w]%MOD;
				for (int j : vadj[i]) {
					if (h[i]-h[j]-w >= 0)
						z = z*dp[j]%MOD*facinv[h[j]]%MOD*fac[h[i]-w]%MOD*facinv[h[i]-h[j]-w]%MOD;
					else
						z = 0;
				}
				REP(t,0,(int)wend[i].size()) {
					z = z*(h[i]-w)%MOD;
				}
				dp[i] += z;
				dp[i] %= MOD;
				vorz *= -1;
			}
// 			printf("dp[%d] = %lld\n", i, dp[i]);
		}
		printf("%lld %lld\n", res1, (dp[0]%MOD+MOD)%MOD);
	}
	return 0;
}
