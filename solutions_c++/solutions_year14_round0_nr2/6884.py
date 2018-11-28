#include<cstdio>
#include<algorithm>
#include<utility>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
#include<iostream>
#include <iomanip>

// macros

#define FORE(a, b, c) for(int c=a; c<= int(b); ++c)
#define FORD(a, b, c) for(int c=a; c>= int(b); --c)
#define FORIT(cont_t, cont, it) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it)
#define REP(i, n) for(int i = 0; i < (n); ++i)
#define ALL(a) a.begin(), a.end() 
#define PR(n) printf("%d ", (int) (n)) 
#define PRL(n) printf("%lld ", (ll) (n)) 
#define SC(n) scanf("%d", &n);

#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define itr iterator

#define dbg if(0)
#define prd dbg printf

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;

typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef vector<pi> vii;

const double eps = 1e-10;

int t;
double f, c, x;
double tim, opt, tmp, gain, time_to_build;

double magic() {
	cin >> c >> f >> x;
	tim  = 0;
	gain = 2;
	opt = (double) x/2.0;
	dbg cout << c << " " << f << " " << x << " " << opt << endl;
	
	if(c > x) return opt;
	
	while(1) {
		time_to_build = c / gain;
		tim += time_to_build;
		gain += f;
		
		tmp = tim + x/gain;
		
		dbg cout << tim << ", " << gain << "gives " << tmp << endl;
		
		if(tmp < opt - eps)
			opt = tmp;
		else return opt;
		
		
	}
	return x/2.0;
}

int main() {
	cin >> t;
	REP(i, t)
		cout << "Case #" << i+1 << ": " << setprecision(10) << magic() << endl;
	return 0;
}
		
				
		
		
		
