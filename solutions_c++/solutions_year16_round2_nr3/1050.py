#include <bits/stdc++.h>

using namespace std;

pair<int, int> v[32];

int main() {

    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);

    int T; scanf("%d", &T);
    char s[32], t[32];
    string S;

    for(int ncase=1; ncase<=T; ncase++) {
        int n;
        scanf("%d", &n);

        map<string, int> M;
        int cnt = 1;
        int idx;
        for(int i=0; i<n; i++) {
            scanf("%s %s", s, t);

            idx = M[S = s];
            if (idx == 0) M[S] = idx = cnt++;
            v[i].first = idx;

            idx = M[S = t];
            if (idx == 0) M[S] = idx = cnt++;
            v[i].second = idx;
        }

        /*for(int i=0; i<n; i++) {
            printf("%d %d\n", v[i].first, v[i].second);
        }*/

        int best = 0;
        for(int mask=0; mask<(1<<n); mask++) {
            int fake = 0;
            int i;
            for(i=0; i<n; i++) {
                if (((1<<i)&mask) == 0) continue;
                fake++;
                bool first = false, second = false;
                for(int j=0; j<n; j++) {
                    if (((1<<j)&mask) == 0) {
                        if (v[j].first == v[i].first) first = true;
                        if (v[j].second == v[i].second) second = true;
                    }
                }
                if (!first || !second) break;
            }
            if (i == n) best = max(fake, best);
        }

        printf("Case #%d: %d\n", ncase, best);
    }

    return 0;
}
