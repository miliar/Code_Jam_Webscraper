#include <bits/stdc++.h>
using namespace std;
int N, L, TC;
char tmp[500];
int main() {
    scanf("%d", &TC);
    for (int T = 1; T <= TC; ++T) {
        scanf("%d%d", &N, &L);
        bool fail = 0;
        for (int i = 0; i < N; ++i) {
            scanf("%s", tmp);
            bool allones = 1;
            for (int k = 0; k < L && allones; ++k) {
                if (tmp[k] != '1') allones = 0;
            }
            if (allones) fail = 1;
        }
        scanf("%s", tmp);
        printf("Case #%d: ", T);
        if (fail) {
            puts("IMPOSSIBLE");
            continue;
        }
        if (L == 1) printf("0");
        for (int i = 0; i < L-1; ++i) printf("?0");
        printf(" ");
        for (int i = 0; i < L-1; ++i) printf("1");
        printf("0?");
        for (int i = 0; i < L-1; ++i) printf("1");
        puts("");
    }
}