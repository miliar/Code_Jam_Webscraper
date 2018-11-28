//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
#pragma comment(linker,"/STACK:935544320") /*32Mb*/
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
typedef	pair<int,int>           PII;
typedef map<string,int>         MSI;
typedef set<int>                SI;
typedef set<string>             SS;
typedef complex<double>         CD;
typedef vector< CD >            VCD;
typedef map<int,int>            MII;
typedef	pair<double,double>     PDD;

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

const double PI = acos(-1.0);

string keyboard, targetWord;
int maxL;

int check(string s) {
	int res = 0;
	FOR(i,0,SZ(s) - SZ(targetWord) + 1) {
		if(targetWord == s.substr(i,SZ(targetWord))) {
			res++;
		}
	}
	return res;
}

int sum;
int cnt;
int mx;

void rec(string x) {
	if(SZ(x) == maxL) {
		int c = check(x);
		sum += c;
		cnt ++;
		mx = max(mx, c);
		return ;
	}
	FOR(i,0,SZ(keyboard)) {
		string tmp = x;
		tmp.PB(keyboard[i]);
		rec(tmp);
	}
}

void solve() {
	int k, l;
	cin >> k >> l >> maxL;
	cin >> keyboard;
	cin >> targetWord;

	sum = cnt = mx = 0;
	rec("");
	double av = 1.0 * sum / (0. + cnt);
	double res = mx * 1.0  - av;
	printf("%.8f\n", res);
}

void solveTest(int test) {
	printf("Case #%d: ", test);
	solve();
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int TEST_NUM;
	cin >> TEST_NUM;
	FOR(TEST,0,TEST_NUM) {
		cerr << "solving test #" << TEST + 1 << endl;
		solveTest(TEST + 1);
	}
	return 0;
}