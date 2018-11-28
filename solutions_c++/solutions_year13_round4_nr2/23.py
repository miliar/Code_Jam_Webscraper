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

LL worst_position(int n, LL x) {
    if (x == 0) {
        return 1;
    } else {
        return (1LL << (n - 1)) + worst_position(n - 1, (x - 1) / 2);
    }
}

LL best_position(int n, LL x) {
    if (x == (1LL << n) - 1) {
        return (1LL << n);
    } else {
        return best_position(n - 1, (x + 1) / 2);
    }
}

void alg() {
    int n;
    LL p;
    cin >> n >> p;
    LL must_win, can_win;
    {
        LL l = 0;
        LL r = (1LL << n) - 1;
        while (l < r) {
            LL c = (l + r + 1) / 2;
            if (worst_position(n, c) <= p) {
                l = c;
            } else {
                r = c - 1;
            }
        }
        must_win = l;
    }
    {
        LL l = 0;
        LL r = (1LL << n) - 1;
        while (l < r) {
            LL c = (l + r + 1) / 2;
            if (best_position(n, c) <= p) {
                l = c;
            } else {
                r = c - 1;
            }
        }
        can_win = l;
    }
    cout << must_win << " " << can_win << endl;
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
