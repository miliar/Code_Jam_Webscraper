#include <vector>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <utility>

#include <string>
#include <iostream>

using namespace std;

template<typename T>
inline int sz(const T& x) { return (int)x.size(); }

typedef long long int LL;
typedef vector<LL> vi;
typedef vector<vi> vvi;
typedef pair<LL,LL> ii;
typedef vector<ii> vii;

const LL MOD = 1000002013;


LL dist(LL N, LL n) {
	return (n*(N+1) - n*(n+1)/2) % MOD;
}

int main() {
	int tcn; cin >> tcn;

	for (int tc = 1; tc <= tcn; ++tc) {
		int ans = 0;

		int N, M;
		cin >> N >> M;

		map<int,LL> in, out;
		LL s = 0;
		for (int i = 0; i < M; ++i) {
			int o, e, p;
			cin >> o >> e >> p;
			s = (s + p*dist(N, e - o))%MOD;
			in[o] += p;
			out[e] += p;
		}

		LL s2 = 0;
		for(map<int,LL>::iterator it = out.begin(); it != out.end();) {
			int p = it->second;
			if (p == 0) {
				++it;
				continue;
			}

			int e = it->first;
			map<int,LL>::iterator it2 = in.lower_bound(e);
			if (it2->first != e) --it2;
			int o = it2->first;

			LL gp = min(it->second, it2->second);
			it->second -= gp;
			it2->second -= gp;
			if (it2->second == 0)
				in.erase(o);

			s2 = (s2 + gp*dist(N, e - o))%MOD;
		}
		//cout << s << endl << s2 << endl;

		ans = (s - s2 + MOD) % MOD;
		cout << "Case #" << tc << ": " << ans << "\n";
	}

	return 0;
}
