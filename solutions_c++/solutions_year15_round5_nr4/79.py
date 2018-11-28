#include <iostream>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;

#define REP(i, n) for(int i(0); (i)<(int)(n); i++)
#define FOR(i, a, b) for (int i(a); i <= int(b); i++)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair


map<LL, LL> a, b;
vector<LL> ans;
LL p, n;

void solve() {
	cin >> p;
	vector<LL> x;
	a.clear(); b.clear();
	REP(i, p) {
		LL xx;
		cin >> xx;
		x.PB(xx);
	}
	LL sum = 0;
	REP(i, p) {
		LL c;
		cin >> c;
		a[x[i]] = c;
		sum += c;
	}
	n = 0;
	while ((sum >> n) != 1) n++;
	ans.clear();
	REP(k, n) {
		b.clear();
		vector<pair<LL, LL> > x;
		for (map<LL, LL> :: iterator itr = a.begin(); itr != a.end(); itr++) {
			x.PB(MP(itr->first, itr->second));
		}
		LL p = 0;
		if ((int)x.size() > 1) {
			p = x[1].first;
		}
		ans.PB(p);
		b.clear();
		a.swap(b);
		for (map<LL, LL> :: iterator itr = b.begin(); itr != b.end(); itr++)
		if (itr->second > 0) {
			if (p < 0) {
				a[itr->first - p] = itr->second;
				b[itr->first - p] -= itr->second;
			} else if (p > 0) {
				a[itr->first] = itr->second;
				b[itr->first + p] -= itr->second;
			} else if (p == 0)
				a[itr->first - p] = itr->second / 2;
		}
	}

	static int caseCnt = 0;
	cerr << caseCnt << endl;
	sort(ALL(ans));
	printf("Case #%d:", ++caseCnt);
	REP(i, ans.size()) cout << ' ' << ans[i];
	cout << endl;
}

int main() {
	int T = 1;
	scanf("%d", &T);
	while (T--) solve();
	return 0;
}

