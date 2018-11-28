
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)


const int MOD = 1000002013;
ll N, M;
ll gcost(ll d){
	ll res = (N * (N +1) - (N - d) * (N - d + 1)) / 2;
	return res % MOD;
}
int calc(){
	map<int, int> inout;
	ll cost = 0;
	cin >> N >> M;
	while(M--){
		int f, t, p;
		cin >> f >> t >> p;
		cost = (cost + gcost(t - f) * p) % MOD;
		//cout << f << " " << t << " " << p << " " << cost << endl;
		inout[f] += p;
		inout[t] -= p;
	}
	stack<pii > inside;
	FORIT(it, inout){
		int pos = it->first;
		int peo = it->second;
		//cout << " J " << pos << " " << peo << endl;
		if(peo == 0)continue;
		if(peo < 0){
			peo = -peo;
			while(1){
				pii cur = inside.top();
				inside.pop();
				int opos = cur.first;
				int opeo = cur.second;
				int take = min(opeo, peo);
				cost -= take * gcost(pos - opos);
				//cout << take << " " << gcost(pos - opos) << ":" <<cost << endl;
				cost %= MOD;
				if(opeo - take)inside.push(pii(opos, opeo - take));
				if(take == peo)break;
				peo -= take;
			}
		} else {
			inside.push(pii(pos, peo));
		}
	}
	cost %= MOD;
	if(cost < 0)cost += MOD;
	return cost;
}


int main() {
	int tc;
	cin >> tc;
	FOR(tcc, 1, tc + 1){
		cout << "Case #" << tcc << ": " << calc() << endl;
	}
	return 0;
}
