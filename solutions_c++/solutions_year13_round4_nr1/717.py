#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <string>

using namespace std;

const int modl = 1000002013;
typedef long long ll;

struct data{
	int u, v;
	ll t;
	inline friend bool operator < (const data a, const data b) {
		return a.u < b.u;
	}
};

int test;
set<int> f;
data a[1010];
vector< pair<int, ll> > su, sv;

int main() {
	freopen("alarge.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &test);
	for(int ctest = 1; ctest <= test; ctest++) {
		int n, m;
		scanf("%d%d", &n, &m);
		ll total = 0;
		f.clear();
		for(int i = 1; i <= m; i++) {
			int u, v, t;
			scanf("%d%d%d", &u, &v, &t);
			
			int k = v - u;
			ll now = n*ll(n+1)/2 - (n-k)*ll(n-k+1)/2;
			now %= modl;
			total = (total + now*t) % modl;
			
			a[i].u = u; a[i].v = v; a[i].t = t;
			f.insert(u); f.insert(v);
		}
		// cout << total << endl;
		sort(a+1, a+1+m);
		ll optimal = 0;
		su.clear();
		sv.clear();	
		int idx = 0;
		for(set<int>::iterator it = f.begin(); it != f.end(); it++) {
			int i = *it;
			while (idx < m && a[idx+1].u <= i) {
				idx++;
				su.push_back(make_pair(a[idx].u, a[idx].t));
				sv.push_back(make_pair(a[idx].v, a[idx].t));
			}
			sort(sv.begin(), sv.end(), greater<pair<int, ll> >());
			
			while (!sv.empty() && sv.back().first == i) {
				ll t = sv.back().second;
				sv.pop_back();
				while (t) {
					ll tt = min(su.back().second, t) % modl;

					int k = i - su.back().first;
					ll now = n*ll(n+1)/2 - (n-k)*ll(n-k+1)/2;
					now %= modl;
					optimal = (optimal + now*tt) % modl;

					t -= tt;
					su.back().second -= tt;
					if (!su.back().second) su.pop_back();
				}
			}

			// if (ctest == 2) cout << i << " " << optimal << endl;
		}

		// cout << optimal << endl;
		ll ret = total-optimal;
		while (ret < 0) ret += modl;
		printf("Case #%d: %lld\n", ctest, ret);
	}

	return 0;
}
