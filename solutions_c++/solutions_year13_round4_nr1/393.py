#include <iostream>
#include <cassert>
#include <map>
#include <vector>

using namespace std;


int N, M;
const long long int mod = 1000002013;
const long long int half = (mod + 1) / 2;

long long cost(int o, int e) {
	assert(e >= o);
	long long ret = (e - o) % mod;
	ret *= (ret - 1);
	ret %= mod;
	return (ret * half) % mod;
}

void solve(int casenum) {
	cin >> N >> M;
	assert(N >= 2 && N <= 1000000000);
	assert(M >= 1 && M <= 1000);
	map<int, long long> m;
	long long oldCost = 0;
	long long newCost = 0;
	for (int i = 0; i < M; i++) {
		long long o, e, p;
		cin >> o >> e >> p;
		m[o] += p;
		m[e] -= p;
		oldCost += (cost(o, e) * p) % mod;
		oldCost %= mod;
	}
	vector<pair<long long, long long> > v;
	for (map<int, long long>::iterator it = m.begin(); it != m.end(); it++) {
		if (it->second < 0) {
			long long minus = -it->second;
			while (minus > 0) {
				assert(!v.empty());
				long long deze = min(minus, v.back().second);
				newCost += (cost(v.back().first, it->first) * deze) % mod;
				newCost %= mod;
				minus -= deze;
				v.back().second -= deze;
				if (v.back().second == 0)
					v.pop_back();
			}
		}
		if (it->second > 0) {
			v.push_back(make_pair(it->first, it->second));
		}
	}
	cout << "Case #" << casenum << ": " << (newCost + mod - oldCost) % mod << endl;
}

int main() {
	int T;
	cin >> T;
	assert(T > 0 && T <= 20);
	for (int i = 1; i <= T; i++) {
		solve(i);
	}
	return 0;
}
