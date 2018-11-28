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

const double PI = acos(-1.0);


void solve() {
	int n, m;
	cin >> n >> m;
	VS a(n);
	FOR(i,0,n) {
		cin >> a[i];
	}

	vector<char> lastCol(m, ' ');

	int res = 0;
	bool valid = true;

	FOR(i,0,n) {
		char lastInRow = ' ';
		FOR(j,0,m) {
			
			if(a[i][j] != '.') {
				bool left = false;
				bool right = false;
				FOR(k,0,m) {
					if(a[i][k] != '.') {
						if(k < j) left = true;
						if(k > j) right = true;
					}
				}

				bool up = false, down = false;
				FOR(k,0,n) {
					if(a[k][j] != '.') {
						if(k < i) up = true;
						if(k > i) down = true;
					}
				}

				if(!(up || down || left || right)) {
					valid = false;
				}
				if( (!up && a[i][j]=='^') || (!down && a[i][j]=='v') || (!left && a[i][j]=='<') || (!right && a[i][j] == '>')) {
					res ++;
				}
			}

		}
	}
	if(!valid)
		cout << "IMPOSSIBLE\n";
	else 
		cout << res << "\n";
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