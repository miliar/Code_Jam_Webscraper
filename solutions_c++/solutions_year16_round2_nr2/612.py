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

using namespace std;

typedef unsigned long long      ui64;
typedef long long               i64;
typedef	vector<int>             VI;
typedef	vector<bool>            VB;
typedef	vector<VI>              VVI;
typedef	vector<string>          VS;
typedef	pair<int, int>           PII;
typedef map<string, int>         MSI;
typedef set<int>                SI;
typedef set<string>             SS;
typedef complex<double>         CD;
typedef vector< CD >            VCD;
typedef map<int, int>            MII;
typedef	pair<double, double>     PDD;

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
#define INF                     (2000000000)

#ifdef _DEBUG
#define eprintf(...) fprintf (stderr, __VA_ARGS__)
#else
#define eprintf(...) assert (true)
#endif

const double PI = acos(-1.0);

string tos(i64 a, int w) {
	string res = to_string(a);
	while (SZ(res) < w)
		res = '0' + res;
	return res;
}

pair<string, string> solve(string _s0, string _s1) {
	string s[2];
	//cin >> s[0] >> s[1];
	s[0] = _s0;
	s[1] = _s1;
	int n = SZ(s[0]);
	pair<i64, i64> a, b;
	a = b = MP(0, 0);
	VB isV(2, true);
	bool isValid = true;
	i64 c = 0;
	FOR(i, 0, n) {
		if (s[0][i] == s[1][i] && s[0][i] == '?') {
			// two ??
			if (isValid) {
				c = c * 10;
				if(a.X)
					a = min(MP(a.X * 10, a.Y * 10 + 9), MP(c + 1, c));
				else
					a = MP(c + 1, c);
				if (b.Y)
					b = min(MP(c, c + 1), MP(b.X * 10 + 9, b.Y * 10));
				else
					b = MP(c, c + 1);
				continue;
			}
			a = MP(a.X * 10, a.Y * 10 + 9);
			b = MP(b.X * 10 + 9, b.Y * 10);
			continue;
		}
		if (s[0][i] == '?') {
			if (s[1][i] == '9') {
				a = MP(a.X * 10 + 0, a.Y * 10 + 9);
				if (isValid)
					b = MP(c * 10 + 8, c * 10 + 9);
				else
					b = MP(b.X * 10 + 9, b.Y * 10 + 9);
				c = c * 10 + 9;
				continue;
			}
			if (s[1][i] == '0') {
				if (isValid)
					a = MP(c * 10 + 1, c * 10 + 0);
				else
					a = MP(a.X * 10 + 0, a.Y * 10 + 0);
				b = MP(b.X * 10 + 9, b.Y * 10 + 0);
				c = c * 10 + 0;
				continue;
			}

			if (isValid)
				a = MP(c * 10 + s[1][i]-'0' + 1, c * 10 + s[1][i] - '0');
			else
				a = MP(a.X * 10 + 0, a.Y * 10 + s[1][i] - '0');

			if(isValid)
				b = MP(c * 10 + s[1][i] - '0' - 1, c * 10 + s[1][i] - '0');
			else
				b = MP(b.X * 10 + 9, b.Y * 10 + s[1][i] - '0');

			c = c * 10 + s[1][i] - '0';
			continue;
		}


		// Vice versa
		if (s[1][i] == '?') {
			if (s[0][i] == '9') {
				if (isValid)
					a = MP(c * 10 + 9, c * 10 + 8);
				else
					a = MP(a.X * 10 + 9, a.Y * 10 + 9);

				b = MP(b.X * 10 + 9, b.Y * 10 + 0);
				c = c * 10 + 9;
				continue;
			}
			if (s[0][i] == '0') {
				a = MP(a.X * 10 + 0, a.Y * 10 + 9);
				if(isValid)
					b = MP(c * 10 + 0, c * 10 + 1);
				else
					b = MP(b.X * 10 + 0, b.Y * 10 + 0);
				c = c * 10 + 0;
				continue;
			}

			if (isValid)
				a = MP(c * 10 + s[0][i] - '0', c * 10 + s[0][i] - '0' - 1);
			else
				a = MP(a.X * 10 + s[0][i] - '0', a.Y * 10 + 9);

			if (isValid)
				b = MP(c * 10 + s[0][i] - '0', c * 10 + s[0][i] - '0' + 1);
			else
				b = MP(b.X * 10 + s[0][i] - '0', b.Y * 10 + 0);

			c = c * 10 + s[0][i] - '0';

			continue;
		}

		
		if(isValid && s[0][i] > s[1][i])
			a = MP(c * 10 + s[0][i] - '0', c * 10 + s[1][i] - '0');
		else
			a = MP(a.X * 10 + s[0][i] - '0', a.Y * 10 + s[1][i] - '0');

		if (isValid && s[0][i] < s[1][i])
			b = MP(c * 10 + s[0][i] - '0', c * 10 + s[1][i] - '0');
		else
			b = MP(b.X * 10 + s[0][i] - '0', b.Y * 10 + s[1][i] - '0');

		if (s[0][i] != s[1][i])
			isValid = false;

		c = c * 10 + s[0][i] - '0';
	}

	/*
	cerr << s[0] << " " << s[1] << endl;
	cerr << a.X << " " << a.Y << endl;
	cerr << b.X << " " << b.Y << endl;
	cerr << c << " " << isValid << endl;
	cerr << "===\n";
	*/
	if (isValid) {
		return MP(tos(c, n), tos(c, n));
	}
	if (abs(a.X - a.Y) == abs(b.X - b.Y)) {
		if (b.X < a.X || (b.X == a.X && b.Y < a.Y))
			return MP(tos(b.X, n), tos(b.Y, n));
		else
			return MP(tos(a.X, n), tos(a.Y, n));
	}
	else if (abs(a.X - a.Y) > abs(b.X - b.Y)) 
		return MP(tos(b.X, n), tos(b.Y, n));
	else 
		return MP(tos(a.X, n), tos(a.Y, n));
}

bool fit(string a, string b) {
	FOR(i, 0, SZ(a)) {
		if (a[i] != '?' && a[i] != b[i])
			return false;
	}
	return true;
}

pair<string, string> brute(string s0, string s1) {
	int t = pow(10, SZ(s0));
	PII best = MP(0, t - 1);
	FOR(i, 0, t) {
		FOR(j, 0, t) {
			if (fit(s0, tos(i, SZ(s0))) && fit(s1, tos(j, SZ(s0))) && abs(i - j) < abs(best.X - best.Y))
				best = MP(i, j);
		}
	}
	return MP(tos(best.X, SZ(s0)), tos(best.Y, SZ(s0)));
}


int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	cin >> test;
	FOR(test_id, 0, test) {
		printf("Case #%d: ", test_id + 1);
		string s0, s1;
		cin >> s0 >> s1;
		pair<string, string> a = solve(s0, s1);
		/*pair<string, string> b = brute(s0, s1);
		if (a != b) {
			cerr << "ERROR!!!\n";
			cerr << s0 << " " << s1 << "\n";
			cerr << a.X << " " << a.Y << endl;
			cerr << b.X << " " << b.Y << endl;
			cerr << "===\n";
		}*/
		cout << a.X << " " << a.Y << endl;
		cerr << test_id << endl;
	}
	return 0;
}