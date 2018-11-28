#include <bits/stdc++.h>
#define endl '\n'
#define D(x) cout << #x ": " << (x) << endl;
using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<ll,ll> pii;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T;
	cin >> T;

	int n;
	string s;
	for (int cn = 1; cn <= T; cn++) {
		cin >> n;
		cin >> s;
		bool standing[s.size()];

		ll tot = 0, ans = 0;
		for (int i = 0; i < s.size(); i++) {
			if (tot < i) {
				ans++;
				tot++;
			}
			tot += s[i] - '0';
		}
		cout << "Case #" << cn << ": " << ans << endl;
	}

	return 0;
}