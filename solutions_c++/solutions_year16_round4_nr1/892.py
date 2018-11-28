#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define SQR(a) ((a) * (a))
#define SZ(x) ((int) (x).size())
#define ALL(x) (x).begin(), (x).end()
#define CLR(x, a) memset(x, a, sizeof x)
#define VAL(x) #x << " = " << (x) << "   "
#define FOREACH(i, x) for(__typeof((x).begin()) i = (x).begin(); i != (x).end(); i ++)
#define FOR(i, n) for (int i = 0; i < (n); i ++)
#define X first
#define Y second

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;

const int MAXN = 1 * 1000 + 10;

/*string convert(vector<int> v) {
	string ans;
	for (int i = 0; i < SZ(v); i ++) {
		if (v[i] == 0) ans.pb('R');
		if (v[i] == 1) ans.pb('P');
		if (v[i] == 2) ans.pb('S');
	}
	return ans;
}

int winner(int a, int b) {
	if (b > a) swap(a, b);
	if (a == 1 && b == 0) return 1;
	if (a == 2 && b == 1) return 2;
	if (a == 2 && b == 0) return 0;
	return 0;
}

bool check(vector<int> v) {
	if (SZ(v) & 1) return true;

	vector<int> next;
	for (int i = 0; i < SZ(v); i += 2) {
		if (v[i] == v[i + 1])
			return false;
		next.pb(winner(v[i], v[i + 1]));
	}
	return check(next);
}

vector<int> v;
string ans;
bool has = false;

void f(int a, int b, int c) {
	if (has) return ;

	if (a == 0 && b == 0 && c == 0) {
		if (check(v)) {
			has = true;
			ans = convert(v);
		}
		return ;
	}

	if (b) {
		v.pb(1);
		f(a, b - 1, c);
		v.pop_back();
	}
	if (a) {
		v.pb(0);
		f(a - 1, b, c);
		v.pop_back();
	}
	if (c) {
		v.pb(2);
		f(a, b, c - 1);
		v.pop_back();
	}
}*/

string f(int n, int a, int b, int c) {
	if (n == 0) {
		if (a) return "R";
		if (b) return "P";
		if (c) return "S";
	}

	string s1, s2;
	if (n % 2 == 0) {
		if (a > b) {
			s1 = f(n - 1, a / 2, b / 2 + 1, c / 2);
			s2 = f(n - 1, a / 2, b / 2, c / 2 + 1);
		}
		if (b > c) {
			s1 = f(n - 1, a / 2 + 1, b / 2, c / 2);
			s2 = f(n - 1, a / 2, b / 2, c / 2 + 1);
		}
		if (c > a) {
			s1 = f(n - 1, a / 2, b / 2 + 1, c / 2);
			s2 = f(n - 1, a / 2 + 1, b / 2, c / 2);
		}
	}
	else {
		if (a < b) {
			s1 = f(n - 1, a / 2, b / 2 + 1, c / 2);
			s2 = f(n - 1, a / 2, b / 2, c / 2 + 1);
		}
		if (b < c) {
			s1 = f(n - 1, a / 2 + 1, b / 2, c / 2);
			s2 = f(n - 1, a / 2, b / 2, c / 2 + 1);
		}
		if (c < a) {
			s1 = f(n - 1, a / 2, b / 2 + 1, c / 2);
			s2 = f(n - 1, a / 2 + 1, b / 2, c / 2);
		}
	}
	return s1 + s2;
}

int main () {
	ios::sync_with_stdio(false);

	int o; cin >> o;
	for (int oo = 0; oo < o; oo ++) {

		int n; cin >> n;
		int a, b, c; cin >> a >> b >> c;

		cout << "Case #" << oo + 1 << ": ";

		int mx = max(a, max(b, c));
		int mn = min(a, min(b, c));
		if (mx - mn > 1) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		cout << f(n, a, b, c) << endl;
		
	}
	return 0;
}

