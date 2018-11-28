#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;

bool vs[20];

inline int add(ll n) {
    int c = 0;
    while(n) {
        c += !vs[n % 10];
        vs[n % 10] = true;
        n /= 10;
    }
    return c;
}

ll solve(ll n) {
    memset(vs, 0, sizeof(vs));
    int c = add(n);
    ll ans = n;
    while(c < 10) {
        ans += n;
        c += add(ans);
    }
    return ans;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", cas);
        if(n == 0) {
            puts("INSOMNIA");
            continue;
        }
        printf("%I64d\n", solve(n));
    }
    return 0;
}
