#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <iomanip>

#pragma warning (disable:4996)

using namespace std;

#define rep(i, a, b) for(int i = (a); i < (b); i++)
#define per(i, a, b) for(int i = (b) - 1; i >= (a); i--)

#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define sz(x) ((int)(x).size())

typedef vector<int> vi;
typedef long long ll;
typedef pair<int, int> pii;

const ll mod = 1000000007;
ll powmod(ll a, ll b) { ll res = 1; a %= mod; for (; b; b >>= 1) { if (b & 1) res = res*a%mod; a = a*a%mod; } return res; }

string print(string c, int n) {
	if (n == 0) return c;
	else {
		string a, b;
		switch (c[0]) {
		case 'P': 
			a = print("P", n - 1);
			b = print("R", n - 1);
			if (a < b) return a + b;
			else return b + a;
		case 'R': 
			a = print("R", n - 1);
			b = print("S", n - 1);
			if (a < b) return a + b;
			else return b + a;
		case 'S': 
			a = print("P", n - 1);
			b = print("S", n - 1);
			if (a < b) return a + b;
			else return b + a;
		}
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a-l.out", "w", stdout);
	int t, cas = 1;
	cin >> t;
	/*int rr[5000], pp[5000], ss[5000];
	rr[0] = 1, pp[0] = 0, ss[0] = 0;
	rep(i, 1, 5000) {
		rr[i] = pp[i - 1] + rr[i - 1];
		pp[i] = pp[i - 1] + ss[i - 1];
		ss[i] = rr[i - 1] + ss[i - 1];
	}*/
	while (t--) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		int m = 1 << n;
		cout << "Case #" << cas++ << ": ";
		int flg = 1, win = n % 3;
		if (n & 1) flg = -1;
		string ans;
		if (p == r && p + flg == s) {
			if (win == 0) ans = print("S", n);
			else if (win == 1) ans = print("P", n);
			else ans = print("R", n);
			cout << ans << endl;
		}
		else if (p == s && p + flg == r){
			if (win == 0) ans = print("R", n);
			else if (win == 1) ans = print("S", n);
			else ans = print("P", n);
			cout << ans << endl;
		}
		else if (r == s && r + flg == p) {
			if (win == 0) ans = print("P", n);
			else if (win == 1) ans = print("R", n);
			else ans = print("S", n);
			cout << ans << endl;
		}
		else cout << "IMPOSSIBLE\n";
	}
	return 0;
}
