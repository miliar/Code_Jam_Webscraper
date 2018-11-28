#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define FORC( it, V ) for( __typeof( (V).begin() ) it = (V).begin(); it != (V).end(); ++it )
#define SZ(a) a.size()
#define INF 1001001001

string i2s(int x) { ostringstream tmp;  tmp << x;  return tmp.str(); }
int s2i(string s) { istringstream i(s);  int x;  i >> x;  return x; }

long long n, m;
int origin[1111];
long long dest[1111];
long long p[1111];
long long totalCost;
vector<long long> pos;
long long cnt[2222];

long long cost(int a, int b) {
	long long len = b - a;
	if (len <= 0) return 0;
	//len = 2: N + N - 1;
	//len = 3: N + N - 1 + N - 2;
	//len = 4: N + N - 1 + N - 2 + N - 3;
	//len = 5: 5N - 1 - 2 - 3 - 4
	return len * n - len * (len - 1) / 2;
}

long long process() {
	sort(pos.begin(), pos.end());
	pos.resize(unique(pos.begin(), pos.end()) - pos.begin());
	REP(i, m) {
		long long o, d;
		REP(j, pos.size()) {
			if (origin[i] == pos[j]) o = j;
			if (dest[i] == pos[j]) d = j;
		}
		FOR(j, o, d - 1) {
			cnt[j] += p[i];
		}
	}
	long long curCost = 0;
	REP(i, pos.size()) {
		while (cnt[i]) {
			int right = i;
			while (right + 2 < pos.size() && cnt[right + 1]) right++;
			long long pp = INF;
			FOR(j, i, right) pp = min(pp, cnt[j]);
			FOR(j, i, right) cnt[j] -= pp;
			curCost += pp * cost(pos[i], pos[right + 1]);
		}
	}
	return totalCost - curCost;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int test;
	cin >> test;
	REP(itest,test) {
		cin >> n >> m;
		totalCost = 0;
		pos.clear();
		REP(i, m) {
			cin >> origin[i] >> dest[i] >> p[i];
			pos.push_back(origin[i]);
			pos.push_back(dest[i]);
			totalCost += p[i] * cost(origin[i], dest[i]);
		}
		cout << "Case #" << itest+1 << ": " << process() << endl;
	}
	return 0;
}
