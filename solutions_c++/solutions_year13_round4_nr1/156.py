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

const int MOD = 1000002013;
int n, m;

long long cal(ll k) {
	// cout << "k = " << k << endl;
	if (!k) return 0;
	return (n + n - k + 1) * k / 2 % MOD;
}

int main() {
	int T, nowCase = 0;
	cin >> T;
	while (T--) {
		cin >> n >> m;
		// cout << n << " " << m << endl;
		vector< pair<PII, int> > res;
		long long orig = 0;
		REP(i, m) {
			int s, e, p;
			cin >> s >> e >> p;
			res.PB(MP(MP(s, -1), p));
			res.PB(MP(MP(e, 1), p));
			orig = (orig + cal(e - s) * p % MOD) % MOD;
		}
		SORT(res);
		long long ans = 0;
		vector<PII> s;
		TR(it, res) {
			PII e = it->first;
			if (e.second == -1) {
				s.PB(MP(e.first, it->second));
			} else {
				ll num = it->second;
				while (num) {
					int shift = min((ll)s.back().second, num);
					ans = (ans + cal(e.first - s.back().first) * shift) % MOD;
					s.back().second -= shift;
					num -= shift;
					if (!s.back().second) s.pop_back();
				}
			}
		} 

		ans = (orig - ans) % MOD;
		ans = (ans + MOD) % MOD;
		cout << "Case #" << ++nowCase << ": " << ans << endl;
	}
	return 0;
}