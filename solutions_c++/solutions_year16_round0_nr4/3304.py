#include <cstdio>

typedef long long int ll;

void solve(int K, int C, int S) {
    if(K/C > S) {
        printf(" IMPOSSIBLE");
        return;
    }
    for(int i = 1; i <= K; i+=C) {
        ll v = 0;
        for(int j = i; j-i<C && j <= K; j++) {
            v *= K;
            v += (j-1);
        }
        printf(" %lld", v+1);
    }
}

int main() {

    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++) {
        int K, C, S;
        scanf("%d %d %d", &K, &C, &S);
        printf("Case #%d:", t);
        solve(K, C, S);
        printf("\n");
    }
}
