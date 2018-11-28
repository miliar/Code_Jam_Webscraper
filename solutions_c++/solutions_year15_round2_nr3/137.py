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

// macros

#define FORE(c, a, b) for(int c=a; c<= int(b); ++c)
#define FORD(c, a, b) for(int c=a; c>= int(b); --c)
#define FORIT(it, cont, cont_t) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it)
#define REP(i, n) for(int i = 0; i < (n); ++i)
#define ALL(a) a.begin(), a.end() 
#define PR(n) printf("%d ", (int) (n)) 
#define PRL(n) printf("%lld ", (ll) (n)) 

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
typedef vector<vi> vvi;
typedef queue<pair<ll, int> > qll;

// actual code

int n, ans, tt, d, h, m;

void compute(int ki) {
	cin >> n;
	vii hike;
	int hit = 0;
	
	REP(i, n) {
		cin >> d >> h >> m;
		hike.pb(mp(m, d));
		if(h == 2)
			hike.pb(mp(m+1, d));
	}
	
	if(hike.size() == 2) {
		sort(ALL(hike));
		if(hike[0].xx < hike[1].xx) {
			ll t1 = (ll) (360 - hike[0].yy) * hike[0].xx; // szybszy
			ll t2 = (ll) (360 - hike[1].yy) * hike[1].xx;
			
			if(((ll) hike[0].xx * 360) + t1 <= t2)
				hit = 1;
			}
		}
		
	cout << "Case #" << ki << ": " << hit << endl;
	cerr << "Case #" << ki << ": " << hit << endl;		
}
		

int main() {
	cin >> tt;
	REP(ti, tt)
		compute(ti + 1);
	return 0;
}
