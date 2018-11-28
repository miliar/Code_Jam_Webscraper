#include <bits/stdc++.h>
using namespace std;

int T, R, C, W, arr[10][10];

bool not_possible(bool b[]) {
    int lastpos = -1;
    for (int i = 0; i < C; i++) {
        if (b[i]) {
            if (i - lastpos - 1 >= W) return false;
            else lastpos = i;
        }
    }
    return !(C - lastpos - 1 >= W);
}

int main() {
    freopen("a.in", "r", stdin);
    FILE *out = fopen("a.out", "w");
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        scanf("%d%d%d", &R, &C, &W);
        vector<int> V;
        for (int i = 0; i < C; i++) V.push_back(i);
        int ans = 200;
        do {
            int tries = 0, hits = 0;
            bool b[11];
            memset(b, 0, sizeof(b));
            for (int i = 0; i < C; i++) {
                tries++;
                int target = V[i];
                b[target] = 1;
                if (not_possible(b)) {
                    b[target] = 0;
                    hits++;
                }
                if (hits == W) break;
            }
            ans = min(ans, tries);
        } while (next_permutation(V.begin(), V.end()));
        printf("TC %d done.\n", tc);
        fprintf(out, "Case #%d: %d\n", tc, ans);
    }
}
