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
#define INF                     (2000000000)

#ifdef _DEBUG
#define eprintf(...) fprintf (stderr, __VA_ARGS__)
#else
#define eprintf(...) assert (true)
#endif

//const double PI = acos(-1.0);

const long double eps = 1e-8;

bool eq(long double a, long double b) {
	return abs(a-b) < eps;
}

void solve() {
	int n;
	cin >> n;
	long double v, x;
	cin >> v >> x;
	vector<long double> r(n);
	vector<long double> c(n);
	FOR(i,0,n)
		cin >> r[i] >> c[i];

	if(n==1) {
		if(eq(c[0], x)) {
			printf("%.7lf\n", v / r[0]);
		}
		else {
			printf("IMPOSSIBLE\n");
		}

		return ;
	}
	
	if(eq(c[1], c[0])) {
		if(eq(c[0], x)) {
			printf("%.7lf\n", v / (r[1] + r[0]));
		}
		else {
			printf("IMPOSSIBLE\n");
		}
		return ;
	}

	if((c[0] < x && c[1] < x) || (c[0] > x && c[1] > x)) {
		printf("IMPOSSIBLE\n");
		return ;
	}

	long double t2 = (v*x*r[0] - v*r[0]*c[0])/(r[0] *r[1]*c[1] - r[1] * c[0]*r[0]);
	long double t1 = (v - r[1]*t2)/r[0];

	long double A = t1 * r[0] + t2 * r[1];
	long double B = t1 * r[0]*c[0] + t2*r[1]*c[1];

	if(!eq(A, v) || !eq(B, v*x)) {
		cerr << "Crashed~!\n";
	}

	if(min(t1, t2) < 0.0) {
		//cerr << t1 << " " << t2 << endl;
		//printf("IMPOSSIBLE\n");
		//return ;
	}

	printf("%.7lf\n", max(t1, t2));
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int tests;
	scanf("%d", &tests);
	FOR(TEST,1,tests + 1) {
		printf("Case #%d: ", TEST);
		cerr << "running test # " << TEST << "\n";
		solve();
	}
	return 0;
}