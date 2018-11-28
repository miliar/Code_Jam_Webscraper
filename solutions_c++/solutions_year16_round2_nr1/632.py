//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
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

string tos[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

set<pair<vector<int>, string> > M;

string RES;

void rec(vector<int> a, string res) {
	int mn = SZ(res) == 0 ? 0 : (res.back() - '0');
	if (SZ(RES))
		return;
	if (M.count(MP(a, res)))
		return;
	bool isFine = true;
	FOR(i, 0, 26) {
		if (a[i] < 0)
			return;
		if (a[i] != 0)
			isFine = false;
	}
	if (isFine) {
		RES = res;
		return;
	}
	M.insert(MP(a, res));
	FOR(i, mn, 10) {
		string xx = tos[i];
		FOR(i, 0, SZ(xx)) {
			a[xx[i] - 'A'] --;
		}
		rec(a, res + (char)(i + '0'));
		FOR(i, 0, SZ(xx)) {
			a[xx[i] - 'A'] ++;
		}
	}
}

void solve() {
	M.clear();
	RES = "";
	string s;
	cin >> s;
	
	VI a(26, 0);
	FOR(i, 0, SZ(s)) {
		a[s[i] - 'A'] ++;
	}
	rec(a, "");
	cout << RES << endl;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	cin >> test;
	FOR(test_id, 0, test) {
		printf("Case #%d: ", test_id + 1);
		solve();
		cerr << test_id << endl;
	}
	return 0;
}