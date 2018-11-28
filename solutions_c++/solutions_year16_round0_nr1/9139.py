#include <cstdio>
#include <utility>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <unordered_map>
#include <map>
using namespace std;

#define REP(i, x) for (int i = 0; i < (x); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define ALL(a) (a).begin(), (a).end()

typedef long long ll;

int main() {
    int T;
    ll N;
    scanf("%d", &T);

    REP (i, T) {
        scanf("%lld", &N);
        if (N == 0) printf("Case #%d: INSOMNIA\n", i + 1);
        else {
            int ans = 1;
            ll N2 = N;
            bool occur[10];
            fill(occur, occur + 10, false);
            while (true) {
                char buf[1000];
                bool f = true;

                sprintf(buf, "%lld", N2);
                REP (j, strlen(buf)) {
                    occur[buf[j] - '0'] = true;
                }

                REP (j, 10) f = f && occur[j];
                if (f) break;

                ans++;
                N2 += N;
            }
            printf("Case #%d: %lld\n", i + 1, N2);
        }
    }

    return 0;
}
