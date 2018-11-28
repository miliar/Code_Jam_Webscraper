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

int R, C;
int F[111][111];

int dr[4] = { 0, 0, -1, 1 };
int dc[4] = { -1, 1, 0, 0 };

void solve() {
    cin >> R >> C;
    char c;
    REP(i, R) {
        REP(j, C) {
            cin >> c;
            if (c == '.') F[i][j] = -1;
            if (c == '<') F[i][j] = 0;
            if (c == '>') F[i][j] = 1;
            if (c == '^') F[i][j] = 2;
            if (c == 'v') F[i][j] = 3;
        }
    }

    int ans = 0;
    REP(i, R) {
        REP(j, C) {
            if (F[i][j] == -1) continue;

            int okdir = -1;
            for (int k = 0; k < 4; k++) {
                int ci = i + dr[k];
                int cj = j + dc[k];
                while (ci >= 0 && cj >= 0 && ci < R && cj < C) {
                    if (F[ci][cj] != -1) {
                        okdir = k;
                        break;
                    }
                    ci += dr[k];
                    cj += dc[k];
                }

                if (okdir == F[i][j]) {
                    break;
                }
            }

            if (okdir == -1) {
                printf("IMPOSSIBLE\n");
                return;
            }

            if (okdir != F[i][j]) {
                ans++;
            }
        }
    }
    printf("%d\n", ans);
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
	freopen("a.in", "r", stdin);
#elif _LOCAL_TEST == 1
	freopen("../input/A-small-attempt0.in", "r", stdin);
    freopen("../output/A-small0.out", "w", stdout);
#elif _LOCAL_TEST == 2
	freopen("../input/A-large.in", "r", stdin);
    freopen("../output/A-large.out", "w", stdout);
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
