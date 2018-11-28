#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
long long solve() {
	int N, M;
	cin >> N >> M;
	vector<int> o(M), e(M), p(M);
	for (int i = 0; i < M; ++ i) cin >> o[i] >> e[i] >> p[i];
	long long r = 0, rr = 0;
	vector<pair<int,int>> a;
	for (int i = 0; i < M; ++ i) {
		int d = e[i] - o[i];
		r += p[i] * (d * N - d * (d-1) / 2);
		a.push_back(make_pair(o[i], -p[i]));
		a.push_back(make_pair(e[i], p[i]));
	}
	sort(a.begin(), a.end());
	map<int, int> b;
	for (auto x : a) {
		if (x.second < 0) {
			b[x.first] += -x.second;
		} else {
			int n = x.second;
			for (auto i = b.rbegin(); n > 0 && i != b.rend(); ++ i) {
				int m = min(n, i->second);
				if (m > 0) {
					n -= m;
					i->second -= m;
					int d = x.first-i->first;
					rr += m * (d * N - d * (d-1) / 2);
				}
			}
		}
	}
	return r - rr;
}
int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++ tt) {
		cout << "Case #" << tt << ": " << solve() << endl;
	}
}
