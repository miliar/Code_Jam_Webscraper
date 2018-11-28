#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <list>
#include <stack>
#include <tuple>
#include <utility>
#include <complex>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <climits>
#include <typeinfo>
using namespace std;

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

#define REP(i,n) for(int i=0; i<(n); i++)
#define REPA(i,s,e) for(int i=(s); i<=(e); i++)
#define REPD(i,s,e) for(int i=(s); i>=(e); i--)
#define ALL(a) (a).begin(), (a).end()

#define PRT(a) cerr << #a << " = " << (a) << endl
#define PRT2(a, b) cerr << #a << " = " << (a) << ", " << #b << " = " << (b) << endl
#define PRT3(a, b, c) cerr << #a << " = " << (a) << ", " << #b << " = " << (b) << ", " << #c << " = " << (c) <<  endl
template <class Ty> void print_all(Ty b, Ty e) {
	cout << "[ ";
	for(Ty p=b; p!=e; ++p) {
		cout << (*p) << ", ";
	}
	cout << " ]" << endl;
}

// -----------------------------------------------------------------------------
// Code starts 
// -----------------------------------------------------------------------------

void solve() {
    int s, n;
    map<int,int> mp;
    cin >> s;
    for (int i = 0; i < s * 2 - 1; i++) {
        for (int j = 0; j < s; j++) {
            cin >> n;
            mp[n] += 1;
        }
    }

    vector<int> ans;
    for (auto& p : mp) {
        if (p.second % 2 != 0) {
            ans.push_back(p.first);
        }
    }
    sort(ALL(ans));

    REP(i, ans.size()) {
        printf("%d%c", ans[i], i == ans.size() - 1 ? '\n' : ' ');
    }
}

// -----------------------------------------------------------------------------
// Code ends 
// -----------------------------------------------------------------------------

void coding() {
    int T;
    cin >> T;
    REPA(t,1,T) {
        fprintf(stderr, "%3d / %d\n", t, T);
        printf("Case #%d: ", t);
        solve();
    }
}

#define _LOCAL_TEST 2

int main() {
#if _LOCAL_TEST == 0
	clock_t startTime = clock();
	freopen("b.in", "r", stdin);
#elif _LOCAL_TEST == 1
	freopen("../input/B-small-attempt0.in", "r", stdin);
    freopen("../output/B-small0.out", "w", stdout);
#elif _LOCAL_TEST == 2
	freopen("../input/B-large.in", "r", stdin);
    freopen("../output/B-large.out", "w", stdout);
#endif

	coding();

#if _LOCAL_TEST == 0
	clock_t elapsedTime = clock() - startTime;
	cerr << endl;
	cerr << (elapsedTime / 1000.0) << " sec elapsed." << endl;
	cerr << "This is local test" << endl;
	cerr << "Do not forget to comment out _LOCAL_TEST" << endl << endl;
#endif

}
