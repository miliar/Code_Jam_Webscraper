#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

int N, J;
typedef long long ll;
ll conv(ll s, int b) {
	ll ret = 0;
	for(int i = N - 1; i >= 0; i--) {
		ret *= b;
		if(s & (1LL << i)) {
			ret++;
		}
	}
	return ret;
}

ll finddiv(ll n) {
	for(ll i = 2; i * i <= n; i++) {
		if(n % i == 0) return i;
	}
	return -1;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for(int loop = 1; loop <= T; loop++) {
		cin >> N >> J;

		vector<ll> ans1;
		vector<vector<ll>> ans2;
		for(ll i = 1LL << (N - 1); i < 1LL << N; i++) {
			if(i & 1) {
				//cout << i << endl;
				vector<ll> a;
				for(int b = 2; b <= 10; b++) {
					ll c = conv(i, b);
					//cout << "b:" << b << " c:" << c << endl;
					ll d = finddiv(c);
					if(d == -1) break;
					a.push_back(d);
				}
				if(a.size() != 9) continue;
				ans1.push_back(i);
				ans2.push_back(a);
			}
			if(ans1.size() == J) break;
		}

		cout << "Case #" << loop << ":" << endl;
		for(int i = 0; i < J; i++) {
			//	cout << ans1[i] << endl;
			string s;
			for(int j = 0; j < N; j++) {
				if(ans1[i] & (1 << j)) s = '1' + s;
				else s = '0' + s;
			}
			cout << s << " ";
			for(int j = 0; j < 9; j++) {
				cout << ans2[i][j];
				if(j != 8) cout << " ";
			}
			cout << endl;
		}
	}
}