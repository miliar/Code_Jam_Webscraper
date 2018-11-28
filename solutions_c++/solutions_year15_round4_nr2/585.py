#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<iomanip>
#include<vector>
#include<string>
#include<cstdio>
#include<cstring>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

#define mp make_pair
#define X first
#define Y second

#define pb push_back
#define forI_(i,V,_) for(__typeof(V.end())i=_;i!=V.end();++i)
#define forI(i,V) forI_(i,V,V.begin())

#define rep(i,l,r) for(int i = l; i <= r; ++i)
#define per(i,r,l) for(int i = r; i >= l; --i)
#define rep_(i,l,r) for(int i = l; i < r; ++i)
#define per_(i,r,l) for(int i = r; i > l; --i)

// =====================================================
// Settings

string prob = "t";

const int OUTPUT_TO_FILE = 0;
const int MULTI_TESTCASE = 1;
const int TESTCASE_NUM_GIVEN = 1;
const int OUTPUT_CASE_NUM = 1;

const int MAXN = 0;
const int MAXM = 0;
const int P = 1000000007;

// =====================================================
// Code goes here.
// main_solve() should return if it has seen EOF if (MULTI_TESTCASE && ! TESTCASE_NUM_GIVEN).
// The return value doesn't matter otherwise.

#define FAIL { puts("IMPOSSIBLE"); return 0;}

const double eps = 1e-6;

inline double Abs( double x ) {
	if (x > 0)
		return x;
	else
		return -x;
}

inline double Det22( double a, double b, double c, double d ) {
	return a * d - b * c;
}

bool main_solve(){
	int n;
	double V, R;
	cin >> n >> V >> R;
	cout << fixed << setprecision(12);
	if ( n > 2 ) {
		double v, r;
		while ( n-- )
			cin >> v >> r;
		puts("Abort!");
		return 0;
	}
	if ( n == 1 ) {
		double v, r;
		cin >> v >> r;
		//if ( Abs( r - R ) > eps ) 
		if ( R != r )
			FAIL;
		cout << V / v << endl;
	}
	if ( n == 2 ) {
		double v1, r1, v2, r2;
		cin >> v1 >> r1 >> v2 >> r2;
		if ( r1 == r2 ) {
			if ( r1 != R )
				FAIL;
			cout << V / ( v1 + v2 ) << endl;
		} else {
			if ( ( r1 - R ) * ( r2 - R ) > 0 )
				FAIL;
			R *= V, r1 *= v1, r2 *= v2;
			double D = Det22( v1, v2, r1, r2);
			double t1 = Det22( V, v2, R, r2 ) / D;
			double t2 = Det22( v1, V, r1, R ) / D;
			cout << max ( t1, t2 ) << endl;
		}
	}
}

// =====================================================

int main(){
#ifdef ONLINE_JUDGE
	if(prob == "t")
		prob = "";
#endif
	if(prob != ""){
		freopen((prob+".in").c_str(), "r", stdin);
		if(OUTPUT_TO_FILE)
			freopen((prob+".out").c_str(), "w", stdout);
	}
	if(MULTI_TESTCASE){
		if(TESTCASE_NUM_GIVEN){
			int TC;
			scanf("%d\n", &TC);
			rep(T, 1, TC){
				if(OUTPUT_CASE_NUM)
					printf("Case #%d: ", T);
				main_solve();
			}
		}else{
			while(main_solve());
		}
	}else{
		main_solve();
	}
	return 0;
}
