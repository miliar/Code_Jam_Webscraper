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
#include <cstring>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SZ(x) (int)(x).size()
#define ALL(c) c.begin(),c.end()
#define ZERO(x) memset(x,0,sizeof(x))

vector<int> a;
vector<int> b;

bool is_smaller(int i, int j) {
    if (i < j) {
        return b[i] <= b[j];
    } else if (i > j) {
        return a[i] <= a[j];
    } else {
        return false;
    }
}

void alg() {
    int n;
    cin >> n;
    a.assign(n, 0);
    b.assign(n, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }
    vector<int> t(n, 0);
    vector<vector<int> > e(n);
    vector<int> out(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (is_smaller(j, i)) {
                e[j].PB(i);
                ++out[i];
            }
        }
    }
    vector<int> cinc(n, 1);
    vector<int> cdec(n, 1);

    int c = 0;
    while (c < n) {
        ++c;
        bool got = false;
        for (int i = 0; i < n; ++i) {
            if (out[i] == 0 && cinc[i] == a[i] && cdec[i] == b[i]) {
                t[i] = c;
                out[i] = -1;
                FORE (it, e[i]) {
                    --out[*it];
                }
                for (int k = i + 1; k < n; ++k) {
                    if (t[k] == 0) {
                        cinc[k] = max(cinc[k], cinc[i] + 1);
                    }
                }
                for (int k = 0; k < i; ++k) {
                    if (t[k] == 0) {
                        cdec[k] = max(cdec[k], cdec[i] + 1);
                    }
                }
                got = true;
                break;
            }
        }
        assert(got);
    }
    for (int i = 0; i < n; ++i) {
        cout << " " << t[i];
    }
    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    int d;
    cin >> d;
    for (int i = 1; i <= d; ++i) {
        cout << "Case #" << i << ":";
        alg();
    }
}
