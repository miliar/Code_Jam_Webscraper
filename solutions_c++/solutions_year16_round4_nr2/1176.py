#include <iostream>
#include <iomanip>
#include <deque>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <string>
#include <bitset>
#include <cstdint>
#include <cstdio>

using ii = int64_t;
using ui = uint64_t;
#define all(v) v.begin(), v.end()

using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cout << fixed << setprecision(8);
	int cases; cin >> cases;
	for (ui cas = 1; cas <= cases; ++cas) {
		cout << "Case #" << cas << ": ";
		ii k, n; cin >> n >> k;
		deque<double> p(n); for (auto &pp : p) cin >> pp;
		double mm = 0.0;
		for (ii b = 0; b < (1 << n); ++b) {
			ii cnt = 0;
			for (ii i = 0; i < n; ++i) if (b & (1 << i)) ++cnt;
			if (cnt != k) continue;
			vector<double> q;
			for (ii i = 0; i < n; ++i) if (b & (1 << i)) q.push_back(p[i]);
			vector<double> ppp(2);
			ppp[0] = (1.0 - q[0]);
			ppp[1] = q[0];
			for (ui i = 1; i < k; ++i) {
				double c = q[i];
				vector<double> qqq(ppp.size() + 1);
				for (ui j = 0; j < ppp.size(); ++j) qqq[j] = ppp[j] * (1.0 - c);
				for (ui j = 1; j < qqq.size(); ++j) qqq[j] += ppp[j - 1] * c;
				ppp = move(qqq);
			}
			mm = max(mm, ppp[k / 2]);
		}
		cout << mm << '\n';
	}
}