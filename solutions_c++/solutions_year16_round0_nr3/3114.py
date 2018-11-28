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
#define INF                     (2000000000)

#ifdef _DEBUG
#define eprintf(...) fprintf (stderr, __VA_ARGS__)
#else
#define eprintf(...) assert (true)
#endif

bool isPrime(LL n) {
	if (n <= 2)
		return true;
	for (LL i = 2; i*i <= n; i++) {
		if (n%i == 0) {
			return false;
		}
	}
	return true;
}

set<LL> devs(LL n) {
	set<LL> d;
	for (LL i = 2; i*i <= n; i++) {
		if (n%i == 0) {
			d.insert(i);
			if (n / i != i) {
				d.insert(n / i);
			}
		}
	}
	return d;
}

LL cc[11];
LL st[22][22];

string binary(LL n) {
	//cout << n << "-";
	string s = "";
	while (n) {
		if (n % 2 == 1) {
			s = "1" + s;
		}
		else {
			s = "0" + s;
		}
		n /= 2;
	}
	return s;
}

set<LL> a[11];
LL res[11];
int us[11];

bool isOk(LL n) {
	//cout << n << endl;
	FOR(i, 0, 11)
		cc[i] = 0;
	int s = 0;
	while (n) {
		if (n % 2 == 1) {
			FOR(i, 2, 11) {
				cc[i] += st[i][s];
				//cout <<i<<" "<<s<<" "<< cc[i] << " - " << st[i][s] << endl;
			}
		}
		s++;
		n /= 2;
	}

	FOR(i, 2, 11) {
		if (isPrime(cc[i]))
			return false;
		a[i] = devs(cc[i]);
	}

	CLEAR(us, 0);

	FOR(i, 2, 11) {
		int ms = 10000000, x=-1;
		FOR(j,2,11)
			if (!us[j] && a[j].size() > 0 && a[j].size()<ms ) {
				ms = a[j].size();
				x = j;
			}
		if (x == -1) {
			return false;
		}
		
		us[x] = 1;

		LL d = (*a[x].begin());
		//cout << d << endl;
		res[x] = d;

		FOR(j, 2, 11)
			a[j].erase(d);
	}

	return true;
}

void solve(int t) {
	cout << "Case #" + std::to_string(t) + ":"<<endl;
	int n, k;
	cin >> n >> k;
	//cout << (1 << (n - 1)) + 1 << " " << (1 << n) << endl;
	for (int i = (1 << (n - 1)) + 1; i < (1 << n); i += 2) {
		if (isOk(i)) {
			FOR(j, 2, 11) {
				//cout << cc[j] << " ";
			}
			//cout << endl;
			cout << binary(i);
			FOR(j, 2, 11) {
				if (cc[j] % res[j] != 0) {
					cout << "--------------------------";
				}
				FOR(q, j + 1, 11) {
					if (res[q] == res[j]) {
						cout << "--------------------------";
					}
				}
				cout << " " << res[j];
			}
			cout << endl;
			k--;
		}
		if (k == 0)
			break;
	}
}

int main() {
	FOR(i, 2, 11) {
		st[i][0] = 1;
		FOR(j, 1, 17) {
			st[i][j] = st[i][j - 1] * 1ll * i;
			//cout << st[i][j] << " ";
		}
		//cout << endl;
	}
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t;
	cin >> t;
	FOR(i, 0, t) {
		solve(i+1);
	}
	return 0;
}
