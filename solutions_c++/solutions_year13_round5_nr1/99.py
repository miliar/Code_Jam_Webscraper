#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

int nowCase = 0;

int n;
ll a[37], b;
ll invest[37];

double e = 0;

ll c[37];

void update() {
	REP(i, 37) c[i] = a[i] + invest[i];
	int numSame = 0;
	REP(i, 37) if (c[i] == c[0]) ++numSame;
	REP(i, 36) assert(c[i] <= c[i + 1]);
	double ans = 0;
	REP(i, 37) if (c[i] == c[0]) {
		ans += invest[i] / (double) numSame * 36 - invest[i];
	} else ans -= invest[i];

	e = max(e, ans);
}

bool change[55];

void solve() {
	cin >> b >> n;
	CLEAR(a);
	REP(i, n) cin >> a[i];
	sort(a, a + 37);
	CLEAR(invest);
	e = 0.0;
	ll b0 = b;
	for (int i = 0; i < 36; ) {
		int j = i;
		while (j < 36 && a[i] == a[j]) {
			++j;
		}
		ll most = a[j] - a[i];
		ll can = min(b / j, most - 1);
		if (most == 0) break;
		for (int k = 0; k < j; ++k) invest[k] += can;
		update();
		b -= can * j;
		if (b >= j) {
			for (int k = 0; k < j; ++k) ++invest[k];
			b -= j;
			update();
		} else break;
		i = j;
	}
	b = b0;
	CLEAR(invest);
	for (int i = 0; i < 36; ) {
		int j = i;
		while (j < 36 && a[i] == a[j]) {
			++j;
		}
		ll most = a[j] - a[i];
		ll can = min(b / j, most - 1);
		if (most == 0) break;
		for (int k = 0; k < j; ++k) invest[k] += can;
		if (invest[0]) {
			CLEAR(change);
			for (int k = 0; k < j && invest[k]; ++k) {
				change[k] = true;
				--invest[k];
				update();
			}
			for (int k = 0; k < j && change[k]; ++k) {
				++invest[k];
			}
		}
		b -= can * j;
		b -= j;
		for (int k = 0; k < j; ++k) ++invest[k];
		for (int k = 0; k < j; ++k) {
			--invest[k];
			++b;
			if (b >= 0) update();
		}
		if (b >= j) {
			for (int k = 0; k < j; ++k) ++invest[k];
			b -= j;
		} else {
			break;
		}
		i = j;
	}

	printf("Case #%d: %.10f\n", ++nowCase, e);
}

int main() {
	int T;
	cin >> T;
	while (T--) {
		solve();
	}
	return 0;
}