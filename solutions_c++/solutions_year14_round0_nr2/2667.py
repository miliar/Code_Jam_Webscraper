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
typedef pair<int, int> pii;
typedef pair<int, pii> tiii;

class debu {
	public:
	template<class someClass>
	debu & operator,(someClass arg) {
		cerr << arg << " ";
		return *this;
	}
} debug;


void init() {
    cout << setprecision(8) << fixed;
}

double solve(int testnr) {
	double C, F, X;
	cin >> C;
	cin >> F;
	cin >> X;
	double t = 0;	// time
	double N = 0;		// number of farms
	// cookie_prod = 2 + N*F
	// time until buy next cookie farm = C / cookie_prod
	while (X / (2 + (N+1)*F) + C / (2 + N*F) < X / (2 + N*F)) {
		// buy cookie farm
		t += C / (2 + N*F);
		N++;
	}
	t += X / (2 + N*F);
    return t;
}


int main() {

    init();
    
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": " << solve(i) << "\n";
    }
    
    return 0;
}
