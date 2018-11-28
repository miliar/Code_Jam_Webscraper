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

int N;
double X, V;
double Rs[111];
double Cs[111];
double A[111][111];
double b[111];
double t[111];

void failed() {
    printf("IMPOSSIBLE\n");
}

void solve() {
    cin >> N >> V >> X;
    REP(i, N) {
        cin >> Rs[i] >> Cs[i];
    }
    
    if (N > 2) {
        failed();
        return;
    }

    if (N == 1) {
        if (Cs[0] != X) {
            failed();
            return;        
        }
        printf("%.8f\n", V / Rs[0]);
        return;
    }

    if (Cs[0] == X && Cs[1] == X) {
        printf("%.8f\n", V / (Rs[0] + Rs[1]));
        return;
    }

    A[0][0] = Rs[0];
    A[0][1] = Rs[1];
    A[1][0] = Rs[0] * Cs[0];
    A[1][1] = Rs[1] * Cs[1];
    b[0] = V;
    b[1] = V * X;

    double det = A[0][0] * A[1][1] - A[1][0] * A[0][1];

    t[0] = ( A[1][1] * b[0] - A[0][1] * b[1]) / det;
    t[1] = (-A[1][0] * b[0] + A[0][0] * b[1]) / det;

    if ((Cs[0] > X && Cs[1] > X) || (Cs[0] < X && Cs[1] < X)) {
        failed();
        return;    
    }

    double ans = max(t[0], t[1]);
    printf("%.8f\n", ans);
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

#define _LOCAL_TEST 1

int main() {
#if _LOCAL_TEST == 0
	clock_t startTime = clock();
	freopen("b.in", "r", stdin);
#elif _LOCAL_TEST == 1
	freopen("../input/B-small-attempt4.in", "r", stdin);
    freopen("../output/B-small4.out", "w", stdout);
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
