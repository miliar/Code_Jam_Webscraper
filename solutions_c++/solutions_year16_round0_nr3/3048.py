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

const int MAXN = 1 << 17;
int f[MAXN];

void init() {
	memset(f, -1, sizeof(f));
	FOR(i, 2, MAXN) {
		if (f[i] == -1) {
			for (int j = i + i; j < MAXN; j += i) {
				f[j] = i;
			}
		}
	}
}

i64 isp(i64 n) {
	for (int i = 2; i <= n / i; i++) {
		if (n % i == 0)
			return i;
	}
	return -1;
}

void solve(int n, int k) {
	
	init();

	FOR(z, 0, 1 << (n - 2)) {
		if (k == 0)
			break;
		int mask = (z << 1) + 1 + (1 << (n-1));
		vector<i64> ans;
		FOR(j, 2, 11) {
			i64 inI = 0;
			i64 mult = 1;
			FOR(k, 0, n) {
				if ((1 << k) & mask) {
					inI += mult;
				}
				mult *= j;
			}

			i64 dv = isp(inI);

			if (dv == -1)
				break;
			ans.push_back(dv);
		}
		if (SZ(ans) == 9) {
			RFOR(i, n, 0) {
				if ((1 << i) & mask)
					cout << 1;
				else
					cout << 0;
			}
			FOR(i, 0, 9)
				cout << " " << ans[i];
			cout << endl;
			k--;
		}
	}
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	cin >> test;
	FOR(test_id, 0, test) {
		printf("Case #%d: ", test_id + 1);
		int n, k;
		cin >> n >> k;
		solve(n, k);
		cerr << test_id << endl;
	}
	return 0;
}