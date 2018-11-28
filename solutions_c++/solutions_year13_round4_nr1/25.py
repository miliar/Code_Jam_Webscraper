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

const LL MD = 1000002013;
const LL D2 = 500001007;

void ad(LL& a, LL b) {
    a = (a + b % MD + MD) % MD;
}

LL mul(LL a, LL b) {
    return (a % MD * (LL) (b % MD)) % MD;
}

LL cost(LL n, LL le, LL ri) {
    LL len = ri - le;
    LL res = mul(n, len);
    ad(res, -mul(mul(len, len - 1), D2));
    return res;
}

void alg() {
    int n, m;
    cin >> n >> m;
    map<LL, LL> v;
    LL result = 0;
    for (int i = 0; i < m; ++i) {
        int le, ri, passengers;
        cin >> le >> ri >> passengers;
        v[le] += passengers;
        v[ri] -= passengers;
        ad(result, mul(cost(n, le, ri), passengers));
    }
    vector<pair<LL, LL> > riding;
    FORE (it, v) {
        if (it->ND > 0) {
            riding.PB(*it);
        } else if (it->ND < 0) {
            LL rem = -it->ND;
            while (rem > 0) {
                pair<LL, LL> cur = riding.back();
                riding.pop_back();
                LL used = min(rem, cur.second);
                ad(result, -mul(cost(n, cur.first, it->ST), used));
                cur.second -= used;
                rem -= used;
                if (cur.second > 0) {
                    riding.PB(cur);
                }
            }
        }
    }
    cout << result << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    int d;
    cin >> d;
    for (int i = 1; i <= d; ++i) {
        cout << "Case #" << i << ": ";
        alg();
    }
}
