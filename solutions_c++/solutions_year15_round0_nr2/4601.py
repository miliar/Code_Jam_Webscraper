#include <bits/stdc++.h>

using namespace std;

#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define for_each(it, c) for (__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
typedef long long ll;
typedef long double ld;
map<vector<int>, int> mp;
int dp(vector<int> v) {
	int mx = *max_element(all(v));
	if (mx <= 1)
		return mx;
	int &ret = mp[v];
	if (ret)
		return ret;
	ret = mx;
	v.erase(max_element(all(v)));
	if (mx == 9) {
		vector<int> v2 = v;
		v2.push_back(4);
		v2.push_back(5);
		ret = min(ret, 1 + dp(v2));
		v2.clear();
		v2 = v;
		v2.push_back(6);
		v2.push_back(3);
		ret = min(ret, 1 + dp(v2));

	} else {
		vector<int> v2 = v;
		v2.push_back(mx/2);
		v2.push_back(mx/2 + mx%2);
		ret = min(ret, 1 + dp(v2));

	}
	return ret;

}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		int d;
		scanf("%d", &d);
		vector<int> v(d);
		for (int j = 0; j < d; ++j) {
			scanf("%d", &v[j]);

		}

		printf("Case #%d: %d\n", i, dp(v));

	}

}

