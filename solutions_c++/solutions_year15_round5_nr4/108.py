#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

void solve() {
	int p;
	cin >> p;
	vector<int64_t> e(p);
	for (auto &v: e)
		cin >> v;
	multiset<int64_t> ms;
	int sum2 = 0;
	for (int i = 0; i < p; ++i) {
		int f;
		cin >> f;
		sum2 += f;
		for (int j = 0; j < f; ++j)
			ms.emplace(e[i]);
	}
	int sum;
	for (sum = 0; (1<<sum) < sum2; ++sum) {}
	assert((1<<sum) == sum2);

	multiset<int64_t> ans;
	for (int i = 0; i < sum; ++i) {
		bool ok = false;
		for (auto it = begin(ms); it != end(ms); ++it) {
			int64_t v = *it;
			auto cp = ms;
			multiset<int64_t> nxt;
			while (!cp.empty()) {
				auto jt = begin(cp);
				int64_t w = *jt;
				cp.erase(jt);
				if (v < 0) {
					nxt.emplace(w - v);
					w -= v;
				} else {
					nxt.emplace(w);
					w += v;
				}
				jt = cp.find(w);
				if (jt == end(cp))
					break;
				cp.erase(jt);
			}
			if (cp.empty()) {
				ok = true;
				ans.emplace(v);
				ms = nxt;
				break;
			}
		}
		assert(ok);
	}

	for (auto v: ans)
		cout << v << ' ';
}

int main() {
	int tcase;
	cin >> tcase;
	for (int t = 0; t < tcase; ++t) {
		cout << "Case #" << (t + 1) << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}
