#include <cstdio>
int N, M, T, a[105][105];
int main() {
    scanf("%d", &T);
    for (int tc=1;tc<=T;++tc) {
        scanf("%d%d", &N, &M);
        for (int i=1;i<=N;++i)
            for (int j=1;j<=M;++j)
                scanf("%d", &a[i][j]);
        bool ok = true;
        for (int i=1;i<=N;++i) {
            for (int j=1;j<=M;++j) {
                bool ckn = true, ckm = true;
                for (int k=1;k<=N;++k) if (a[k][j] > a[i][j]) ckn = false;
                for (int k=1;k<=M;++k) if (a[i][k] > a[i][j]) ckm = false;
                if (!(ckn || ckm)) ok = false;
            }
        }
        printf("Case #%d: %s\n", tc, ok?"YES":"NO");
    }
    return 0;
}
