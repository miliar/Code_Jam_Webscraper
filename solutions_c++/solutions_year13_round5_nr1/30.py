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

typedef long double LD;

const int n = 37;

LD alg() {
    LL B;
    int m;
    cin >> B >> m;
    vector<LL> v(n);
    for (int i = 0; i < m; ++i) {
        cin >> v[i];
    }
    sort(ALL(v));
    LD result = 0;
    for (int k = 1; k <= n; ++k) {
        LL l = 0LL;
        LL r = (LL) 1e18;
        while (l < r) {
            LL c = (l + r + 1) / 2;
            LL cost = 0;
            for (int i = 0; i < k; ++i) {
                cost += max(0LL, c - v[i]);
                if (cost > B) {
                    break;
                }
            }
            if (cost <= B) {
                for (int i = k; i < n; ++i) {
                    cost += max(0LL, c + 1 - v[i]);
                    if (cost > B) {
                        break;
                    }
                }
            }
            if (cost > B) {
                r = c - 1;
            } else {
                l = c;
            }
        }
        if (l >= v[k - 1]) {
            LL sum = 0;
            for (int i = 0; i < k; ++i) {
                sum += l - v[i];
            }
            LL cost = sum;
            for (int i = k; i < n; ++i) {
                cost += max(0LL, l + 1 - v[i]);
            }
            LD v = sum / (LD) k;
            result = max(result, 36 * v - cost);
        }
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    int d;
    cin >> d;
    for (int i = 1; i <= d; ++i) {
        cout << fixed << setprecision(10);
        cout << "Case #" << i << ": " << alg() << endl;
    }
}
