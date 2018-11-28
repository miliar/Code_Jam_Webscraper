#include <cstdio>
#include <cstring>

const int mul[4][4] = {
    {0, 1, 2, 3},
    {1, 4, 3, 6},
    {2, 7, 4, 1},
    {3, 2, 5, 4}
};

int Test, L, X;
char s[200010];
int rd[200010], rs[200010];

int main() {
    scanf("%d", &Test);
    for (int T = 1; T <= Test; ++T) {
        scanf("%d%d", &L, &X);
        scanf("%s", s);
        for (int i = 1; i < X; ++i)
            memcpy(s + i * L, s, L * sizeof(char));
        s[X * L] = '\0';
        L *= X;

        rd[L] = 0, rs[L] = 0;
        for (int k = L - 1; k >= 0; --k) {
            int ret = mul[s[k] - 'h'][rd[k + 1]];
            if (ret & 4) rs[k] = rs[k + 1] ^ 1;
            else rs[k] = rs[k + 1];
            rd[k] = ret & 3;
        }

        int ld = 0, ls = 0;
        bool found = false;
        for (int i = 0; i < L - 2; ++i) {
            int ret = mul[ld][s[i] - 'h'];
            if (ret & 4) ls ^= 1;
            ld = ret & 3;
            if (ls != 0 || ld != 1) continue;

            int md = 0, ms = 0;
            for (int j = i + 1; j < L - 1; ++j) {
                ret = mul[md][s[j] - 'h'];
                if (ret & 4) ms ^= 1;
                md = ret & 3;
                if (ms != 0 || md != 2) continue;

                if (rd[j + 1] == 3 && rs[j + 1] == 0) {
                    found = true;
                    break;
                }
            }
            if (found) break;
        }
        printf("Case #%d: %s\n", T, found ? "YES" : "NO");
    }
}
