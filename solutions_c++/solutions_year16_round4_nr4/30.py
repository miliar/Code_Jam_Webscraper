#include <bits/stdc++.h>
#define sz(x) (int((x).size()))
#define pb push_back
#define eb emplace_back
#define all(x) (x).begin(), (x).end()
template<typename T> bool domax(T &a, T b) { return (b > a ? (a = b, true) : false); }
template<typename T> bool domin(T &a, T b) { return (b < a ? (a = b, true) : false); }
typedef long long ll;

const int maxn = 4;

int n, g[maxn], h[maxn], ans = maxn*maxn, bc[(1<<maxn) + 5];
char tmp[maxn];
bool doneperson[maxn], donejob[maxn];

void clear() {
    ans = maxn*maxn;
}
bool ho(int d) {
    if (d == n) return true;
    else {
        bool allg = true;
        for (int i = 0; allg && i < n; i++) if (!doneperson[i]) {
            doneperson[i] = true;
            bool good = false;
            for (int j = 0; j < n; j++) if (!donejob[j] && (h[i] & (1<<j))) good = true;
            for (int j = 0; good && j < n; j++) if (!donejob[j] && (h[i] & (1<<j))) {
                donejob[j] = true;
                if (!ho(d+1)) good = false;
                donejob[j] = false;
            }
            doneperson[i] = false;
            if (!good) allg = false;
        }
        return allg;
    }
}
void go(int i, int teachtotal) {
    if (i == n) {
        if (teachtotal < ans && ho(0)) {
            ans = teachtotal;
            //printf("teachtotal = %d\n", teachtotal);
            //for (int i = 0; i < n; i++) {
            //    printf("i = %d: ", i);
            //    for (int j = 0; j < n; j++) printf("%d ", ((g[i] & (1<<j)) >> j));
            //    printf("\n");
            //}
        }
    } else {
        for (int teach = 0; teach < (1<<n); teach++) {
            if ((teach & g[i]) == 0 && bc[teach] + teachtotal < ans) {
                h[i] = teach | g[i];
                go(i+1, teachtotal + bc[teach]);
            }
        }
    }
}
int bitcount(int k) {
    int c = 0;
    for (int b = 0; b < maxn; b++) if (k & (1<<b)) c++;
    return c;
}

int main() {
    for (int i = 0; i < (1<<maxn); i++) bc[i] = bitcount(i);
    //for (int i = 0; i < (1<<maxn); i++) printf("i = %d, bc[i] = %d\n", i, bc[i]);
    int testcases; scanf("%d", &testcases);
    for (int testnum = 1; testnum <= testcases; testnum++) {
        printf("Case #%d: ", testnum);
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf(" %s", tmp);
            g[i] = 0;
            for (int j = 0; j < n; j++) if (tmp[j] == '1') g[i] |= (1<<j);
        }
        go(0, 0);
        printf("%d\n", ans);
        clear();
    }
}

