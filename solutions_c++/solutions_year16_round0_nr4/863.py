#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
#include <vector>

using namespace std;

typedef long long ll;

const int maxn = 105;

ll hPow[maxn];

vector<ll> getList(int k, int c) {
	vector<ll> ret;
	int cInd = 0;
	while (cInd < k) {
		int add = c;
		ll tot = 0;
		while (add-- && cInd < k) {
			tot += hPow[add]*cInd;
			cInd++;
		}
		ret.push_back(tot);
	}
	return ret;
}

int main() {
	ios_base::sync_with_stdio(0);
	ifstream cin("All.in");
	ofstream cout("All.out");
	int t;
	cin >> t;
	for (int rep = 1; rep <= t; rep++) {
		cout << "CASE #" << rep << ":";
		ll k, c, s;
		cin >> k >> c >> s;
		hPow[0] = 1;
		for (int i = 1; i <= c; i++) {
			hPow[i] = hPow[i-1]*k;
		}
		vector<ll> ans = getList(k, c);
		if (ans.size() > s) cout << " IMPOSSIBLE";
		else for (int i = 0; i < ans.size(); i++) cout << ' ' << ans[i]+1;
		cout << '\n';
	}
	return 0;
}

