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

int res;
int v;
bool used[31];

void rec(int Mask, int maxAdded, int added) {
	
	if(Mask == ((1<<(v+1)) - 1) ) {
		res = min(res, added);
	}

	if(added > min(6, res))
		return ;

	FOR(i, maxAdded + 1, v + 1) if( !used[i] ) {
		int mask = Mask;
		RFOR(j,v+1,0) {
			if((mask & (1<<j)) && j + i <= v )
				mask |= 1<< (j+i);
		}
		rec(mask, i, added + 1);
	}
}

void solve2() {
	int c, n;
	cin >> c >> n >> v;
	VI a(n);
	
	FOR(i,0,n) {
		cin >> a[i];
	}

	set<i64> Set(ALL(a));
	int res = 0;
	i64 mx = 0;
	while(true) {
		if(mx >= v)
			break;
		i64 next = mx + 1;
		if(!Set.count(next))
			res++;
		Set.erase(next);
		mx = next * (1 + c) - 1;

		while(!Set.empty() && (*Set.begin()) <= mx) {
			i64 val = *Set.begin();
			Set.erase(val);
			mx = mx + val * c;
		}
	}
	cout << res << endl;
}

void solve() {
	int c, n;
	cin >> c >> n >> v;
	VI a(n);
	memset(used, false,sizeof(used));
	FOR(i,0,n) {
		cin >> a[i];
		used[a[i]] = true;
	}

	//  C == 1
	res = INF;
	VI r(v + 1);
	r[0] = 1;
	FOR(i,0,SZ(a)) {
		RFOR(j,v + 1,0) {
			if(r[j] && (j + a[i] <= v) )
				r[j + a[i]] = 1;
		}
	}
	int mask = 0;
	FOR(i,0,v + 1)
		if(r[i])
			mask |= 1<<i;
	rec(mask, 0, 0);
	cout << res << endl;
}

void solveTest(int test) {
	printf("Case #%d: ", test);
	solve2();
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