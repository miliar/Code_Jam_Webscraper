#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <numeric>
#include <bitset>
#include <complex>
#define rep(x, to) for (int x = 0; x < (to); x++)
#define REP(x, a, to) for (int x = (a); x < (to); x++)
#define foreach(itr, x) for (typeof((x).begin()) itr = (x).begin(); itr != (x).end(); itr++)
#define EPS (1e-14)
#define _PA(x,N) rep(i,N){cout<<x[i]<<" ";}cout<<endl;
#define _PA2(x,H,W) rep(i,(H)){rep(j,(W)){cout<<x[i][j]<<" ";}cout<<endl;}

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef complex<double> Complex;
typedef vector< vector<int> > Mat;


const ll INF = 1e+15;

int T;
string s;
ll ans;

map<string, ll> memo;
queue< pair<string, ll> > Q;

bool ok(string &x) {
	for (int i = 0; i < x.size(); i++) {
		if (x[i] == '-') return false;
	}
	return true;
}

ll bfs(string x) {

	memo[x] = 0;
	Q.push(pair<string, ll>(x, 0));

	while (!Q.empty()) {
		pair<string, ll> cur = Q.front(); Q.pop();
		string x = cur.first;
		ll d = cur.second;

		for (int i = 1; i <= x.size(); i++) {
			//flip : [0, i)
			string y = "";
			rep(j, i) y += x[i - j - 1] == '+' ? '-' : '+';
			y += x.substr(i);
			if (memo.find(y) != memo.end()) continue;
			memo[y] = d + 1;
			Q.push(pair<string, ll>(y, d + 1));
		}
	}

	string z = "";
	for (int i = 0; i < x.size(); i++) z += '+';

#if 0
	foreach(itr, memo) {
		cout << itr->first << " " << itr->second << endl;
	}
#endif

	return memo[z];
}

ll solve() {
	memo.clear();
	return bfs(s);
}

int main() {
	cin >> T;
	rep(i, T) {
		cin >> s;
		ans = solve();
		printf("Case #%d: %lld\n", i + 1, ans);
	}
	return 0;
}


