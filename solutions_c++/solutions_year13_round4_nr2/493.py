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

int T ;
ll N , P ;

ll Bad(ll mid) {
    ll sum = 0 ;
    ll x = N-1 ;
    for (int i = 1 ; (1ll<<i) <= mid ; ++i , --x) {
	sum += (1ll<<x) ;
    }
    return sum+1 ;
}

ll mn() {
    ll l = 1 , r = (1ll<<N) ;
    while (l < r) {
	ll mid = (l+r+1)/2 ;
	if (Bad(mid) > P)
	    r = mid-1 ;
	else
	    l = mid ;
    }
    return l-1 ;
}

ll Good(ll mid) {
    ll x = (1ll<<N)-mid+1 ;
    return (1ll<<N)-Bad(x)+1 ;
}

ll mx() {
    ll l = 1 , r = (1ll<<N) ;
    while (l < r) {
	ll mid = (l+r+1)/2 ;
	if (Good(mid) <= P)
	    l = mid ;
	else
	    r = mid-1 ;
    }
    return l-1 ;
}

int main() {
//     N = 3 ;
//     cerr << Bad(1) << " " << Bad(2) << " " << Bad(3) << " " << Bad((1ll<<N)-1) << " " << Bad(1ll<<N) << endl ;
    cin >> T ;
    REP (l,1,T) {
	cin >> N >> P ;
	cout << "Case #" << l << ": " << mn() << " " << mx() << endl ;
    }
    return 0 ;
}
