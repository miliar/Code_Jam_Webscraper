/**
 * Author : Parachvte (ryannx6@gmail.com)
 * Date   : 04/10/2016
 */

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define range(i, a, b) for (int i = (a), _end_ = (b); i <= _end_; ++i)
#define rep(i, n) for (int i = (0), _end_ = (n); i < _end_; ++i)
#define pb push_back
#define mp make_pair
#define INF 1000000000
#define MOD 1000000007
#define EPS 1e-6

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;

#define INF 1000000000
#define MOD 1000000007
#define EPS 1e-6

void solve() {
    int n;
    scanf("%d", &n);

    if (n == 0) {
        printf("INSOMNIA\n");
        return;
    }

    bool appear[10];
    rep(i, 10) appear[i] = false;
    int count = 0;

    for (int i = 1; ; i++) {
        LL now = (LL)(n) * i;
        while (now) {
            int last = now % 10;
            now /= 10;
            if (!appear[last]) {
                appear[last] = true;
                count++;
            }
        }
        if (count == 10) {
            printf("%lld\n", (LL)(n) * i);
            return;
        }
    }
}

int main() {
#ifdef DEBUG
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    std::ios_base::sync_with_stdio(false);

    int T;
    scanf("%d", &T);
    rep(i, T) {
        printf("Case #%d: ", i + 1);
        solve();
    }
    
    return 0;
}
