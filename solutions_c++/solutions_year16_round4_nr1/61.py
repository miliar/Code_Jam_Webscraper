#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
void PR(vi &v) { trav(x, v) cout << x << ' '; cout << endl; }

string str;

bool check(string s) {
	while (s.size() > 1) {
		string s2;
		for (int i = 0; i < sz(s); i += 2) {
			char a = s[i], b = s[i+1];
			if (a == b) return false;
			char c = 'R' + 'P' + 'S' - a - b;
			s2 += c;
		}
		s = move(s2);
	}
	return true;
}

void push(char c) { str += c; }
void pop() { str.erase(str.end()-1); }

void rec(int R, int P, int S) {
	if (!R && !P && !S) {
		if (check(str))
			throw 0;
	}
	if (P) push('P'), rec(R,P-1,S), pop();
	if (R) push('R'), rec(R-1,P,S), pop();
	if (S) push('S'), rec(R,P,S-1), pop();
}

void solve() {
	int N, R, P, S;
	cin >> N >> R >> P >> S;
	try {
		rec(R,P,S);
	}
	catch(int) {
		cout << str << endl;
		str.clear();
		return;
	}
	cout << "IMPOSSIBLE" << endl;
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(0);
	int N;
	cin >> N;
	rep(i,0,N) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}
