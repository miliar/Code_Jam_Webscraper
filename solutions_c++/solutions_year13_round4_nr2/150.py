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

ll n, p;

ll worstRank(ll x) {
	++x;
	ll s = x - 1, all = (1ll << n);
	ll rank = 0;
	for (int r = 0; r < n; ++r) {
		// cout << "all = " << all << " s = " << s << endl;
		ll rest = all - 1 - s;
		if (s != 0) {
			--s;
			rank += all / 2;
			s /= 2;
		} else {
			return rank + 1;
		}
		all /= 2;
	}
	return rank + 1;
}

ll bestRank(ll x) {
	++x;
	ll all = (1ll << n), s = all - x;
	ll rank = 0;
	for (int r = 0; r < n; ++r) {
		ll rest = all - 1 - s;
		if (s != 0) {
			--s;
			s = s / 2;
		} else {
			rank += all / 2;
		}
		all /= 2;
	}
	return rank + 1;
	assert(false);

}

int main() {
	int T, nowCase = 0;
	cin >> T;
	while (T--) {
		cin >> n >> p;
		// cout << "rank1 = " << worstRank(2) << endl;
		// while(1);
		ll low = 0, high = (1ll << n) - 1;
		while (low < high) {
			ll mid = ((low + high) >> 1ll) + 1;
			if (worstRank(mid) <= p) {
				low = mid;
			} else {
				high = mid - 1;
			}
		}

		ll worstCanGetPrize = low;
		low = 0; high = (1ll << n) - 1;
		while (low < high) {
			ll mid = ((low + high) >> 1ll) + 1;
			if (bestRank(mid) <= p) {
				low = mid;
			} else {
				high = mid - 1;
			}
		}

		cout << "Case #" << ++nowCase << ": " << worstCanGetPrize << " " << low << endl;
	}
	return 0;
}