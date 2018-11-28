#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int Solve2(int L, vector<ll>& org, vector<ll>& target)
{
	sort(target.begin(), target.end());
	int ret = -1;
	for (int i = 0; i < org.size(); i++) {
		for (int j = 0; j < target.size(); j++) {
			ll x = org[i] ^ target[j];
			auto o = org;
			for (auto& e : o) {
				e ^= x;
			}
			sort(o.begin(), o.end());

			if (o == target) {
				ll b = 0, t = x;
				while (t) {
					b += t & 1;
					t /= 2;
				}
				if (ret == -1 || ret > b) {
					ret = b;
				}
			}
		}
	}
	return ret;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, L;
		cin >> N >> L;
		vector<ll> org(N, 0), target(N, 0);
		for (int i = 0; i < N; i++) {
			string s;
			cin >> s;
			ll p = 1;
			for (auto c : s) {
				if (c == '1') {
					org[i] += p;
				}
				p *= 2;
			}
		}
		for (int i = 0; i < N; i++) {
			string s;
			cin >> s;
			ll p = 1;
			for (auto c : s) {
				if (c == '1') {
					target[i] += p;
				}
				p *= 2;
			}
		}

		int m = Solve2(L, org, target);
		if (m >= 0) {
			printf("Case #%d: %d\n", t, m);
		}
		else {
			printf("Case #%d: NOT POSSIBLE\n", t);
		}
	}

	return 0;
}
