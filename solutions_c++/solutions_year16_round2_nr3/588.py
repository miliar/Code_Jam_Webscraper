#include <bits/stdc++.h>
using namespace std;

const int N = 17;
pair<int, int> arr[N];
bool prF[100], prS[100];
int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs) {
		int n;
		cin >> n;
		unordered_map<string, int> mp;
		for (int i = 0; i < n; ++i) {
			string a, b;
			cin >> a >> b;
			if (!mp.count(a)) mp[a] = mp.size();
			if (!mp.count(b)) mp[b] = mp.size();

			arr[i].first = mp[a];
			arr[i].second = mp[b];
		}

		int mn = 100;

		for (int msk = 0; msk < (1 << n); ++msk) {
			memset(prF, 0, sizeof prF);
			memset(prS, 0, sizeof prS);

			for (int i = 0; i < n; ++i)
				if ((msk >> i) & 1) prF[arr[i].first] = prS[arr[i].second] = 1;
			bool val = 1;
			for (int i = 0; i < n; ++i)
				if (!((msk >> i) & 1)) val &= prF[arr[i].first], val &= prS[arr[i].second];
			if (val) mn = min(mn , __builtin_popcount(msk)) ;
		}
		cout << "Case #" << cs << ": " << n - mn << '\n' ;
	}

	return 0;
}
