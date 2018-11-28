#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int c[4][4] = {
    0, 1, 2, 3,
    1, 0, 3, 2,
    2, 3, 0, 1,
    3, 2, 1, 0
};
int b[4][4] = {
    1, 1, 1, 1,
    1, -1, 1, -1,
    1, -1, -1, 1,
    1, 1, -1, -1
};
struct abc{
    int t, v;
    abc operator * (const abc &a) const {
        abc re;
        re.t = t * a.t * b[v][a.v];
        re.v = c[v][a.v];
        return re;
    }
    abc operator * (char ch) const {
        abc a;
        a.t = 1; a.v = ch - 'i' + 1;
        return (*this) * a;
    }
};
char s[40010], ts[40010];
int main() {
    int T, ri = 1, n, k, i, j;
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &k);
        scanf("%s", s);
        printf("Case #%d: ", ri++);
        abc r; r.t = 1; r.v = 0;
        for (i = 0; s[i]; i++) r = r * s[i];
        abc t; t.t = 1; t.v = 0;
        for (int i = 0; i < k % 4; i++) t = t * r;
        if (t.t != -1 || t.v != 0) {
            printf("NO\n");
            continue;
        }
        strcpy(ts, s);
        strcat(s, ts);
        strcpy(ts, s);
        strcat(s, ts);
        r.t = 1; r.v = 0;
        int posi = -1;
        for (i = 0; s[i]; i++) {
            r = r * s[i];
            if (r.t == 1 && r.v == 1) {
                posi = i + 1;
                break;
            }
        }
        r.t = 1; r.v = 0;
        int posk = -1;
        for (i = 0; s[i]; i++) {
            abc t; t.t = 1; t.v = s[n * 4 - 1 - i] - 'i' + 1;
            r = t * r;
            if (r.t == 1 && r.v == 3) {
                posk = i + 1;
                break;
            }
        }
        if (posi >= 0 && posk >= 0 && posi + posk < 1ll * n * k) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
