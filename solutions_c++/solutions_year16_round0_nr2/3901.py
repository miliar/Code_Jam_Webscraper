#include <bits/stdc++.h>

#include <emmintrin.h>

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

using namespace std;

typedef long long ll;

const int maxn = 201000;

void solve() {
	string s;
	cin >> s;
	int ans = 0;
	for (int i = 0; i + 1 < (int) s.length(); ++i) {
		if (s[i] != s[i + 1]) ++ans;
	}
	if (s[s.size() - 1] != '+') ++ans;
	cout << ans << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
}
