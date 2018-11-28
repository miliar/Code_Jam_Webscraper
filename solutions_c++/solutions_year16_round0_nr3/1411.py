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

void bits(lint K) {
    vector<int> v;
    while (K != 0) {
        cout << (K & 0x01);
        K >>= 1;
    }
    printf(" ");
}

lint isprime(lint M) {
    if (M == 0 || M == 1) return -1;

    for (lint i = 2; i * i <= M; i++) {
        if (M % i == 0) return i;
    }

    return -1;
}

lint check2(lint K, lint i) {
    lint M = 0;
    while (K != 0) {
        M = (M * i) + (K & 0x01);
        K >>= 1;
    }

    return isprime(M);
}

bool check(lint K) {
    lint x[11];
    for (int i = 10; i >= 2; i--) {
        x[i] = check2(K, i);
        if (x[i] == -1) return false;
    }

    bits(K);
    for (int i = 2; i <= 10; i++) {
        cout << x[i];
        if (i != 10) cout << " ";
    }
    cout << endl;
    return true;
}

bool check_large(lint K) {
    lint M = K;
    int i = 0;
    int ans = 0;
    for (int i = 1; M != 0; i++) {
        if ((M & 0x01) != 0) {
            ans += i % 2 == 0 ? 1 : -1;
        }
        M >>= 1;
    }

    if (ans != 0) return false;

    bits(K);
    for (int i = 2; i <= 10; i++) {
        printf("%d%c", i + 1, i == 10 ? '\n' : ' ');
    }
    return true;
}

void solve() {
    int N, J;
    cin >> N >> J;

    lint M = 1ll << (N - 2);
    int success = 0;
    for (lint i = 0; i < M; i++) {
        lint K = (1ll << (N - 1)) + (i << 1) + 1;
        if (check_large(K)) {
            success++;
            fprintf(stderr, "%d\n", success);
        }
        if (success == J) break;
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
        printf("Case #%d:\n", t);
        solve();
    }
}

#define _LOCAL_TEST 2

int main() {
#if _LOCAL_TEST == 0
	clock_t startTime = clock();
	freopen("c.in", "r", stdin);
#elif _LOCAL_TEST == 1
	freopen("../input/C-small-attempt0.in", "r", stdin);
    freopen("../output/C-small0.out", "w", stdout);
#elif _LOCAL_TEST == 2
	freopen("../input/C-large.in", "r", stdin);
    freopen("../output/C-large.out", "w", stdout);
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
