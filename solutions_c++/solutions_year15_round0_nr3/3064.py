#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int T, L, X;
char str[12001];

int c[5][5] = {
    {0, 0, 0, 0, 0},
    {0, 1, 2, 3, 4},
    {0, 2, -1, 4, -3},
    {0, 3, -4, -1, 2},
    {0, 4, 3, -2, -1}
};

int C(int i, char j) {
    return c[abs(i)][j - 'g'] * (i > 0 ? 1 : -1);
}

int f[12001][12001];

void solve() {
    scanf("%d%d", &L, &X);
    scanf("%s", str);
    for (int t=1;t<X;t++) for (int i=0;i<L;i++) {
        str[t * L + i] = str[i];
    }
    str[X * L] = '\0';
    int n = strlen(str);
    for (int i=0; i<n; i++) {
        int cur = 1;
        for (int j=i; j<n; j++) {
            cur = C(cur, str[j]);
            f[i][j] = cur;
        }
    }

    for (int i=0; i<n; i++) if (f[0][i-1] == 2) {
        for (int j=i+1; j<=n-1; j++) if (f[i][j-1] == 3 && f[j][n-1] == 4) {
           // for (int k=0;k<=i;k++) printf("%c", str[k]);
           // printf(" ");
           // for (int k=i+1;k<=j;k++) printf("%c", str[k]);
           // printf(" ");
           // for (int k=j+1;k<=n-1;k++) printf("%c", str[k]);
            printf("YES");
            return;
        }
    }
    printf("NO");
}

int main() {
    freopen("c.txt", "r", stdin);
    scanf("%d", &T);
    for (int i=1; i<=T; i++) {
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
    return 0;
}
