#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

void solve() {
	static int tc = 1;
	cout << "Case #" << tc << ": ";
	tc++;
	string a;
	cin >> a;
	int score = 0;
	int left = sz(a);
	stack<char> L;
#define last (L.empty() ? -1 : L.top())
	trav(it, a) {
		if (last == it) {
			score += 5;
			L.pop();
		} else if (sz(L) == left) {
			L.pop();
		} else if (it == 'C') {
			L.push('C');
			score += 5;
		} else if (it == 'J') {
			L.push('J');
			score += 5;
		} else {
			assert(false);
		}
		--left;
	}
	cout << score << endl;

}

int main() {
	int N;
	cin.sync_with_stdio(false);
	cin >> N;
	while (N --> 0) solve();
}
