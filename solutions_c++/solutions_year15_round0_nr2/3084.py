#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <fstream>
#include <iostream>
#include <utility>
#include <iomanip>
#include <stack>
#include <list>
#include <sstream>
using namespace std;
#define PB push_back
#define MP make_pair
#define REP(i, n) for (int i(0); i < n; ++i)
#define REP1(i, n) for (int i(1); i < n; ++i)
#define FOR(i, a, b) for (int i(a); i <= b; ++i)

int tc;
int n;
vector<int> q;

int solve() {
    int m = q[0];
    if (m == 1) return 1;
    if (m == 2) return 2;
    int res = m;
    for (int i = 2; i < m; i++) {

    }
    REP1(i, m) { // try split into max_i pile
        int _res = 0;
        REP(j, q.size()) { // for each item j
            if (q[j] > i) {
                _res += ((q[j] + i - 1) / i - 1);
                //cout<<"-> "<<_res<<endl;
            }
        }
        _res += i;
        //cout<<"i: "<<i<<", _res: "<<_res<<endl;
        res = min(res, _res);
    }
    return res;
}

int main(int argc, char* argv[]) {
    cin >> tc;
    int tcIndex = 1;
    REP(i, tc) {
        q.clear();
        cin >> n;
        REP(j, n) {
            int d;
            cin >> d;
            q.push_back(d);
        }
        sort(q.begin(), q.end(), greater<int>());
        printf("Case #%d: %d\n", tcIndex, solve());
        tcIndex++;
    }
    return 0;
}
