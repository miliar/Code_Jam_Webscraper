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

void solve() {
	int n;
	cin >> n;
	vector<pair<string, string> > s(n);
	FOR(i, 0, n)
		cin >> s[i].X >> s[i].Y;
	int res = 0;
	FOR(mask, 0, 1 << n) {
		set<string> f;
		set<string> se;
		int k = n;
		FOR(i, 0, n) {
			if(mask & (1<<i)) {
				k--;
				f.insert(s[i].X);
				se.insert(s[i].Y);
			}
		}
		bool ok = true;

		FOR(i, 0, n) {
			if ((mask & (1 << i)) == 0) {
				if (f.count(s[i].X) + se.count(s[i].Y) != 2)
					ok = false;
			}
		}
		if (ok)
			res = max(res, k);
	}
	cout << res << endl;
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