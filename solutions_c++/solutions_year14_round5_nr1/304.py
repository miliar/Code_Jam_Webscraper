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

using namespace std;

#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(ll (i)=0;(i)<(n);(i)++)
#define dbg(args...) {debug,args; cerr << endl;}

#define mp make_pair
#define mt(a,b,c) mp(a,mp(b,c))
#define P1(a) (a).first
#define P2(a) (a).second
#define T1(a) (a).first
#define T2(a) (a).second.first
#define T3(a) (a).second.second
#define INF 1e20
#define EPS 1e-8

typedef long long ll;
typedef pair<ll,ll> pii;
typedef pair<ll,pii> tiii;

class debu{
	public:
	template<class someClass>
	debu & operator,(someClass arg){
		cerr << arg << " ";
		return *this;
	}
} debug;


void init(){
    cout << setprecision(12)<< fixed;
}

void compare(ll t1, ll t2, ll total, ll &opt) {
    ll m = max(max(t1, t2), total - t1 - t2);
    opt = min(m, opt);
}

double solve(ll testnr){
    ll N, p, q, r, s;
    cin >> N >> p >> q >> r >> s;
    vector<ll> a(N);
    ll total = 0;
    rep(i,N) {
        a[i] = (i * p + q) % r + s;
        total += a[i];
    }
    ll tot1 = 0, tot2 = 0;
    ll i1 = -1;
    do {
        i1++;
        if ((tot1 + a[i1])*3 < total) tot1 += a[i1]; else break;
    } while (true);
    ll i2 = i1;
    do {
        if ((tot2 + a[i2])*3 < total) tot2 += a[i2]; else break;
        i2++;
    } while (true);
    
    
    ll opt = max(max(tot1, tot2), total - tot1 - tot2);
    compare(tot1, tot2, total, opt);
    compare(tot1, tot2 + a[i2], total, opt);
    while (tot1 < opt) {
        tot1 += a[i1];
        i1++;
        i2 = i1;
        tot2 = 0;
        do {
            if ((tot2 + a[i2])*2 + tot1 < total) tot2 += a[i2]; else break;
            i2++;
        } while (true);
        compare(tot1, tot2, total, opt);
        compare(tot1, tot2 + a[i2], total, opt);
    }
    return ((double)total-(double)opt)/((double)total);
}

int main(){

    init();
    
    ll T;
    cin >> T;
    for(ll i=1;i<=T;i++){
        cout << "Case #" << i << ": " << solve(i) << "\n";
    }
    
    return 0;
}
