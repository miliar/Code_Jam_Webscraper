#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define SZ size()
#define AA first
#define BB second
#define BG begin()
#define ED end()
#define SQ(x) ((x)*(x))
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)

#define NAME "c-small"

LL isprime(LL x) {
    for(LL i = 2; i * i < x; ++i) {
        if (x % i == 0) return i;
    }
    return 0;
}

int check(int x, int n) {
    vector<LL> ans;
    for(LL base = 2; base <= 10; ++base) {
        LL y = 0;
        for(int i = n - 1; i >= 0; --i) {
            y *= base;
            if (x & (1<<i)) {
                y += 1;
            }
        }
        LL flag = isprime(y);
        if(!flag) return false;
        else ans.PB(flag);
    }

    for(int i = n - 1; i >= 0; --i) {
        if (x & (1<<i)) {
            putchar('1');
        }
        else {
            putchar('0');
        }
    }
    for(int i = 0; i < ans.size(); ++i) {
        cout << " " << ans[i];
    }
    cout << endl;
    return true;
}

int main() {
    //freopen(NAME".in", "r", stdin);
    freopen(NAME".out", "w", stdout);
    int i, j, k, u, v, w;
    int n;
    int te;
    cin >> te;
    for(int ca = 1; ca <= te; ++ca) {
        printf("Case #%d:\n", ca);
        cin >> n >> j;

        for (int i = 0; i < (1<<(n - 2)) ; ++i) {
            if (check(1 | (i << 1) | 1 << (n - 1), n)) {
                --j;
                if(j == 0) break;
            }
        }
    }
    return 0;
}
