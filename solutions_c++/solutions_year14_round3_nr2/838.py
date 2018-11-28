#include <cstdio>
#include <cstring>
#include <algorithm>
//freopen("A-large.in", "r", stdin);
//freopen("A-large.out", "w", stdout);
using namespace std;
const int MAXN = 15;
char str[MAXN][MAXN * 10];
int n;
int G[MAXN][MAXN];
int cnt;
int vis[MAXN];


int main() {
    int T;
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%s", str[i]);
        }
        int a[15];
        for (int i = 0; i < n; i++) {
            a[i] = i;
        }
        int cnt = 0;
        do {
            char ss[MAXN * 100];
            memset(ss, 0, sizeof(ss));
            for (int i = 0; i < n; i++) {
                strcat(ss, str[a[i]]);
            }
            int len = strlen(ss);
            //printf("%s\n", ss);
            int ok = 1;
            for (int i = 0; i < len - 1 && ok; i++) {
                if (ss[i] != ss[i - 1]) {
                    for (int j = i; j < len; j++) {
                        if (ss[j] == ss[i - 1]) {
                            ok = 0;
                            break;
                        }
                    }
                }
            }
            if (ok) {
                ++ cnt;
            }
        }while (next_permutation(a, a + n));
        printf("Case #%d: %d\n", cas, cnt);
    }
    return 0;
}


/*
3
3
ab bbbc cd
4
aa aa bc c
2
abc bcd
*/
