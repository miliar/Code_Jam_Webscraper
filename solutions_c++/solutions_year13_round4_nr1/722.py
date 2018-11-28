#include <iostream>
#include <vector>
#include <map>

#define M 1000002013ll

using namespace std;

long long n;

long long calc(long long delta, long long v) {
	return ((2*n-delta+1)*delta/2 % M) * v % M;
}

inline
void add(long long & a, long long b) {
	a = (a + b) % M;
}

int main() {
	long long T;
	cin >> T;
	for (long long ca = 1; ca <= T; ca++) {
		long long m;
		cin >> n >> m;
		map<long long, long long> mp;
		long long orig = 0;
		for (long long i = 0; i < m; i++) {
			long long l, r, v;
			cin >> l >> r >> v;
			add(orig, calc(r - l, v));
			mp[l] += v;
			mp[r] -= v;
			if (mp[l] == 0) {
				mp.erase(l);
			}
			if (mp[r] == 0) {
				mp.erase(r);
			}
		}
		vector<pair<long long, long long>> stack;
		long long ans = 0;
		//for (auto & iter : mp) {
		//	cout << iter.first << " " << iter.second << "\n";
		//}
		for (auto & iter : mp) {
			if (iter.second >= 0) {
				stack.push_back(make_pair(iter.first, iter.second));
			} else {
				long long cost = -iter.second;
				while (stack.size() > 0 && stack.back().second <= cost) {
					cost -= stack.back().second;
					add(ans, calc(iter.first - stack.back().first, stack.back().second));
					stack.pop_back();
					//cout << ans << "\n";
				}
				stack.back().second -= cost;
				add(ans, calc(iter.first - stack.back().first, cost));
			}
		}
		cout << "Case #" << ca << ": " << (orig - ans + 10 * M) % M << "\n";
	}
	return 0;
}
