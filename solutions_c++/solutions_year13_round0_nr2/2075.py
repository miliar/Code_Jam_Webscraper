#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <memory>
#include <cassert>
#include <climits>
using namespace std;

#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define ALL(a) (a).begin(), (a).end()

#define DBG(x) cout << #x << " = " << x << endl
// #define DBG(x) ;

const string XWON = "X won";
const string YWON = "O won";
const string DRAW = "Draw";
const string IN_PROGRESS = "Game has not completed";

template<typename T>
void dbg_vector(const vector<T>& v, const string& name) {
    cout << name << " = ";
    REP(i, SIZE(v)) {
        cout << v[i] << ' ';
    }
    cout << endl;
}

bool doit(const vector< vector<int> >& a) {
    int N = SIZE(a);
    int M = SIZE(a[0]);
    vector<int> mxi(N, 0);
    vector<int> mxj(M, 0);
    REP(i, N) REP(j, M) {
        mxi[i] = max(mxi[i], a[i][j]);
        mxj[j] = max(mxj[j], a[i][j]);
    }
    REP(i, N) REP(j, M) {
        if (a[i][j] < mxi[i] && a[i][j] < mxj[j]) {
            return false;
        }
    }
    return true;
}


int main() {
    int tests;
    cin >> tests;
    REP(zzz, tests) {
        int N, M;
        cin >> N >> M;
        vector< vector<int> > vi(N, vector<int>(M));
        REP(i, N) REP(j, M) cin >> vi[i][j];
        cout << "Case #" << zzz + 1 << ": " << (doit(vi) ? "YES" : "NO")  << endl;
    }

    return 0;
}
