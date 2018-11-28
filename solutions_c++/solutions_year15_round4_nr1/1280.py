#include <bits/stdc++.h>

const int hi[] = {0, 0, 1, -1};
const int hj[] = {1, -1, 0, 0};
const char sym[] = {'>', '<', 'v', '^'};

char s[200][200];

int main() {
    int ct;
    scanf("%d", &ct);
    for (int nt = 1; nt <= ct; nt++) {
        int r, c;
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; i++) scanf("%s", s[i]);
        int res = 0;
        for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            if (s[i][j] == '.') continue;
            if (res == -1) break;
            bool ok = false;
            bool ok2 = false;
            for (int k = 0; k < 4; k++) {
                bool ok3 = false;
                int ii = i + hi[k], jj = j + hj[k];
                while (ii >= 0 && ii < r && jj >= 0 && jj < c) {
                    if (s[ii][jj] != '.') {
                        ok3 = true;
                        break;
                    }
                    ii += hi[k];
                    jj += hj[k];
                }
                if (ok3) {
                    ok2 = true;
                    if (sym[k] == s[i][j]) ok = true;
                }
            }
            if (ok2) {
                if (!ok) res++;
            }
            else res = -1;
        }
        printf("Case #%d: ", nt);
        if (res == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", res);
    }
    return 0;
}
