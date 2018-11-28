#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<vii> vvii;
typedef set<int> si;
typedef vector<si> vsi;
typedef pair<double, double> dd;

const int inf = 1e9;

int main() {
	ios::sync_with_stdio(false);

    int ts; cin >> ts;
	for (int t = 1; t <= ts; t++) {
		string s; cin >> s;
		int cur = s.length() - 1;
		int ans = 0;
		while (cur >= 0) {
			while (cur >= 0 && s[cur] == '+')
				cur--;
			if (cur < 0)
				break;
			if (s[0] == '-') {
				for (int i = 0; i <= cur / 2; i++) {
					swap(s[i], s[cur - i]);
					s[i] == '-' ? s[i] = '+' : s[i] = '-';
					s[cur - i] == '-' ? s[cur - i] = '+' : s[cur - i] = '-';
				}
				if (cur % 2 == 0)
					s[cur / 2] == '-' ? s[cur / 2] = '+' : s[cur / 2] = '-';
			} else {
				int first_plus = cur;
				while (first_plus > 0 && s[first_plus] == '-')
					first_plus--;
				for (int i = 0; i <= first_plus / 2; i++) {
					swap(s[i], s[first_plus - i]);
					s[i] == '-' ? s[i] = '+' : s[i] = '-';
					s[first_plus - i] == '-' ? s[first_plus - i] = '+' : s[first_plus - i] = '-';
				}
				if (first_plus % 2 == 0)
					s[first_plus / 2] == '-' ? s[first_plus / 2] = '+' : s[first_plus / 2] = '-';
			}
			// cerr << s << ' ' << cur << endl;
			ans++;
		}
		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}
