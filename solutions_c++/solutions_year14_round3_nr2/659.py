#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define all_of(v) v.begin(), v.end()
#define fi first
#define se second
#define pb push_back

vector<int> facts = {1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800};

int fact(int x) {
	return facts[x - 1];
}

int main() {
	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		cout << "Case #" << test << ": ";

		int n;
		cin >> n;

		vector<string> strs;

		for (int i = 0; i < n; i++) {
			string s;
			cin >> s;

			strs.push_back(s);
		}

		vector<int> v;
		for (int i = 0; i < n; i++) {
			v.push_back(i);
		}

		int ans = 0;

		int f = fact(n);
		for (int _i = 0; _i < f; _i++) {

			string result;
			for (int i: v) {
				result += strs[i];
			}

			//cout << result << endl;

			bool bad[256];
			memset(bad, false, 256);

			for (int i = 0; i < result.length(); i++) {
				if (bad[result[i]]) {
					goto next;
				}

				int _next = i + 1;
				while (_next < result.length() && result[i] == result[_next]) {
					_next++;
				}

				bad[result[i]] = true;
				i = _next - 1;
			}

			//cout << "OK" << endl;
			ans++;
			next: next_permutation(v.begin(), v.end());
		}

		cout << ans << endl;
	}
}