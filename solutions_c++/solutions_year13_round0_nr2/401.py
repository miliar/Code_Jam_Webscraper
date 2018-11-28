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

const int MAXN = 100 + 7;
int a[MAXN][MAXN];

void Solve() {
	int n, m;
	scanf("%d%d",&n,&m);
	FOR(i,0,n) {
		FOR(j,0,m) {
			scanf("%d",&a[i][j]);
		}
	}
	VI max_in_row(n, 0);
	VI max_in_col(m, 0);
	FOR(i,0,n) {
		FOR(j,0,m) {
			max_in_row[i] = max( max_in_row[i], a[i][j] );
			max_in_col[j] = max( max_in_col[j], a[i][j] );
		}
	}
	bool ok = true;
	FOR(i,0,n) {
		FOR(j,0,m) {
			if(a[i][j] < min(max_in_row[i], max_in_col[j]) ) {
				ok = false;
			}
		}
	}
	if(ok)
		printf("YES");
	else
		printf("NO");
}

int main() {
	freopen("a.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(CUR_TEST,1,test+1) {
		printf("Case #%d: ",CUR_TEST);
		Solve();
		printf("\n");
	}
	return 0;
}