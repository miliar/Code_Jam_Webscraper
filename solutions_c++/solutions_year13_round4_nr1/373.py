#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned int ui;
typedef pair<int,int> pii;
typedef vector<vector<int> > graph;

const double pi = acos(-1.0);

#define oned(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define twod(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

#define MAXM 1005

int TESTS, CASE;
int n, m;
int l[MAXM], r[MAXM], p[MAXM];
int mod = 1000002013;

ll cost(int len) {
	return (len * (ll)(2*n - len + 1) / 2) % mod;
}

void solve() {
	cout << "Case #" << CASE << ": ";
	
	map<int,ll,greater<int> > starts;
	map<int,ll> ends;
	for(int i = 0; i < m; i++) {
		starts[l[i]] += p[i];
		ends[r[i]] += p[i];
	}
	
	ll sum = 0;
	while(!ends.empty()) {
		int end = ends.begin()->fst;
		ll endCnt = ends.begin()->snd;
		map<int,ll,greater<int> >::iterator it = starts.lower_bound(end);
		int start = it->fst;
		ll startCnt = it->snd;
		
		ll cnt = min(startCnt, endCnt);
		sum = (sum + cost(end-start)*cnt) % mod;
		
		if(cnt == endCnt) {
			ends.erase(ends.begin());
		} else {
			ends[end] -= cnt;
		}
		
		if(cnt == startCnt) {
			starts.erase(it);
		} else {
			starts[start] -= cnt;
		}
	}
	
	ll ori = 0;
	for(int i = 0; i < m; i++) {
		ori = (ori + cost(r[i]-l[i])*p[i]) % mod;
	}
	
	int ans = (ori - sum) % mod;
	if(ans < 0) ans += mod;
	cout << ans << endl;
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	cin >> TESTS;
	for(CASE = 1; CASE <= TESTS; CASE++) {
		scanf("%d %d", &n, &m);
		for(int i = 0; i < m; i++) {
			scanf("%d %d %d", l+i, r+i, p+i);
		}
		solve();
	}
}
