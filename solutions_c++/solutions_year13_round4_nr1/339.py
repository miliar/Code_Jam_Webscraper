#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <functional>
#include <vector>
#include <deque>
#include <utility>
#include <bitset>

using namespace std;
typedef long long ll;
const int INF = 987654321;
const ll LINF = (ll)1e15;

int TC, TCC;

const ll N_ = (ll)1e9;
const int M_ = 150;
const ll MOD = 1000002013ll;

int N, M;

ll MD(ll a) { return (a + MOD * 10000ll) % MOD; }
int PLUS (ll a, ll b) { return (MD(a) + MD(b)) % MOD; }
int MUL  (ll a, ll b) { return (MD(a) * MD(b)) % MOD; }

struct A {
	ll o, e, p;
	A(): o(0), e(0), p(0) { }
	A(ll o, ll e, ll p): o(o), e(e), p(p) { }
	bool operator< (const A &t) const {
		return (o != t.o) ? (o < t.o) : (e < t.e);
	}
} D[M_];

ll res;

typedef pair<ll, ll> pll;
priority_queue < pll, vector<pll>, greater<pll> > QA;
priority_queue < pll > QB;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

    int i, j, k;

	scanf("%d", &TC);
	while(++TCC <= TC) {
		printf("Case #%d: ", TCC);
		
		scanf("%d%d", &N, &M);
		for(i = 1; i <= M; i++) scanf("%lld%lld%lld", &D[i].o, &D[i].e, &D[i].p);
		sort(D + 1, D + M + 1);

		res = 0;

		for(i = 1; i <= M; i++) {
			ll t = (D[i].e - D[i].o);
			ll m = MUL(t * (t-1) / 2, D[i].p);
			res = PLUS(res, -m);
		}

		for(i = 1; i <= M; i++) {
			while(!QA.empty() && QA.top().first < D[i].o) {
				pll a = QA.top(); QA.pop();
				while(a.second) {
					pll b = QB.top(); QB.pop();
					ll c = (a.first - b.first);
					if(a.second >= b.second) {
						ll v = MUL(c * (c - 1) / 2, b.second);
						res = PLUS(res, v);
						a.second -= b.second;

					}else {
						ll v = MUL(c * (c - 1) / 2, a.second);
						res = PLUS(res, v);

						b.second -= a.second;
						a.second = 0;
						QB.push(b);
					}
				}
			}
			
			QA.push( pll(D[i].e, D[i].p) );
			QB.push( pll(D[i].o, D[i].p) );
		}

		while(!QA.empty()) {
				pll a = QA.top(); QA.pop();
				while(a.second) {
					pll b = QB.top(); QB.pop();
					ll c = (a.first - b.first);
					if(a.second >= b.second) {
						ll v = MUL(c * (c - 1) / 2, b.second);
						res = PLUS(res, v);
						a.second -= b.second;
					}else {
						ll v = MUL(c * (c - 1) / 2, a.second);
						res = PLUS(res, v);

						b.second -= a.second;
						a.second = 0;
						QB.push(b);
					}
				}
		}

		while(!QA.empty()) QA.pop();
		while(!QB.empty()) QB.pop();

		printf("%lld\n", res);
	}

	return 0;
}