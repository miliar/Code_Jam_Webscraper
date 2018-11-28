#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;
 
#define FOREACH(i, c) for(__typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for(__typeof(n) i = (a); i<(n); ++i)
#define REP(i, a, n) for(__typeof(n) i = (a); i<=(n); ++i)
#define ROF(i, n, a) for(__typeof(n) i = (n); i>=(a); --i)
#define error(n) cout << #n << " = " << n << endl
#define all(c) c.begin(), c.end()
#define pb push_back
#define po pop_back
#define Size(n) ((int)(n).size())
#define X first
#define Y second
int _ ;
#define scanf _ = scanf
// #define X real()
// #define Y imag()

typedef long long   ll ;
typedef long double ld ;
typedef pair<int,int> pii ;

const int MAXM = 1000 ;

int T ;

ll N ;
int M ;
ll o[MAXM] , e[MAXM] , p[MAXM] ;
map <ll,int> mp ;
ll sum[MAXM*2] ;
ll point[MAXM*2] ;

ll F(ll r) {
    return r*(r+1)/2 ;
}

ll F(ll l , ll r) { // sigma i = l to r : i
    return F(r) - F(l-1) ;
}

ll Dis(int l , int r) {
    return point[r]-point[l] ;
}

int main() {
    cin >> T ;
    REP (l,1,T) {
	// Clearing
	mp.clear() ;
	memset (sum,0,sizeof(sum)) ;
	//
	cin >> N >> M ;
	ll cur = 0 , tot = 0 ; // current answer , answer after optimizing
	for (int i = 0 ; i < M ; ++i) {
	    cin >> o[i] >> e[i] >> p[i] ;
	    mp[o[i]] = mp[e[i]] = 0 ;
	    cur += p[i] * F(1,e[i] - o[i]) ;
	}
	int siz = 0 ;
	FOREACH (it,mp) {
	    point[siz] = it->X ;
	    mp[it->X] = siz++ ;
	}
	for (int i = 0 ; i < M ; ++i) {
	    sum[mp[o[i]]] += p[i] ;
	    sum[mp[e[i]]] -= p[i] ;
	}
	for (int i = 1 ; i < siz ; ++i)
	    sum[i] += sum[i-1] ;
// 	FOR (i,0,siz)
// 	    cerr << sum[i] << " " ;
	for (int i = 0 ; i < siz-1 ; ++i) {
	    ll mn = sum[i] ;
	    for (int j = i ; j < siz-1 ; ++j) {
		mn = min(mn,sum[j]) ;
		tot += mn*F(Dis(i,j)+1,Dis(i,j+1)) ;
		sum[j] -= mn ;
	    }
	}
// 	cerr << endl ;
	cout << "Case #" << l << ": " ;
	cout << tot-cur << endl ;
    }
    return 0 ;
}
