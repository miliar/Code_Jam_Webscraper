#include <bits/stdc++.h>
#define sz(x) (int((x).size()))
#define pb push_back
#define eb emplace_back
#define all(x) (x).begin(), (x).end()
template<typename T> bool domax(T &a, T b) { return (b > a ? (a = b, true) : false); }
template<typename T> bool domin(T &a, T b) { return (b < a ? (a = b, true) : false); }
typedef long long ll;

void clear() {
}

const int maxn = 105, maxl = 55;

int n, l;
char g[maxn][maxl], b[maxl];

int main() {
    int testcases; scanf("%d", &testcases);
    for (int testnum = 1; testnum <= testcases; testnum++) {
        printf("Case #%d: ", testnum);
        scanf("%d%d", &n, &l);
        for (int i = 0; i < n; i++) scanf(" %s", g[i]);
        scanf(" %s", b);
        bool rip = false;
        for (int i = 0; i < n; i++) if (strcmp(g[i], b) == 0) rip = true;
        if (rip) {
            printf("IMPOSSIBLE\n");
        } else {
            //printf("%s ", b);
            if (l == 1) {
                if (b[0] == '1') printf("0 ");
                else printf("1 ");
            } else {
                for (int i = 0; i < l-1; i++) printf("%c", b[i]);
                printf(" ");
            }
            for (int i = 0; i < l; i++) {
                if (b[i] == '0') b[i] = '1';
                else b[i] = '0';
                printf("%c?", b[i]);
            }
            printf("\n");
        }
        clear();
    }
}

