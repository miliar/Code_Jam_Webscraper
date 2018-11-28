//
// upanddown.cpp
//
// Siwakorn Srisakaokul - ping128
// Written on Saturday, 31 May 2014.
//

#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <algorithm>
#include <map>
#include <ctype.h>
#include <string.h>

#include <assert.h>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<PII, int> PII2;

#define MAXN 1000005

int in[MAXN];
int N;
LL sum;
LL sum2[MAXN];
void solve() {
    sum = 0;
    LL p, q, r, s;
    cin >> N >> p >> q >> r >> s;
    for (int i = 0; i < N; i++) {
        in[i] = (i * p + q) % r + s;
        sum += in[i];
    }

    if (sum == 0) {
        printf("0\n");
    } else if (N == 1) {
        printf("0\n");
    } else if (N == 2) {
        printf("%.9lf\n", min(in[0], in[1]) * 1.0 / (in[0] + in[1]));
    } else {

        memset(sum2, 0, sizeof(sum2));
        for (int i = N - 1; i >= 0; i--) {
            sum2[i] = sum2[i + 1] + in[i];
        }
        LL maxx = 0;
        LL s1 = 0;
        multiset<LL> S;
        for (int i = 1; i < N; i++) {
            S.insert(sum2[i]);
        }
        for (int p1 = 0; p1 < N - 2; p1++) {
            s1 += in[p1];
            S.erase(S.find(sum2[p1 + 1]));
            LL temp = sum - s1;
            auto it = S.lower_bound(temp / 2);
            if (it != S.end()) {
                maxx = max(maxx, sum - max(s1, max(temp - (*it), *it)));
                auto it2 = it;
                it2++;
                if (it2 != S.end())
                    maxx = max(maxx, sum - max(s1, max(temp - (*it2), *it2)));
            }
            if (it != S.begin()) {
                auto it2 = it;
                it2--;
                if (it2 != S.end())
                    maxx = max(maxx, sum - max(s1, max(temp - (*it2), *it2)));
            }
        }
        printf("%.9lf\n", maxx * 1.0 / sum);
    }
}

int main() {
    int test;
    scanf("%d", &test);
    for (int tt = 0; tt < test; tt++) {
        printf("Case #%d: ", tt + 1);
        solve();
        //        if (tt == 1) break;
    }
    return 0;
}
