//batch scheduling 2002
//#include <bits/stdc++.h>
#include <vector>
#include <cstdio>
#include <deque>
#include <iostream>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < n; i++)
#define re return
#define sz(a) (int)a.size()
#define fi first
#define se second
#define mp(a, b) make_pair(a, b)
typedef long long ll;
typedef double ld;
typedef pair<ld, ld> pld;
typedef vector<ll> vi;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
const ll cnn = 800, sz_g = 200000, inf = 1000000000LL, mod2 = 5000000, /*mod = inf + 7, */ma = 128 * 1024;
int n, r, p, s;

void my_assert(bool ok) {
	if (!ok) while(true);	
}


string a = "", ans;

bool ok(string s) {
	if (sz(s) == 1) re true;
	string s1 = "";
	for (int i = 0; i < sz(s); i += 2) {
		if (s[i] == s[i + 1]) re false;
		if (s[i] == 'R' && s[i + 1] == 'S') s1 += "R";
		if (s[i + 1] == 'R' && s[i] == 'S') s1 += "R";
		if (s[i] == 'P' && s[i + 1] == 'S') s1 += "S";
		if (s[i + 1] == 'P' && s[i] == 'S') s1 += "S";
		if (s[i] == 'R' && s[i + 1] == 'P') s1 += "P";
		if (s[i + 1] == 'R' && s[i] == 'P') s1 += "P";
	}
	re ok(s1);
}
bool fc(int k, int p, int q) {
	//cout << k << " " << p << " " << q << endl;
	//cout << a << endl;
	if (k + p + q == 0) {
		if (ok(a)) {
			ans = a;
			re true;
		}
		re false;
	}
	if (p) {
		a += "P";
		if (fc(k, p - 1, q)) {
			a.erase(sz(a) - 1);
			re true;
		}
		a.erase(sz(a) - 1);
	}
	if (k) {
		a += "R";
		if (fc(k - 1, p, q)) {
			a.erase(sz(a) - 1);
			re true;
		}
		a.erase(sz(a) - 1);
	}
	if (q) {
		a += "S";
		if (fc(k, p, q - 1)) {
			a.erase(sz(a) - 1);
			re true;
		}
		a.erase(sz(a) - 1);
	}
	re false;
}

void neww(string s, string &t) {
	t = "";
	forn (i, sz(s)) {
		if (s[i] == 'P') t += "PR";
		if (s[i] == 'R') t += "RS";
		if (s[i] == 'S') t += "PS";
	}
}

void srt(string &s) {
	string q1 = "", q2 = "";
	for (int i = 1; 2 * i <= sz(s); i += i) {
		string pp = "";
		for (int j = 0; j < sz(s); j += 2 * i) {
			q1 = "";
			for (int qq = j; qq < j + 2 * i; qq++)
				q1 += s[qq];
			q2 = "";
			for (int qq = j + i; qq < j + 2 * i; qq++)
				q2 += s[qq];
			for (int qq = j; qq < j + i; qq++)
				q2 += s[qq];
			pp += min(q1, q2);
		}
		s = pp;
	}
} 

int main() {
	//iostream::sync_with_stdio(0), cin.tie(0);
	freopen("sum.in", "r", stdin);
	freopen("sum.out", "w", stdout);
	int t;
	cin >> t;
	forn (i, t) {
		/*n = 5;
		r = rand() % ((1 << (n)) + 1);
		p = rand() % ((1 << (n)) + 1 - r);
		s = (1 << n) - r - p;*/
		cin >> n >> r >> p >> s;
		string s1 = "S", s2 = "R", s3 = "P";
		forn (i, n) {
			neww(s1, s1);
			neww(s2, s2);
			neww(s3, s3);
		}
		srt(s1);
		srt(s2);
		srt(s3);
		//cout << s1 << endl;
		//cout << s2 << endl;
		//cout << s3 << endl;
		int k[3] = {0, 0, 0}, q[3] = {0, 0, 0}, c[3] = {0, 0, 0};
		forn (i, sz(s1)) {
			if (s1[i] == 'R') k[0]++;
			if (s1[i] == 'P') k[1]++;
			if (s1[i] == 'S') k[2]++;
			if (s2[i] == 'R') q[0]++;
			if (s2[i] == 'P') q[1]++;
			if (s2[i] == 'S') q[2]++;
			if (s3[i] == 'R') c[0]++;
			if (s3[i] == 'P') c[1]++;
			if (s3[i] == 'S') c[2]++;
		}
		ans = "IMPOSSIBLE";
		if (k[0] == r && k[1] == p && k[2] == s && (ans == "IMPOSSIBLE" || ans > s1)) {
			ans = s1;
		}
		if (q[0] == r && q[1] == p && q[2] == s && (ans == "IMPOSSIBLE" || ans > s2)) {
			ans = s2;
		}
		if (c[0] == r && c[1] == p && c[2] == s && (ans == "IMPOSSIBLE" || ans > s3)) {
			ans = s3;
		}
		//string ans1 = ans; ans = "IMPOSSIBLE";
		//fc(r, p, s);
		/*if (ans != ans1) {
			cout << ans << " " << ans1 << "\n";
			cout << n << " " << r << " " << p << " " << s << "\n";
			re 0;
		}*/
		//cout << 
		//a = "";
		//fc(r, p, s);
		cout << "Case #" << i + 1 << ": " << ans << "\n";
	}	
	re 0;
}  