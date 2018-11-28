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

void solve(int testnr) {
	int N;
	int p = 0;	// naomi's points
	double n = 0.;
	cin >> N;
	vector<double> naomi (N, 0);
	vector<double> ken (N, 0);
	for (int i = 0; i < N; i++) cin >> naomi[i];
	for (int i = 0; i < N; i++) cin >> ken[i];
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());
	vector<double> naomi2 = naomi;
	vector<double> ken2 = ken;

	// playing deceitful war
	for (int i = 0; i < N; i++) {
		n = naomi[0];
		naomi.erase(naomi.begin());
		if (n < ken[0]) ken.pop_back();
		else {	// naomi scores
			p++;
			ken.erase(ken.begin());
		}
	}
	cout << p << " ";

	// playing war
	p = 0;				// naomi's points
	bool k = false;	// did ken score this round?
	for (int i = 0; i < N; i++) {
		n = naomi2[0];
		naomi2.erase(naomi2.begin());
		for (int j = 0; j < ken2.size(); j++) {
			k = false;
			if (ken2[j] > n) { // ken scores
				k = true;
				ken2.erase(ken2.begin() + j);
				break;
			}
		}
		if (!k) { // naomi scores
			p++;
			ken2.erase(ken2.begin());
		}
	}
	cout << p;

    return;
}

int main() {

    init();
    
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": " ;
        solve(i);
        cout << endl;
    }
    
    return 0;
}
