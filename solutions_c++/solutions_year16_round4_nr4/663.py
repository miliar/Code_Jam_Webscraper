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
#define INF                     (1000000000)

#ifdef _DEBUG
#define eprintf(...) fprintf (stderr, __VA_ARGS__)
#else
#define eprintf(...) assert (true)
#endif

int n;
string s[10];
int a[5][5];
int m[5];
int p[5];

bool valid(int w) {
	if (w >= n)
		return true;
	bool r = false;
	FOR(i, 0, n) {
		if (a[p[w]][i] == 1 && m[i] == 1) {
			m[i] = 0;
			r = true;
			if (valid(w + 1) == false) {
				return false;
			}
			m[i] = 1;
		}
	}
	return r;
}

int ansForMask(int mask) {
	CLEAR(a, 0);
	int c = 0;
	FOR(i, 0, n*n) {
		if (mask & (1 << i)) {
			a[i / n][i%n] = 1;
			c++;
		}
	}

	FOR(i, 0, n) {
		FOR(j, 0, n) {
			//cout << a[i][j];
			if (s[i][j] == '1' && a[i][j] == 0)
				return INF;
		}
		//cout << endl;
	}
	/*if (c == 4) {
		FOR(i, 0, n) {
			FOR(j, 0, n)
				cout << a[i][j];
			cout << endl;
		}
		cout << endl;
	}*/
	FOR(i, 0, n) {
		p[i] = i;
	}
	do {
		FOR(i, 0, n)
			m[i] = 1;
		if (valid(0) == false)
			return INF;
	} while (next_permutation(p, p + n));
	
	return c;
}

void solve(int t) {
	cout << "Case #" + to_string(t) + ": ";
	cin >> n;
	int k = 0;
	FOR(i, 0, n) {
		cin >> s[i];
		FOR(j, 0, n) {
			if (s[i][j] == '1')
				k++;
		}
	}
	int ans = INF;
	FOR(mask, 0, 1 << (n*n)) {
		//cout <<mask<<" "<< ansForMask(mask) << endl;
		ans = min(ans, ansForMask(mask));
	}
	cout << ans - k << endl;
}

int main() {
	freopen("D-small-attempt0.in","r",stdin);
	freopen("Ds.out","w",stdout);
	int t;
	cin >> t;
	FOR(i, 0, t) {
		solve(i+1);
	}
	return 0;
}
