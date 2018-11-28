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

double P[100];
int n, k;
int id[100];
int masks[1000000];
int Cmasks = 0;
double f() {
	double r = 0;
	FOR(q, 0, Cmasks) {
		int mask = masks[q];
		double x = 1.0;
		FOR(i, 0, k) {
			if (mask & (1 << i)) {
				x *= P[id[i]];
			}
			else {
				x *= (1. -P[id[i]]);
			}
		}
		r += x;
	}
	return r;
}


void solve(int t) {
	cout << "Case #" + to_string(t) + ": ";
	cin >> n >> k;
	Cmasks = 0;
	double ans = 0;
	FOR(mask, 0, 1 << k) {
		int c = 0;
		FOR(i, 0, k) {
			if (mask & (1 << i)) {
				c++;
			}
		}
		if (c == k / 2) {
			masks[Cmasks++] = mask;
		}
	}

	FOR(i, 0, n) {
		cin >> P[i];
	}

	FOR(mask, 0, 1 << n) {
		int c = 0;
		FOR(i, 0, n) {
			if (mask & (1 << i)) {
				id[c++] = i;
			}
		}
		if (c == k) {
			ans = max(ans, f());
		}
	}
	printf("%.7f\n", ans);
	//cout << ans << endl;
}

int main() {
	freopen("B-small-attempt0 (1).in","r",stdin);
	freopen("Bs.out","w",stdout);
	int t;
	cin >> t;
	FOR(i, 0, t) {
		solve(i+1);
	}
	return 0;
}
