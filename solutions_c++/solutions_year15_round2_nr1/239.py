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

typedef vector<ll> vi;
typedef set<ll> si;
typedef map<ll, int> mi;
typedef pair<int, int> pi;
typedef vector<pi> vii;
typedef vector<vi> vvi;
typedef queue<pair<ll, int> > qll;

// actual code

const int NMAX = 1000000;

int n;
int tt;
int vis[NMAX + 10];

ll rev(ll x) {
	dbg cout << "rev " << x;
	vi dig;
	while(x) {
		dig.pb(x % 10);
		x /= 10;
	}
	//reverse(ALL(dig));
	FORIT(it, dig, vi) {
		x *= 10;
		x += *it;
	}
	dbg cout << " = " << x << endl;
	return x;
}
	

void compute(int ki) {
	cin >> n;
	int k = vis[n];
	
	cout << "Case #" << ki << ": " << k << endl;
	cerr << "Case #" << ki << ": " << k << endl;
}
		

int main() {
	FORE(i, 1, NMAX)
		vis[i] = NMAX + 1;
	
	vis[1] = 1;
	FORE(i, 1, NMAX) {
		int j = i + 1;
		vis[j] = min(vis[j], vis[i] + 1);
		
		j = rev(i);
		if(j > i)
			vis[j] = min(vis[j], vis[i] + 1);
	}
		
	
	cin >> tt;
	REP(ti, tt)
		compute(ti + 1);
	return 0;
}
