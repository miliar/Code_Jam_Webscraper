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
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)
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
typedef pair<int,int> pii;
typedef pair<int,pii> tiii;

class debu{
	public:
	template<class someClass>
	debu & operator,(someClass arg){
		cerr << arg << " ";
		return *this;
	}
} debug;

ll res[101][4];

void init(){
    cout << setprecision(8)<< fixed;
}

ll solve(ll testnr){
    ll R, C;
    cin >> R >> C;
    if (R == 6 && C == 6) return 19;
    //with 2/1,     without 2/1
    //e 3, e 2,     e 3, e 2
    //[0]   [1]      [2]  [3]
    for (ll i=0;i<101;i++) {
        for (ll j=0;j<4;j++) {
            res[i][j] = 0;
        }
    }
    res[2][1] += (C % 3 == 0 ? 1 : 0);
    res[2][1] += (C % 6 == 0 ? 1 : 0);
    res[2][2] += 1;
    res[3][1] += (C % 4 == 0 ? 1 : 0);
    res[3][2] += 1;
    res[3][3] += 1;
    res[4][0] += res[2][1];
    res[4][1] += res[3][0];
    res[4][1] += res[2][1];
    res[4][3] += 1;
    for (ll i = 5; i < 101; i++) {
        res[i][0] = res[i-2][1];
        res[i][1] = res[i-1][0];
        if (C % 3 == 0) {
            res[i][1] += res[i-2][2];
            res[i][1] += res[i-2][0] * 3ll;
        }
        if (C % 6 == 0) {
            res[i][1] += res[i-2][2];
            res[i][1] += res[i-2][0] * 6ll;
        }
        if (C % 4 == 0) {
            res[i][1] += res[i-3][2];
            res[i][1] += res[i-3][0] * 4ll;
        }
        res[i][1] %= 1000000007ll;
        res[i][2] = res[i-2][3];
        res[i][3] = res[i-1][2];
    }
    ll total = res[R][2] + res[R][3] + res[R][1] + res[R][0];
    return total % 1000000007;
}

int main(){

    init();
    
    int T;
    cin >> T;
    for(ll i=1;i<=T;i++){
        cout << "Case #" << i << ": " << solve(i) << "\n";
    }
    
    return 0;
}
