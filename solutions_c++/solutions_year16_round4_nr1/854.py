//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#define _CRT_SECURE_NO_DEPRECATE
#include<sstream>
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<memory.h>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<complex>
#include<set>
#include<algorithm>
#include <iomanip>

using namespace std;

typedef unsigned long long      ui64;
typedef long long               i64;
typedef long long               LL;
typedef vector<int>             VI;
typedef vector<bool>            VB;
typedef vector<VI>              VVI;
typedef vector<string>          VS;
typedef pair<int, int>           PII;
typedef map<string, int>         MSI;
typedef set<int>                SI;
typedef set<string>             SS;
typedef complex<double>         CD;
typedef vector< CD >            VCD;
typedef map<int, int>            MII;
typedef pair<double, double>     PDD;

#define PB                      push_back
#define MP                      make_pair
#define X                       first
#define Y                       second
#define FOR(i, a, b)            for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b)           for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b)             memset(a, b, sizeof(a))
#define SZ(a)                   int((a).size())
#define ALL(a)                  (a).begin(), (a).end()
#define RALL(a)                 (a).rbegin(), (a).rend()
#define INF                     (1000000000000000000)

#ifdef _DEBUG
#define eprintf(...) fprintf (stderr, __VA_ARGS__)
#else
#define eprintf(...) assert (true)
#endif

string W[555];

int R, S, P;

string f(string s) {
	string r = "";
	FOR(i, 0, s.length()) {
		r += W[s[i]];
	}
	return r;
}

string buidS(string s, int n) {
	string r = "";
	FOR(i, 0, n) {
		r = f(s);
		s = r;
	}
	return r;
}

string orderS(string s){
	if (s.length() == 1) {
		return s;
	}
	string a = "", b = "";
	int n = s.length();
	FOR(i, 0, n) {
		if (i < n / 2)
			a += s[i];
		else
			b += s[i];
	}
	a = orderS(a);
	b = orderS(b);
	return min(a, b) + max(a, b);
}

bool isOk(string s) {
	int r = 0, ss = 0, p = 0;
	FOR(i, 0, s.length()) {
		if (s[i] == 'R') {
			r++;
		}
		if (s[i] == 'S') {
			ss++;
		}
		if (s[i] == 'P') {
			p++;
		}
	}
	return r == R && ss == S && p == P;
}

string ans(int n) {
	string ans = "Z";
	string r = buidS("R", n);
	if (isOk(r)) {
		ans = min(ans, orderS(r));
	}

	r = buidS("S", n);
	if (isOk(r)) {
		ans = min(ans, orderS(r));
	}

	r = buidS("P", n);
	if (isOk(r)) {
		ans = min(ans, orderS(r));
	}
	if (ans == "Z") {
		ans = "IMPOSSIBLE";
	}
	return ans;
}

char per[11];

char Win(char c1, char c2) {
	if (c2 < c1)
		swap(c1, c2);
	if (c1 == 'R' && c2 == 'S')
		return c1;
	if(c1 == 'P' && c2 == 'S')
		return c2;
	if(c1 == 'P' && c2 == 'R')
		return c1;
	throw - 1;
}

bool isValid(string s) {
	while (s.length() > 1) {
		string r = "";
		for (int i = 0; i < s.length(); i += 2) {
			if (s[i] == s[i + 1]) {
				return false;
			}
			r += Win(s[i], s[i + 1]);
		}
		s = r;
	}
	return true;
}

string brut(int n) {
	n *= 2;
	int k = 0;
	FOR(i, 0, P) {
		per[k++] = 'P';
	}
	FOR(i, 0, R) {
		per[k++] = 'R';
	}
	FOR(i, 0, S) {
		per[k++] = 'S';
	}
	do {
		string s = "";
		FOR(i, 0, k) {
			s += per[i];
		}
		if (isValid(s)) {
			return s;
		}

	} while (next_permutation(per, per + k));
	return "IMP";
}

void solve(int t) {
	cout << "Case #" + to_string(t) + ": ";
	int n;
	cin >> n >> R >> P >> S;
	cout << ans(n) << endl;
	//cout << ans(n)<<" "<<brut(n) << endl;
}

int main() {
	W['R'] = "RS";
	W['S'] = "PS";
	W['P'] = "PR";
	freopen("A-large (1).in","r",stdin);
	freopen("Al.out","w",stdout);
	int t;
	cin >> t;
	FOR(i, 0, t) {
		solve(i+1);
	}
	return 0;
}
