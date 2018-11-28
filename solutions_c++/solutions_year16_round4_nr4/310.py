#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string.h>
#include <utility>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctype.h>
#include <map>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long LL;

#define FOR(i,n) for(int i = 0;i < n;i++)
#define MP make_pair
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define PII pair<int, int>
#define PLL pair<long long, long long>
#define CLEAR(a) memset(a, 0, sizeof(a))
#define INF 2000000007
#define y1 uu1
#define y2 uu2
#define hash mash
const double EPS = 1E-12;
const double PI = acos(-1.0);
const LL mod = 1000000007;

using namespace std;

int n;
string s[4];
string r[4];

bool ppl[4];
bool mach[4];

bool att() {
	FOR(i,n) {
		if (!ppl[i]) {
			ppl[i] = 1;
			bool f = 0;
			FOR(j,n) {
				if (!mach[j] && r[i][j] == '1') {
					mach[j] = 1;
					f = 1;
					bool rv = att();
					if (!rv) return 0;
					mach[j] = 0;
				}
			}
			if (!f) return 0;
			ppl[i] = 0;
		}
	}
	return 1;
}

bool check() {
	bool g = 1;
	CLEAR(ppl);
	CLEAR(mach);

	//cout << "CHECK " << r[0] << ' ' << r[1] << endl;

	return att();
}

int go(int i1, int i2) {
	if (i1 == n) {
		if (check()) return 0;
		else return INF;
	}
	int cost = INF;
	if (s[i1][i2] == '1') {
		if (i2 == n-1) {
			cost = min(cost, go(i1+1,0));
		} else {
			cost = min(cost, go(i1,i2+1));
		}
	} else {
		if (i2 == n-1) {
			cost = min(cost, go(i1+1,0));
		} else {
			cost = min(cost, go(i1,i2+1));
		}
		// teach
		r[i1][i2] = '1';
		if (i2 == n-1) {
			cost = min(cost, 1+go(i1+1,0));
		} else {
			cost = min(cost, 1+go(i1,i2+1));
		}
		r[i1][i2] = '0';
	}
	return cost;
}

void solve() {
	cin >> n;
	FOR(i, n) {
		cin >> s[i];
		r[i] = s[i];
	}

	cout << go(0,0) << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;

  FOR(t,tt) {
    cout << "Case #" << t+1 << ": ";
    solve();
  }

  return 0;
}
